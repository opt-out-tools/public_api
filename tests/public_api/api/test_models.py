# pylint: disable=invalid-name, unused-argument
from opt_out.public_api.api.models import Submission


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


def test_save_self_submission(db):
    first, second = create_submission()
    first.save()
    second.save()

    submissions = Submission.objects.all()
    assert submissions.count() == 2

    assert submissions[0].self_submission == False
    assert submissions[1].self_submission == True


def test_save_is_part_of_larger_attack(db):
    first, second = create_submission()
    first.save()
    second.save()

    submissions = Submission.objects.all()
    assert submissions.count() == 2

    assert submissions[0].is_part_of_larger_attack == True
    assert submissions[1].is_part_of_larger_attack == False
