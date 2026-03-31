from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd


documents = [
    "Machine learning is a subset of artificial intelligence",
    "Deep learning uses neural networks for data processing",
    "Natural language processing helps computers understand text",
    "Artificial intelligence and machine learning are transforming technology",
    "Neural networks and deep learning models are powerful tools"
]


vectorizer = TfidfVectorizer(max_features=10, stop_words='english')

tfidf_matrix = vectorizer.fit_transform(documents)


feature_names = vectorizer.get_feature_names_out()

# Extract top keywords for each document
print("=" * 70)
print("TF-IDF ANALYSIS - TOP KEYWORDS PER DOCUMENT")
print("=" * 70)

for doc_idx, doc in enumerate(documents, 1):
    print(f"\nDocument {doc_idx}: {doc}")
    
   
    scores = tfidf_matrix[doc_idx-1].toarray()[0]
    

    top_indices = scores.argsort()[-5:][::-1]
    
    print("Top Keywords:")
    for rank, idx in enumerate(top_indices, 1):
        keyword = feature_names[idx]
        score = scores[idx]
        print(f"  {rank}. {keyword}: {score:.4f}")

print("\n" + "=" * 70)
print("EXPLANATION:")
print("=" * 70)
print("""
TF-IDF (Term Frequency-Inverse Document Frequency):
- TF: How often a word appears in a document
- IDF: How unique/rare the word is across all documents
- High TF-IDF = Important word specific to that document
- Low TF-IDF = Common word across many documents
""")