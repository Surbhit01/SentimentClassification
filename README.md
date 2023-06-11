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

![image](https://github.com/Surbhit01/SentimentClassification/assets/24591039/5ff24459-80b9-4767-b8da-b521d8bcd8b0)
[Image above] Word count distribution in positive and negative tweets


![image](https://github.com/Surbhit01/SentimentClassification/assets/24591039/a2b85654-f5be-4452-b12c-63a7263a64f7)
[Image above] Negative polarity word cloud

![image](https://github.com/Surbhit01/SentimentClassification/assets/24591039/e0b7f4aa-ee5e-440c-a2a6-798f95bed0bb)
[Image above] positive polarity word cloud


![Positive](https://github.com/Surbhit01/SentimentClassification/assets/24591039/f0533d25-4137-41c1-a5a3-feafa3c1ca58)
[Image above] Positive prediction sample

![Negative](https://github.com/Surbhit01/SentimentClassification/assets/24591039/240491c0-c040-4be4-badc-c28d27029e59)
[Image above] Negative prediction sample
