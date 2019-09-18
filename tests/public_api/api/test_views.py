# pylint: disable=invalid-name, unused-argument
import json

import django.test
import hypothesis.strategies as st
import pytest
from hypothesis import given


def test_save_post_request(client: django.test.Client, db, submit_urls_request):
    response = client.post("/submit_urls", json.dumps(submit_urls_request), content_type="application/json")
    assert response.status_code == 201
    assert "submission_id" in response.json()


def test_save_multiple_consecutive_post_request(client: django.test.Client, db, submit_urls_request):
    response = client.post("/submit_urls", json.dumps(submit_urls_request), content_type="application/json")
    assert response.status_code == 201
    assert "submission_id" in response.json()
    submission_id = response.json()["submission_id"]

    response = client.post("/submit_urls", json.dumps(submit_urls_request), content_type="application/json")
    assert response.status_code == 201
    assert "submission_id" in response.json()
    assert submission_id + 1 == response.json()["submission_id"]


@pytest.mark.parametrize("key", ["urls", "self_submission", "is_part_of_larger_attack"])
def test_invalid_request(key, client: django.test.Client, submit_urls_request):
    del submit_urls_request[key]
    response = client.post("/submit_urls", json.dumps(submit_urls_request), content_type="application/json")
    assert response.status_code == 400


@given(urls=st.lists(st.text()))
def test_invalid_user_input(urls, client: django.test.Client, submit_urls_request):
    submit_urls_request["urls"] = urls
    response = client.post("/submit_urls", json.dumps(submit_urls_request), content_type="application/json")
    assert response.status_code == 400


@pytest.mark.parametrize("key", ["urls", "self_submission", "is_part_of_larger_attack"])
@pytest.mark.parametrize("key_type", [list("3"), {"t": "est"}, 9, "cookies"])
def test_invalid_request_type(key, key_type, client: django.test.Client, submit_urls_request):
    submit_urls_request[key] = key_type
    response = client.post("/submit_urls", json.dumps(submit_urls_request), content_type="application/json")
    assert response.status_code == 400


def test_further_details_save_post_request(client: django.test.Client, db, submit_details_request):
    response = client.post("/submit_further_details", json.dumps(submit_details_request),
                           content_type="application/json")
    assert response.status_code == 201


def test_get_prediction(client: django.test.client):
    prediction_form_data = {
        'texts': ['You are a lovely person',
                  'all is good']
    }
    response = client.post("/prediction", json.dumps(prediction_form_data),
                           content_type="application/json")
    assert response.status_code == 200
    assert response.json() == {
        'predictions': [False, False]
    }
