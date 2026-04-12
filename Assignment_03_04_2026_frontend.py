import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
import pickle

# 1. Load your dataset (assuming you have a CSV with 'text' and 'label' columns)
df = pd.read_csv('news_dataset.csv')
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2)

# 2. Create a Machine Learning Pipeline
# TfidfVectorizer looks at word frequencies, PassiveAggressive is great for text classification
model = make_pipeline(TfidfVectorizer(stop_words='english', max_df=0.7), 
                      PassiveAggressiveClassifier(max_iter=50))

# 3. Train the model
model.fit(X_train, y_train)

# 4. Save the trained model to use in your chatbot later
with open('fake_news_model.pkl', 'wb') as file:
    pickle.dump(model, file)
    
print("Model trained and saved successfully!")