import json

from django.http import JsonResponse, HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from opt_out.public_api.api.machine_learning import TextSentimentPrediction
from opt_out.public_api.api.models import SubmissionDetailsForm, PredictionForm
from opt_out.public_api.api.models import SubmissionForm


@csrf_exempt
def submit(request: HttpRequest) -> JsonResponse:
    data = json.loads(request.body.decode("utf-8"))

    try:
        form = SubmissionForm(data)
        if not form.is_valid():
            return JsonResponse(form.errors, status=400)
    except AttributeError:
        return JsonResponse({'form': 'invalid request'}, status=400)

    item = form.save(commit=False)
    item.save()
    response = {"submission_id": item.id}
    return JsonResponse(response, status=201)


@csrf_exempt
def submit_further_details(request: HttpRequest) -> HttpResponse:
    data = json.loads(request.body.decode("utf-8"))

    form = SubmissionDetailsForm(data)
    if not form.is_valid():
        return JsonResponse(form.errors, status=400)

    item = form.save(commit=False)
    item.save()
    return HttpResponse("Thank you for your submission", status=201)


@csrf_exempt
def predict(request: HttpRequest) -> JsonResponse:
    data = json.loads(request.body.decode('utf-8'))

    form = PredictionForm(data)
    if not form.is_valid():
        return JsonResponse(form.errors, status=400)

    predictor = TextSentimentPrediction()
    predictions = predictor(form['texts'].data)
    predictions = predictions >= .5
    predictions = predictions.flatten().tolist()
    return JsonResponse({
        'predictions': predictions
    })


def home(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Welcome to Opt Out API")
