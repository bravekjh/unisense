

class UnisenseError(Exception):
    # unisense related error
    pass


class ModelNotExist(UnisenseError):
    # raised when model does not exist
    def __init__(self, message="need to load or train model before analysis", *args, **kwargs):
        super(ModelNotExist, self).__init__(message, *args, **kwargs)


class VocabFormatError(UnisenseError):
    # raised when model vocab format incorrect
    def __init__(self, message="vocab should be dict of words", *args, **kwargs):
        super(VocabFormatError, self).__init__(message, *args, **kwargs)


class InputFormatError(UnisenseError):
    # raised when model input format incorrect
    def __init__(self, message="input should be list of string", *args, **kwargs):
        super(InputFormatError, self).__init__(message, *args, **kwargs)


