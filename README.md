# unisense


**a homemade python package for sentiment analysis**


## installation
```bash
python setup.py install
```

## requirement
- scikit-learn


## usage
```python
from unisense.en import EnLogRegSentiment
```
a toy model is provided in ***./unisense/test/en/model/***
```python
# create sentiment class
test = EnLogRegSentiment(model_path='./toy_model.pkl')
```
return the sentiment score, input should be list of string
```python
# text analysis
test.analysis(['Hello world!'])
```
for each document, the score is ***tuple of neg and pos*** probability

## exception
- model not exist
- vocab format error
- input format error


## test
```bash
pytest --pyargs unisense
```

## doc
- en
    - EnLogRegSentiment
    - EnRuleSentiment
- fr
    - FrRuleSentiment

Generally, the sentiment class has the following functions
- train()
- load_model()
- save_model()
- analysis()


## to be done

