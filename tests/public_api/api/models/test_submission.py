from opt_out.public_api.api.models import Submission, SubmissionForm


def create_submission():
    first = Submission(urls=["https://twitter.com/i=1"])
    first.self_submission = False
    first.is_part_of_larger_attack = True

    second = Submission(urls=["https://twitter.com/i=2"])
    second.self_submission = True
    second.is_part_of_larger_attack = False

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
