import json

from django.http import JsonResponse, HttpRequest, HttpResponse
from opt_out.public_api.api.models import FurtherDetailsForm
from opt_out.public_api.api.models import SubmissionForm


def submit(request: HttpRequest) -> JsonResponse:
    data = json.loads(request.body.decode("utf-8"))

    try:
        form = SubmissionForm(data)
        if not form.is_valid():
            return HttpResponse(status=400)
    except AttributeError:
        return HttpResponse(status=400)

    item = form.save(commit=False)
    item.save()
    response = {"submission_id": item.submission_id}
    return JsonResponse(response)


def submit_further_details(request: HttpRequest) -> HttpResponse:
    data = json.loads(request.body.decode("utf-8"))

    form = FurtherDetailsForm(data)
    if not form.is_valid():
        return HttpResponse(status=400)

    item = form.save(commit=False)
    item.save()
    return HttpResponse("Thank you for your submission")


def home(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Welcome to Opt Out API")
