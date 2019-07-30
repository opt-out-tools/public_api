# pylint: disable=invalid-name, unused-argument
from opt_out.public_api.api.models import Submission, SubmissionForm

from opt_out.public_api.api.enums import Identify
from opt_out.public_api.api.models import FurtherDetails


def create_submission():
    first = Submission(urls=["https://twitter.com/i=1"])
    first.self_submission = False
    first.is_part_of_larger_attack = True

    second = Submission(urls=["https://twitter.com/i=2"])
    second.self_submission = True
    second.is_part_of_larger_attack = False

    return first, second


def add_further_details():
    first = FurtherDetails()
    first.identify = Identify.female

    second = FurtherDetails()
    second.identify = Identify.transgender

    return first, second


def test_save_urls(db):
    first, second = create_submission()
    first.save()
    second.save()

    submissions = Submission.objects.all()
    assert submissions.count() == 2

    assert submissions[0].urls == ["https://twitter.com/i=1"]
    assert submissions[1].urls == ["https://twitter.com/i=2"]

def test_submission_form_validation(submit_urls_request):
    submit_urls_request['urls'] = ['https://twitter.com/i=1', 'https://twitter.com/i=1']
    submissions = SubmissionForm(submit_urls_request)

    assert not submissions.errors

def test_save_self_submission(db):
    first, second = create_submission()
    first.save()
    second.save()

    submissions = Submission.objects.all()
    assert submissions.count() == 2

    assert not submissions[0].self_submission
    assert submissions[1].self_submission


def test_save_is_part_of_larger_attack(db):
    first, second = create_submission()
    first.save()
    second.save()

    submissions = Submission.objects.all()
    assert submissions.count() == 2

    assert submissions[0].is_part_of_larger_attack
    assert not submissions[1].is_part_of_larger_attack


def test_save_identify(db):
    first, second = add_further_details()
    first.save()
    second.save()

    details = FurtherDetails.objects.all()
    assert details.count() == 2

    assert details[0].identify == "Identify.female"
    assert details[1].identify == "Identify.transgender"

