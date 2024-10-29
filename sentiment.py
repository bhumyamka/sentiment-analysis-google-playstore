import json
from google_play_scraper import Sort, reviews
import re

class SentimentAnalyzer:
    def __init__(self):
        # Initialize positive and negative word dictionaries
        self.positive_words = set([
            'good', 'great', 'awesome', 'excellent', 'happy', 'satisfied', 
            'recommended', 'useful', 'helpful', 'fast', 'easy', 'effective', 
            'efficient', 'reliable', 'impressive', 'responsive', 'innovative', 
            'practical', 'perfect', 'love', 'best', 'amazing', 'wonderful'
        ])

        self.negative_words = set([
            'bad', 'poor', 'terrible', 'disappointing', 'slow', 'expensive', 
            'difficult', 'heavy', 'crash', 'error', 'bug', 'laggy', 'hard', 
            'complicated', 'long', 'fail', 'confusing', 'problematic', 'worst',
            'horrible', 'unusable', 'waste', 'awful', 'useless'
        ])

        self.positive_phrases = [
            'very helpful', 'easy to use', 'good features', 'great service', 
            'quick response', 'fast process', 'user-friendly', 'satisfying results', 
            'easy to understand', 'highly recommended', 'great performance', 
            'works perfectly', 'excellent support', 'stable and reliable', 
            'quick access', 'best app', 'love this app', 'perfect solution',
            'great experience', 'well designed', 'very useful', 'working great'
        ]

        self.negative_phrases = [
            'frequent errors', 'login issues', 'cannot access', 'many bugs', 
            'keeps crashing', 'slow response', 'long process', 'not satisfied', 
            'disappointing experience', 'limited features', 'poor service', 
            'too expensive', 'app is slow', 'difficult to access', 
            'confusing interface', 'features not working', 'login failed', 
            'not responsive', 'very unstable', 'memory intensive', 
            'update issues', 'long loading times', 'waste of time',
            'not working properly', 'keeps freezing'
        ]

    def preprocess_text(self, text):
        """Clean and prepare text for analysis"""
        # Convert to lowercase
        text = text.lower()
        # Remove special characters
        text = re.sub(r'[^a-z0-9\s]', ' ', text)
        # Remove extra whitespace
        return ' '.join(text.split())

    def analyze_sentiment(self, text, rating):
        """
        Analyze sentiment of given text and rating
        
        Args:
            text (str): Review text
            rating (int): Star rating (1-5)
            
        Returns:
            str: Sentiment category ('positive', 'negative', or 'neutral')
        """
        text = self.preprocess_text(text)
        words = text.split()
        
        # Calculate word-based scores
        positive_score = sum(1 for word in words if word in self.positive_words)
        negative_score = sum(1 for word in words if word in self.negative_words)
        
        # Calculate phrase-based scores (weighted higher)
        for phrase in self.positive_phrases:
            if phrase in text:
                positive_score += 2
        for phrase in self.negative_phrases:
            if phrase in text:
                negative_score += 2
        
        # Consider star rating in analysis
        if rating >= 4:
            positive_score += 1
        elif rating <= 2:
            negative_score += 1
        
        # Determine sentiment
        if positive_score > negative_score:
            return 'positive'
        elif negative_score > positive_score:
            return 'negative'
        return 'neutral'

def extract_app_reviews(app_id, lang='en', country='us', count=100):
    """
    Extract and analyze reviews from Google Play Store
    
    Args:
        app_id (str): Application ID from Google Play Store
        lang (str): Language of reviews (default: 'en')
        country (str): Country code (default: 'us')
        count (int): Number of reviews to extract (default: 100)
        
    Returns:
        list: Processed reviews with sentiment analysis
    """
    try:
        # Initialize sentiment analyzer
        analyzer = SentimentAnalyzer()
        
        # Fetch reviews from Play Store
        result, _ = reviews(
            app_id,
            lang=lang,
            country=country,
            sort=Sort.NEWEST,
            count=count
        )
        
        if not result:
            print(f"Warning: No reviews found for app ID {app_id}")
            return []
        
        # Process reviews and analyze sentiment
        processed_reviews = [
            {
                'user': review['userName'],
                'rating': review['score'],
                'date': review['at'].isoformat(),
                'content': review['content'],
                'sentiment': analyzer.analyze_sentiment(review['content'], review['score'])
            }
            for review in result
        ]
        
        return processed_reviews
        
    except Exception as e:
        print(f"Error extracting reviews: {str(e)}")
        return []

def analyze_sentiment_distribution(reviews):
    """
    Calculate sentiment distribution statistics
    
    Args:
        reviews (list): List of processed reviews
        
    Returns:
        dict: Sentiment distribution statistics
    """
    if not reviews:
        return None
        
    distribution = {
        'positive': sum(1 for r in reviews if r['sentiment'] == 'positive'),
        'neutral': sum(1 for r in reviews if r['sentiment'] == 'neutral'),
        'negative': sum(1 for r in reviews if r['sentiment'] == 'negative')
    }
    
    total = len(reviews)
    distribution_percentage = {
        sentiment: {
            'count': count,
            'percentage': (count / total) * 100
        }
        for sentiment, count in distribution.items()
    }
    
    return distribution_percentage

def main():
    """Main execution function"""
    # Replace with your app's ID
    app_id = 'com.example.app'
    
    # Extract reviews
    print("Extracting and analyzing reviews...")
    reviews = extract_app_reviews(app_id)
    
    if reviews:
        # Save to JSON file
        output_file = 'app_reviews_sentiment.json'
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(reviews, f, ensure_ascii=False, indent=2)
        print(f"\nExtracted and analyzed {len(reviews)} reviews. Results saved to {output_file}")
        
        # Analyze sentiment distribution
        distribution = analyze_sentiment_distribution(reviews)
        
        print("\nSentiment Distribution:")
        for sentiment, data in distribution.items():
            print(f"{sentiment.capitalize()}: {data['count']} ({data['percentage']:.2f}%)")
        
        # Display sample reviews
        print("\nSample Reviews Analysis:")
        for review in reviews[:5]:
            print(f"\nUser: {review['user']}")
            print(f"Rating: {review['rating']} stars")
            print(f"Content: {review['content']}")
            print(f"Sentiment: {review['sentiment']}")
            print("-" * 50)
    
if __name__ == "__main__":
    main()
