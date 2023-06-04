# Sentiment Classification
Text sentiment classifier to detect if the input phrase is positive or negative sentiment

## Implementation
In this project I have worked on predicting the sentiment of the input sentence using Logistic Regression.

Total documents - 200000

## Approach
The input tweets is pre processed. In the preprocessing phase:
* " 's " is replaced by "is" (Eg. It's -> It is)
* " # " is removed (Eg. #iPhone -> iPhone)
* " @ " is removed and alphabets are retained (Eg @user -> user)
* Any other non alphabet characters are removed
* http links are removed 
* Text is converted to lower case
* Contraction sentences are fixed (Eg. I've -> I have ; I'd -> I had)
* Words are lemmatized 

Used Logistic Regression, Naive Bayes, Random Forest and Linear SVM for modelling.<br>
Created a streamlit webapp using Naive Bayes model for prediction.<br><br>
![image](https://github.com/Surbhit01/SentimentClassification/assets/24591039/4630229b-2662-40cd-ae89-bedc5df33497)
[Image above] Word count distribution in negative tweets

![image](https://github.com/Surbhit01/SentimentClassification/assets/24591039/b4070d30-dcb9-48f8-a3a8-fffed9cfb039)
[Image above] Word cloud distribution in positive tweets

![image](https://github.com/Surbhit01/SentimentClassification/assets/24591039/2a51264c-78c5-409b-8f37-34d124e1171d)
[Image above] Negative polarity word cloud



![Positive](https://github.com/Surbhit01/SentimentClassification/assets/24591039/9b89f42e-ae4f-4b70-9b15-db170808d537)
[Image above] Positive prediction sample

![Negative](https://github.com/Surbhit01/SentimentClassification/assets/24591039/68346cff-d762-4216-a04d-2976de05670c)
[Image above] Negative prediction sample
