from __future__ import absolute_import

from unisense.sentiment import RuleSentiment, LogRegSentiment
from unisense.exception import InputFormatError
from unisense.util import lstr_lower
from .util import docs_checker
from unisense.ext_lib import spacy_en


# english rule based sentiment class
class EnRuleSentiment(RuleSentiment):

    # text preprocess
    @staticmethod
    def text_preprocess(docs):
        # tokenize by spacy
        docs_tok = []
        for t in docs:
            docs_tok.append([str(tok) for tok in spacy_en.tokenizer(t)])

        return docs_tok

    # lookup in vocab
    @staticmethod
    def vocab_lookup(word_attrib):
        # to do
        return word_attrib

    # weighted average for score
    @staticmethod
    def weight_mean(chunk_score):
        # to do
        return chunk_score

    # match by model
    def match_vocab(self, docs_tok, ngram):

        docs_marked = []

        for t in docs_tok:
            doc_marked = ''
            idx = 0

            while idx < len(t):

                # wait for refactor with ngram condition

                # tri
                if self.sentiment_vocab.get(lstr_lower(t[idx:idx + 3]), 0) < 0:
                    doc_marked += "<mark data-entity=\"neg\">"
                    doc_marked += ' '.join(t[idx:idx + 3]) + "</mark>" + ' '
                    idx += 3

                # bi
                elif self.sentiment_vocab.get(lstr_lower(t[idx:idx + 2]), 0) < 0:
                    doc_marked += "<mark data-entity=\"neg\">"
                    doc_marked += ' '.join(t[idx:idx + 2]) + "</mark>" + ' '
                    idx += 2

                # uni
                elif self.sentiment_vocab.get(lstr_lower(t[idx:idx + 1]), 0) < 0:
                    doc_marked += "<mark data-entity=\"neg\">"
                    doc_marked += ' '.join(t[idx:idx + 1]) + "</mark>" + ' '
                    idx += 1

                else:
                    doc_marked += ' '.join(t[idx:idx + 1]) + ' '
                    idx += 1

            docs_marked.append(doc_marked.replace('\r\n', '\n').replace('\n', '<br>'))

        return docs_marked

    # sentiment analysis
    def analysis(self, docs):
        super(EnRuleSentiment, self).analysis()

        # check input
        try:
            docs_checker(docs)
        except InputFormatError as e:
            print('Exception', e)
            raise

        # preprocess for text
        docs_tok = self.text_preprocess(docs)

        # vocab lookup
        chunk_score = self.vocab_lookup(docs_tok)

        # weighted
        return self.weight_mean(chunk_score)

    # key word match
    def kw_match(self, docs, ngram=3):
        super(EnRuleSentiment, self).analysis()

        # check input
        try:
            docs_checker(docs)
        except InputFormatError as e:
            print('Exception', e)
            raise

        # preprocess for text
        docs_tok = self.text_preprocess(docs)

        # match key word
        return self.match_vocab(docs_tok, ngram)


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

