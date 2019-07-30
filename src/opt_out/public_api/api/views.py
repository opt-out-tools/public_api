from django.http import JsonResponse, HttpRequest, HttpResponse
from opt_out.public_api.api.models import SubmissionForm

from opt_out.public_api.api.models import FurtherDetailsForm


def submit(request: HttpRequest) -> JsonResponse:
    form = SubmissionForm(request.POST)
    if not form.is_valid():
        return HttpResponse(status=400)

    item = form.save(commit=False)
    item.save()
    response = {"submission_id": item.submission_id}
    return JsonResponse(response)


def submit_further_details(request: HttpRequest) -> HttpResponse:
    form = FurtherDetailsForm(request.POST)
    if not form.is_valid():
        return HttpResponse(status=400)

    item = form.save(commit=False)
    item.save()
    return HttpResponse("Thank you for your submission")


def home(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Welcome to Opt Out API")
