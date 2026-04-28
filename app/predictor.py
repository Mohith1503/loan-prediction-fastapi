import pandas as pd
from app.model import model

def make_prediction(data):
    input_df=pd.DataFrame([data.model_dump()])
    result=model.predict(input_df)
    proba = model.predict_proba(input_df)
    return int(result[0]), proba[0][1]