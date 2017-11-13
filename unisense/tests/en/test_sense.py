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

def test_en_model_kw(en_rule):
    model = en_rule
    vocab = {'hello': -1, 'word': -1, 
             'hello world': -1, 'world hello': -1}
    model.train(vocab)
    model.create_matcher()
    assert model.kw_match(['hello World Hello']) == \
        [[{'end': 17, 'start': 0, 'word': 'hello World Hello'}]]
    assert model.kw_match(['hello World word']) == \
        [[{'end': 11, 'start': 0, 'word': 'hello World'},
          {'end': 16, 'start': 12, 'word': 'word'}]]
