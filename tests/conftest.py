# -*- coding: utf-8 -*-
"""
    Dummy conftest.py for apps.

    If you don't know what this is for, just leave it empty.
    Read more about conftest.py under:
    https://pytest.org/latest/plugins.html
"""

import pytest


@pytest.fixture
def submit_urls_request():
    yield {"urls": ["https://twitter.com/i=1"],
           "self_submission": True,
           "is_part_of_larger_attack": True}
