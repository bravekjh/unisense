from __future__ import absolute_import

from unisense.exception import InputFormatError


# english docs checker
def docs_checker(docs):
    if type(docs) is not list:
        raise InputFormatError
    for t in docs:
        if type(t) is not str:
            raise InputFormatError

    # check language
    # to do

    return




