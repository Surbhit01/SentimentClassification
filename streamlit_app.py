##Streamlit page app
import streamlit as st
import sklearn
import pickle


PREDICTOR_MODEL_PATH = "NaiveBayes.pkl"
TFIDF_PATH = "tfidf.pkl"

predictor = pickle.load(open(PREDICTOR_MODEL_PATH,'rb'))
tfidf = pickle.load(open(TFIDF_PATH,'rb'))

print('Predictor model loaded')

st.markdown("<h1 style='text-align: center; color: black;'>SENTIMENT CLASSIFICATION</h1>", unsafe_allow_html=True)

st.subheader("This webapp takes a phrase as input and predicts the tone of the sentence (positive or negative) and its probablity.")

st.text("")
input_text = st.text_input("Enter your phrase below for analysing the sentiment", value="")

st.text("")
st.text("")

if st.button("Predict Sentiment"):
    try:
        input_text = [input_text]
        print(input_text)
        ip = tfidf.transform(input_text)
        pred_val = predictor.predict(ip)
        print(pred_val)
        pred = ""
        if pred_val > 0.5:
            pred = "Positive"
        else:
            pred_val = 1 - pred_val
            pred = "Negative"
            
        print(pred)
        st.text("")
        st.text("")
        st.subheader("Predicted Sentiment: " + pred)
    except Exception as e:
        print(e)