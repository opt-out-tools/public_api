from django.http import JsonResponse, HttpRequest, HttpResponse
from opt_out.public_api.api.models import SubmissionForm


def submit(request: HttpRequest) -> JsonResponse:
    form = SubmissionForm(request.POST)
    if not form.is_valid():
        return HttpResponse(status=400)

    item = form.save(commit=False)
    item.save()
    response = {"submission_id": item.submission_id}
    return JsonResponse(response)

def home(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Welcome to Opt Out API")
