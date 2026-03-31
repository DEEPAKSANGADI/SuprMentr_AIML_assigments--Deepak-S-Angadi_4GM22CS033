import re
from collections import Counter
from typing import List, Dict, Tuple

class SpamDetectionSystem:
    """
    A spam detection system with feature extraction and classification.
    """
    
    def __init__(self):
        # Common spam indicators
        self.spam_keywords = {
            'click_here', 'buy_now', 'limited_offer', 'free_money',
            'winner', 'congratulations', 'claim_prize', 'urgent'
        }
        self.suspicious_domains = {'bit.ly', 'tinyurl.com'}
        self.threshold = 0.5
    
    
    def extract_features(self, message: str) -> Dict[str, float]:
        """Extract relevant features from a message."""
        features = {}
        
       
        words = message.lower().split()
        spam_word_count = sum(1 for word in words if word in self.spam_keywords)
        features['spam_keyword_density'] = spam_word_count / len(words) if words else 0
        
       
        urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+])+', message)
        features['url_count'] = len(urls)
        
        
        suspicious = sum(1 for url in urls if any(d in url for d in self.suspicious_domains))
        features['suspicious_domain_ratio'] = suspicious / len(urls) if urls else 0
        
       
        caps_count = sum(1 for c in message if c.isupper())
        features['caps_ratio'] = caps_count / len(message) if message else 0
        
        
        special_chars = sum(1 for c in message if not c.isalnum() and c != ' ')
        features['special_char_density'] = special_chars / len(message) if message else 0
        
       
        features['exclamation_count'] = message.count('!')
        features['question_count'] = message.count('?')
        
        return features
    
   
    def get_required_data(self) -> Dict[str, List[str]]:
        """Specify data requirements for training."""
        return {
            'labeled_messages': [
                'spam_examples_with_labels',
                'ham_examples_with_labels'
            ],
            'metadata': [
                'sender_reputation_score',
                'sender_domain_age',
                'user_complaint_history',
                'email_headers'
            ],
            'external_data': [
                'known_spam_database',
                'phishing_URL_lists',
                'blacklisted_domains'
            ]
        }
    

    def classify(self, message: str) -> Tuple[str, float]:
        """
        Classify message as spam or ham.
        
        POSSIBLE MISTAKES/PITFALLS:
        1. False Positives: Legitimate emails marked as spam
           - Solution: Whitelist trusted senders, adjust thresholds
        
        2. False Negatives: Spam gets through
           - Solution: Use ensemble methods, update spam patterns
        
        3. Language Bias: Works better in English
           - Solution: Train multilingual models
        
        4. Adversarial Spam: Spammers evolve techniques
           - Solution: Continuous model retraining
        
        5. Context Ignorance: Doesn't understand sender relationship
           - Solution: Include personalization features
        
        6. Class Imbalance: More ham than spam
           - Solution: Use SMOTE, adjust class weights
        """
        features = self.extract_features(message)
        
       
        spam_score = (
            features['spam_keyword_density'] * 0.2 +
            (features['url_count'] / 5) * 0.2 +
            features['suspicious_domain_ratio'] * 0.2 +
            features['caps_ratio'] * 0.15 +
            features['special_char_density'] * 0.15 +
            (features['exclamation_count'] / 3) * 0.1
        )
        
        label = 'SPAM' if spam_score >= self.threshold else 'HAM'
        return label, spam_score



if __name__ == "__main__":
    detector = SpamDetectionSystem()
    
    test_messages = [
        "Click here NOW!!! You won FREE MONEY!!!",
        "Hello, how are you doing today?",
        "URGENT: Limited time offer - bit.ly/xyz123"
    ]
    
    for msg in test_messages:
        label, score = detector.classify(msg)
        print(f"Message: {msg[:50]}...")
        print(f"Classification: {label} (Score: {score:.2f})\n")