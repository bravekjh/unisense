from unisense.en import EnLogRegSentiment

import pytest


@pytest.fixture
def en_logreg():
    model = EnLogRegSentiment()
    return model



