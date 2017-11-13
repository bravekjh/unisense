from __future__ import absolute_import

from unisense.sentiment import RuleSentiment, LogRegSentiment
from unisense.exception import InputFormatError


# french rule based sentiment class
class FrRuleSentiment(RuleSentiment):

    # text preprocess
    @staticmethod
    def text_preprocess(docs):
        # to do
        return docs

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

    # sentiment analysis
    def analysis(self, docs):
        super(FrRuleSentiment, self).analysis()

        # check docs
        # to do

        # get word attribute
        word_attrib = self.text_preprocess(docs)

        # vocab lookup
        chunk_score = self.vocab_lookup(word_attrib)

        # weighted
        return self.weight_mean(chunk_score)