import string
from nltk.corpus import stopwords
import nltk

nltk.download('stopwords')

def preprocess_text(text):
    """
    Remove punctuation, convert to lowercase, and remove stopwords.
    
    Args:
        text (str): Input text to preprocess
        
    Returns:
        str: Preprocessed text
    """
    text = text.lower()
    
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    stop_words = set(stopwords.words('english'))
    
    words = text.split()
    filtered_words = [word for word in words if word not in stop_words]
    
    return ' '.join(filtered_words)


# Test the function
if __name__ == "__main__":
    test_texts = [
        "Hello, World! This is a test.",
        "Python is an amazing programming language!!!",
        "The quick brown fox jumps over the lazy dog."
    ]
    
    for text in test_texts:
        print(f"Original: {text}")
        print(f"Processed: {preprocess_text(text)}")
        print()