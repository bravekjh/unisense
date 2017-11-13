from __future__ import absolute_import

from abc import ABCMeta, abstractmethod
from collections import defaultdict

from sklearn.externals import joblib

from .exception import ModelNotExist, VocabFormatError
from .util import load_pickle, save_pickle


# base sentiment class
class BaseSentiment(metaclass=ABCMeta):

    def __init__(self, *args, **kwargs):
        self._has_model = False
    
    @abstractmethod
    def train(self, *args, **kwargs):
        # train
        self._has_model = True
    
    @abstractmethod
    def load_model(self, *args, **kwargs):
        # load model
        self._has_model = True

    @abstractmethod
    def save_model(self, *args, **kwargs):
        # save model
        pass
    
    @abstractmethod
    def analysis(self, *args, **kwargs):
        if not self._has_model:
            raise ModelNotExist
        
        # text analysis
        return None

     
# rule based sentiment class
class RuleSentiment(BaseSentiment):

    def __init__(self, vocab_path=None):
        super(RuleSentiment, self).__init__()

        # word sentiment vocabulary
        self.sentiment_vocab = defaultdict(defaultdict)
        if vocab_path is not None:
            self.load_model(vocab_path)

    @staticmethod
    # check vocabulary format
    def vocab_check(test_vocab):
        # string only for key
        for k in test_vocab.keys():
            if type(k) is not str:
                raise VocabFormatError

    # update current vocab
    def train(self, update_vocab):
        # check update vocab
        try:
            self.vocab_check(update_vocab)
        except VocabFormatError as e:
            print('Exception', e)
            raise

        # update current vocab
        for k, v in update_vocab.items():
            self.sentiment_vocab[k] = v

        super(RuleSentiment, self).train()

    # load vocab from pickle file
    def load_model(self, vocab_path):
        # load vocab
        new_vocab = load_pickle(vocab_path)

        # check loaded vocab
        try:
            self.vocab_check(new_vocab)
        except VocabFormatError as e:
            print('Exception', e)
            raise

        self.sentiment_vocab = new_vocab

        super(RuleSentiment, self).load_model()

    # vocab persistence
    def save_model(self, vocab_path):
        # save to pickle
        save_pickle(self.sentiment_vocab, vocab_path)

    # sentiment analysis
    @abstractmethod
    def analysis(self, *args, **kwargs):
        super(RuleSentiment, self).analysis()

        # preprocess and vocab lookup
        pass

    # key word match
    @abstractmethod
    def kw_match(self, *args, **kwargs):
        # check model
        if not self._has_model:
            raise ModelNotExist

        # preprocess and vocab lookup
        pass


# logistic regression sentiment class
class LogRegSentiment(BaseSentiment):
    
    def __init__(self, model_path=None):
        super(LogRegSentiment, self).__init__()

        self.doc_clf = None

        # load model
        if model_path:
            self.load_model(model_path)

    # train model
    def train(self):
        # to do
        super(LogRegSentiment, self).train()

    # load model from pickle file
    def load_model(self, model_path):
        # load pipeline
        self.doc_clf = joblib.load(model_path)

        super(LogRegSentiment, self).load_model()
    
    # save model to pickle file
    def save_model(self, model_path):
        # pipeline persistence
        joblib.dump(self.doc_clf, model_path)

    # sentiment analysis
    @abstractmethod
    def analysis(self, *args, **kwargs):
        super(LogRegSentiment, self).analysis()

        # preprocess and predict
        pass

        



    




