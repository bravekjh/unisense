from unisense.exception import ModelNotExist, InputFormatError

import pytest
import os

dir_path = os.path.dirname(os.path.realpath(__file__))


def test_en_model_handle_exception(en_logreg):
    model = en_logreg
    with pytest.raises(ModelNotExist):
        model.analysis([''])


def test_en_model_analysis(en_logreg):
    model = en_logreg
    model.load_model(dir_path + '/model/toy_test.pkl')
    with pytest.raises(InputFormatError):
        model.analysis(['test', 233])


