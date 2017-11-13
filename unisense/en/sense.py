from __future__ import absolute_import

from spacy.matcher import Matcher

from unisense.sentiment import RuleSentiment, LogRegSentiment
from unisense.exception import InputFormatError
from unisense.util import lstr_lower
from .util import docs_checker
from unisense.ext_lib import spacy_en


# english rule based sentiment class
class EnRuleSentiment(RuleSentiment):

    # load vocab and create matcher
    def load_model(self, vocab_path):
        super(EnRuleSentiment, self).load_model(vocab_path)

        # create matcher
        self.create_matcher()
    
    # create matcher
    def create_matcher(self):
        self.matcher = Matcher(spacy_en.vocab)
        for k, v in self.sentiment_vocab.items():
            if v < 0:
                pat = [{'LOWER': w.lower()} for w in k.strip().split()]
                self.matcher.add('neg', None, pat)

    # match by model
    def match_vocab(self, docs):
        res_docs = []
        for t in docs:
            doc = spacy_en(t)
            mat = self.matcher(doc)
            mat_merge = []
            for m in mat:
                if len(mat_merge) > 0 and mat_merge[-1][1] == m[1]:
                    mat_merge[-1] = m
                elif len(mat_merge) > 0 and mat_merge[-1][2] == m[2]:
                    continue
                elif len(mat_merge) > 0 and mat_merge[-1][2] > m[1]:
                    mat_merge[-1] = (m[0], mat_merge[-1][1], m[2])
                else:
                    mat_merge.append(m)
            res = []
            for m in mat_merge:
                res.append({'word': doc[m[1]:m[2]].text, 
                            'start': doc[m[1]:m[2]].start_char, 
                            'end': doc[m[1]:m[2]].end_char})
            res_docs.append(res)
        return res_docs

    # sentiment analysis
    def analysis(self, docs):
        super(EnRuleSentiment, self).analysis()

        # check input
        try:
            docs_checker(docs)
        except InputFormatError as e:
            print('Exception', e)
            raise
        
        # to be done
        return 0

    # key word match
    def kw_match(self, docs, ngram=3):
        super(EnRuleSentiment, self).analysis()

        # check input
        try:
            docs_checker(docs)
        except InputFormatError as e:
            print('Exception', e)
            raise

        # match vocab
        return self.match_vocab(docs)


# english logistic regression sentiment class
class EnLogRegSentiment(LogRegSentiment):

    # preprocess for english
    @staticmethod
    def text_preprocess(docs):
        # to do
        return docs

    # sentiment analysis
    def analysis(self, docs):
        super(EnLogRegSentiment, self).analysis()

        # check input
        try:
            docs_checker(docs)
        except InputFormatError as e:
            print('Exception', e)
            raise

        # preprocess before pipeline
        docs = self.text_preprocess(docs)

        # return sentiment prob
        return self.doc_clf.predict_proba(docs)

