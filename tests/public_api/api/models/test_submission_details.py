# pylint: disable=invalid-name, unused-argument
import hypothesis.strategies as st
import pytest
from hypothesis import given
from opt_out.public_api.api.enums import PerpetratorType, InteractionType, ReactionType
from opt_out.public_api.api.models import SubmissionDetailsForm


def test_details_submission_form_validation_simple(submit_details_request):
    details = SubmissionDetailsForm(submit_details_request)
    assert not details.errors


@given(identify=st.text(min_size=2, max_size=100,
                        alphabet=st.characters(blacklist_categories=("Cs",),
                                               blacklist_characters=['\x00'])).filter(lambda x: x.strip()))
def test_details_submission_form_identify(submit_details_request, identify):
    submit_details_request['identify'] = identify
    details = SubmissionDetailsForm(submit_details_request)
    assert not details.errors


def test_details_submission_identify_above_max_size(submit_details_request):
    submit_details_request['identify'] = 'a' * 101
    details = SubmissionDetailsForm(submit_details_request)
    assert details.errors == {'identify': ['Ensure this value has at most 100 characters (it has 101).']}


def test_details_submission_form_identify_null_characters(submit_details_request):
    submit_details_request['identify'] = '0\x00'
    details = SubmissionDetailsForm(submit_details_request)
    assert details.errors == {'identify': ['Null characters are not allowed.']}


@given(age=st.integers(min_value=0, max_value=32767))
def test_details_submission_form_age(submit_details_request, age):
    submit_details_request['age'] = age
    details = SubmissionDetailsForm(submit_details_request)
    assert not details.errors


def test_details_submission_form_negative_age(submit_details_request):
    submit_details_request['age'] = -1
    details = SubmissionDetailsForm(submit_details_request)
    assert details.errors == {'age': ['Ensure this value is greater than or equal to 0.']}


def test_details_submission_form_above_max_age(submit_details_request):
    submit_details_request['age'] = 32768
    details = SubmissionDetailsForm(submit_details_request)
    assert details.errors == {'age': ['Ensure this value is less than or equal to 32767.']}


@given(job=st.text(min_size=2, max_size=160,
                   alphabet=st.characters(blacklist_categories=("Cs",),
                                          blacklist_characters=['\x00'])).filter(lambda x: x.strip()))
def test_details_submission_job(submit_details_request, job):
    submit_details_request['job'] = job
    details = SubmissionDetailsForm(submit_details_request)
    assert not details.errors


def test_details_submission_job_above_max_size(submit_details_request):
    submit_details_request['job'] = 'a' * 161
    details = SubmissionDetailsForm(submit_details_request)
    assert details.errors == {'job': ['Ensure this value has at most 160 characters (it has 161).']}


def test_details_submission_job_null_characters(submit_details_request):
    submit_details_request['job'] = '0\x00'
    details = SubmissionDetailsForm(submit_details_request)
    assert details.errors == {'job': ['Null characters are not allowed.']}


@pytest.mark.parametrize('perpetrator', [tag.value for tag in PerpetratorType])
def test_details_submission_perpetrator_valid(submit_details_request, perpetrator):
    submit_details_request['perpetrator'] = perpetrator
    details = SubmissionDetailsForm(submit_details_request)
    assert not details.errors


@given(perpetrator=st.text(min_size=2, max_size=40,
                           alphabet=st.characters(blacklist_categories=("Cs",),
                                                  blacklist_characters=['\x00'])))
def test_details_submission_perpetrator_invalid(submit_details_request, perpetrator):
    submit_details_request['perpetrator'] = perpetrator
    details = SubmissionDetailsForm(submit_details_request)
    assert 'perpetrator' in details.errors


@pytest.mark.parametrize('interaction', [tag.value for tag in InteractionType])
def test_details_submission_interaction_valid(submit_details_request, interaction):
    submit_details_request['interaction'] = interaction
    details = SubmissionDetailsForm(submit_details_request)
    assert not details.errors


@given(interaction=st.text(min_size=2, max_size=40,
                           alphabet=st.characters(blacklist_categories=("Cs",),
                                                  blacklist_characters=['\x00'])))
def test_details_submission_interaction_invalid(submit_details_request, interaction):
    submit_details_request['interaction'] = interaction
    details = SubmissionDetailsForm(submit_details_request)
    assert 'interaction' in details.errors


@pytest.mark.parametrize('reaction', [tag.value for tag in ReactionType])
def test_details_submission_reaction_valid(submit_details_request, reaction):
    submit_details_request['reaction'] = reaction
    details = SubmissionDetailsForm(submit_details_request)
    assert not details.errors


@given(reaction=st.text(min_size=2, max_size=40,
                        alphabet=st.characters(blacklist_categories=("Cs",),
                                               blacklist_characters=['\x00'])).filter(lambda x: x.strip()))
def test_details_submission_reaction_invalid(submit_details_request, reaction):
    submit_details_request['reaction_type'] = reaction
    details = SubmissionDetailsForm(submit_details_request)
    assert 'reaction_type' in details.errors


@given(experienced=st.lists(st.text(min_size=2, max_size=300,
                                    alphabet=st.characters(blacklist_categories=("Cs",),
                                                           blacklist_characters=['\x00'])).filter(lambda x: x.strip()),
                            min_size=1))
def test_details_submission_experienced_valid(submit_details_request, experienced):
    submit_details_request['experienced'] = experienced
    details = SubmissionDetailsForm(submit_details_request)
    assert not details.errors


def test_details_submission_experienced_empty(submit_details_request):
    submit_details_request['experienced'] = []
    details = SubmissionDetailsForm(submit_details_request)
    assert details.errors == {'experienced': ['This field is required.']}


@given(feeling=st.text(min_size=2, max_size=300,
                       alphabet=st.characters(blacklist_categories=("Cs",),
                                              blacklist_characters=['\x00'])).filter(lambda x: x.strip()))
def test_details_submission_form_feeling(submit_details_request, feeling):
    submit_details_request['feeling'] = feeling
    details = SubmissionDetailsForm(submit_details_request)
    assert not details.errors


def test_details_submission_feeling_above_max_size(submit_details_request):
    submit_details_request['feeling'] = 'a' * 301
    details = SubmissionDetailsForm(submit_details_request)
    assert details.errors == {'feeling': ['Ensure this value has at most 300 characters (it has 301).']}


@pytest.mark.parametrize('key', ['identify', 'age', 'job', 'perpetrator', 'interaction', 'reaction_type',
                                 'experienced', 'feeling'])
def test_missing_form_fields_from_request(key, submit_details_request):
    del submit_details_request[key]
    details = SubmissionDetailsForm(submit_details_request)
    assert details.errors


def test_details_submissions_invalid_submission_id(submit_details_request):
    submit_details_request['submission'] += 100
    details = SubmissionDetailsForm(submit_details_request)
    assert details.errors

# TODO add IP logging
