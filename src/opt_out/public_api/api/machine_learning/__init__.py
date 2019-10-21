import os.path
import warnings
from pathlib import Path
from typing import List

warnings.filterwarnings('ignore')
import urllib.request
from sklearn.externals import joblib

here = Path(__file__).parent


class TextSentimentPrediction:
    model = None
    tfidf = None

    def __init__(self):
        if TextSentimentPrediction.tfidf is None:
            tfidf_filename = here / 'opt_out_tfidf.joblib'
            if not os.path.isfile(tfidf_filename):
                url = 'https://sculpt-public-models.s3-us-west-2.amazonaws.com/misogyny_vectorizer.joblib'
                urllib.request.urlretrieve(url, tfidf_filename)
            TextSentimentPrediction.tfidf = joblib.load(tfidf_filename)

        if TextSentimentPrediction.model is None:
            prediction_model_filename = here / 'opt_out_logreg.joblib'
            if not os.path.isfile(prediction_model_filename):
                url = 'https://sculpt-public-models.s3-us-west-2.amazonaws.com/misogyny_logreg.joblib'
                urllib.request.urlretrieve(url, prediction_model_filename)
            TextSentimentPrediction.model = joblib.load(prediction_model_filename)

    def pre_process_text(self, text: str):
        return TextSentimentPrediction.tfidf.transform([text])

    def __call__(self, texts: List[str], threshold=0.95) -> List[bool]:
        preprocessed_texts = [self.pre_process_text(text) for text in texts]

        predictions = [TextSentimentPrediction.model.predict_proba(preprocessed_text)[0][0] for preprocessed_text in
                       preprocessed_texts]
        return [float(prediction) > threshold for prediction in predictions]
