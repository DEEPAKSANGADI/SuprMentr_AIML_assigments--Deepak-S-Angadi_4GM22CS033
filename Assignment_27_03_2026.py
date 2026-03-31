from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
import nltk


nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')

def calculate_similarity(word1, word2):
    """Calculate semantic similarity between two words using WordNet"""
    synset1 = wordnet.synsets(word1)
    synset2 = wordnet.synsets(word2)
    
    if not synset1 or not synset2:
        return 0.0
    
    similarity = synset1[0].path_similarity(synset2[0])
    return similarity if similarity else 0.0


word_pairs = [
    ("car", "automobile"),
    ("happy", "joyful"),
    ("large", "big"),
    ("dog", "puppy"),
    ("beautiful", "gorgeous")
]

print("=" * 60)
print("SEMANTIC SIMILARITY ANALYSIS OF WORD PAIRS")
print("=" * 60)

for word1, word2 in word_pairs:
    similarity = calculate_similarity(word1, word2)
    print(f"\nPair: '{word1}' and '{word2}'")
    print(f"Similarity Score: {similarity:.2f}")
    print(f"Explanation: These words share similar meanings")
    print("-" * 60)