from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
import pickle
import numpy as np

# Ask input from user (Explain program + rules)
lyrics = input('''Welcome to Lyrics Classifyer.
                  If you give me some Lyrics, I can guess if 50 Cents said them, or if Britney Spears said them.
                  the more lyrics you give me, the better I am at predicting ;)
                  
                  I am a kid friendly interface - if you use any bad words, you have to censor them.
                  here are some examples to help you: f*ck, b**ch.
                  
                  Go ahead, and try.
                  Enter text here: ''')


# Load Fitted Vectorizer + apply transformation to input
with open("vector_1.pickle", "rb") as meep:
    loaded_vector = pickle.load(meep)
lyrics_v = loaded_vector.transform([lyrics])

# Load fitted model + make prediction
with open("model_1.pickle", "rb") as meep2:
    loaded_model = pickle.load(meep2)

# set threshhold (see notebook) and make prediction
THRESHOLD = 0.6
artist_prediction = np.where(loaded_model.predict_proba(lyrics_v)[:,1] > THRESHOLD, 1, 0)
prediction_probabilaty = loaded_model.predict_proba(lyrics_v)


# transform prediction to text + return to user
if artist_prediction==0:
    print('''
    
    This Text belongs to - 50 Cent, with prediction probabilaty of: ''', round(prediction_probabilaty[0][0], 3))
if artist_prediction==1:
    print('''
    
    This Text belongs - Britney Spears, with prediction probabilaty of: ''', round(prediction_probabilaty[0][1], 3))
