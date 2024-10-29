# sentiment-analysis-google-playstore

# Play Store Review Sentiment Analysis

A Python-based sentiment analysis tool for Google Play Store reviews. This project helps developers and product managers analyze user feedback by automatically extracting reviews and determining their sentiment (positive, negative, or neutral).

![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Dependencies](https://img.shields.io/badge/dependencies-2-orange.svg)

## 🚀 Features

- Automated review extraction from Google Play Store
- Sentiment analysis using dictionary-based approach
- Support for multiple languages (configurable)
- Detailed sentiment distribution analysis
- JSON export of analyzed reviews
- Comprehensive word and phrase dictionaries
- Rating-based sentiment adjustment
- Sample review display

## 📋 Requirements

- Python 3.7 or higher
- Required Python packages:
  ```
  google-play-scraper
  ```

## 💻 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/bhumyamka/sentiment-analysis-google-playstore.git
   cd sentiment-analysis-google-playstore
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## 🎮 Usage

1. Basic usage:
   ```python
   from sentiment_analysis import extract_app_reviews

   # Replace with your app's ID from Google Play Store
   app_id = 'com.example.app'
   reviews = extract_app_reviews(app_id)
   ```

2. Run the complete analysis:
   ```bash
   python sentiment_analysis.py
   ```

3. Customize the analysis:
   ```python
   # Specify language and country
   reviews = extract_app_reviews(
       app_id='com.example.app',
       lang='en',  # Language code
       country='us',  # Country code
       count=100  # Number of reviews to analyze
   )
   ```

## 📊 Output Example

```json
{
    "user": "John Doe",
    "rating": 5,
    "date": "2024-01-01T12:00:00",
    "content": "Great app, very useful and easy to use!",
    "sentiment": "positive"
}
```

## 📈 Sentiment Distribution Example

```
Sentiment Distribution:
Positive: 45 (45.00%)
Neutral: 30 (30.00%)
Negative: 25 (25.00%)
```

## 🛠️ Customization

### Modifying Word Dictionaries

You can customize the sentiment dictionaries by modifying the word lists in the `SentimentAnalyzer` class:

```python
self.positive_words = set([
    'good', 'great', 'awesome',
    # Add your positive words here
])

self.negative_words = set([
    'bad', 'poor', 'terrible',
    # Add your negative words here
])
```

### Adjusting Sentiment Analysis

You can modify the sentiment analysis logic in the `analyze_sentiment` method:

```python
def analyze_sentiment(self, text, rating):
    # Customize your sentiment analysis logic here
    pass
```

## 📝 Code Structure

```
playstore-sentiment-analysis/
│
├── sentiment_analysis.py    # Main script
├── requirements.txt        # Project dependencies
├── README.md              # Project documentation
└── examples/              # Example outputs
```

## 🎯 Use Cases

- Monitor user satisfaction trends
- Identify common issues in your app
- Track sentiment changes after updates
- Generate reports for stakeholders
- Analyze competitor app reviews
- Prioritize feature development based on user feedback

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Limitations

- Dictionary-based approach may not catch complex sentiments
- Cannot understand sarcasm or context-dependent meanings
- Limited by the quality of the word dictionaries
- May require adjustment for specific domains or languages

## 🔄 Future Improvements

- [ ] Add machine learning-based sentiment analysis
- [ ] Implement multi-language support
- [ ] Add aspect-based sentiment analysis
- [ ] Create a web interface
- [ ] Add automated reporting
- [ ] Implement trend analysis
- [ ] Add support for batch processing

## 📞 Support

If you encounter any issues or have questions, please:

1. Check the [issues page](https://github.com/bhumyamka/sentiment-analysis-google-playstore/issues)
2. Create a new issue if needed
3. Contact the maintainers

## 👥 Authors

- BYS - [bhumyamka](https://github.com/bhumyamka)

## 🙏 Acknowledgments

- Google Play Scraper developers
- Open source community
- All contributors

---

Remember to ⭐ this repo if you find it helpful!
