from unisense.en import EnLogRegSentiment, EnRuleSentiment

import pytest


@pytest.fixture
def en_logreg():
    model = EnLogRegSentiment()
    return model

@pytest.fixture
def en_rule():
    model = EnRuleSentiment()
    return model



