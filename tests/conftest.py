# -*- coding: utf-8 -*-
"""
    Dummy conftest.py for apps.

    If you don't know what this is for, just leave it empty.
    Read more about conftest.py under:
    https://pytest.org/latest/plugins.html
"""

import pytest
from hypothesis._strategies import just
from hypothesis.extra.django import from_model
from opt_out.public_api.api.enums import PerpetratorType, InteractionType, ReactionType
from opt_out.public_api.api.models import Submission


@pytest.fixture
def submit_urls_request():
    yield {
        "urls": ["https://twitter.com/i=1", "https://twitter.com/i=2"],
        "self_submission": True,
        "is_part_of_larger_attack": True,
    }


@pytest.fixture
def submit_details_request(db):
    submission = from_model(Submission, urls=just(['http://twitter.com/'])).example()
    yield {
        "identify": "female",
        "age": 40,
        "job": 'public speaker',
        "perpetrator": PerpetratorType.single_stranger.value,
        'interaction': InteractionType.post_rarely_for_friends.value,
        'reaction_type': ReactionType.i_took_a_break_from_platform.value,
        'experienced': ['sad'],
        'feeling': 'hurt',
        'submission': submission.id
    }
