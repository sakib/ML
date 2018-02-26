### Feature extraction and save the train and test data###
### Diana S. Kim 2018.Jan.31##############################

from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

categories = [
        'alt.atheism',
        'talk.religion.misc',
        'comp.graphics',
        'sci.space',
    ]


train=fetch_20newsgroups(subset='train', categories=categories,shuffle=True)
test=fetch_20newsgroups(subset='test', categories=categories,shuffle=True)

train_data=dict()
test_data=dict()

train_data['target'] = train.target
test_data['target'] = test.target

vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,stop_words='english')
train_data['data'] = vectorizer.fit_transform(train.data)
test_data['data'] = vectorizer.transform(test.data)

with open('train.pkl','wb') as f0:
    pickle.dump(train_data,f0)
f0.close()
with open('test.pkl','wb') as f0:
    pickle.dump(test_data,f0)
f0.close()


