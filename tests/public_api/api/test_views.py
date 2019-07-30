# pylint: disable=invalid-name, unused-argument
import django.test
from hypothesis import given
import hypothesis.strategies as st
import pytest


def test_save_post_request(client: django.test.Client, db, submit_urls_request):
    response = client.post("/submit_urls", data=submit_urls_request)
    assert response.status_code == 200
    assert "submission_id" in response.json()


def test_save_multiple_consecutive_post_request(client: django.test.Client, db, submit_urls_request):
    response = client.post("/submit_urls", data=submit_urls_request)
    assert response.status_code == 200
    assert "submission_id" in response.json()
    submission_id = response.json()["submission_id"]

    response = client.post("/submit_urls", data=submit_urls_request)
    assert response.status_code == 200
    assert "submission_id" in response.json()
    assert submission_id + 1 == response.json()["submission_id"]


@pytest.mark.parametrize("key", ["urls", "self_submission", "is_part_of_larger_attack"])
def test_invalid_request(key, client: django.test.Client, submit_urls_request):
    del submit_urls_request[key]
    response = client.post("/submit_urls", data=submit_urls_request)
    assert response.status_code == 400


def test_invalid_request_keys(client):
    response = client.post("/submit_urls", data={1: 1,
                                                 2: 2,
                                                 3: 3})
    assert response.status_code == 400

@given(urls=st.lists(st.text()))
def test_invalid_user_input(urls, client: django.test.Client, submit_urls_request):
    submit_urls_request["urls"] = urls
    response = client.post("/submit_urls", data=submit_urls_request)
    assert response.status_code == 400

@pytest.mark.parametrize("key", ["urls", "self_submission", "is_part_of_larger_attack"])
@pytest.mark.parametrize("key_type", [list, set, dict, int, str])
def test_invalid_request_type(key, key_type, client: django.test.Client, submit_urls_request):
    submit_urls_request[key] = key_type()
    response = client.post("/submit_urls", data=submit_urls_request)
    assert response.status_code == 400
