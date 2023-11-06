from newspaper import Article
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from mediawiki import MediaWiki

# Initialize NLTK and download VADER lexicon
nltk.download("vader_lexicon")

# Initialize Sentiment Intensity Analyzer
analyzer = SentimentIntensityAnalyzer()

# Fetch content from Wikipedia
wikipedia = MediaWiki()
war = wikipedia.page("2023 Israel–Hamas war")
war_title = war.title
war_content = war.section("Background") + war.section("Events")

# Sentiment analysis for the Wikipedia page
war_sentiment = analyzer.polarity_scores(war_content)

# Print sentiment analysis for the Wikipedia page
print(f"Wikipedia Page: {war_title}")
print(f"Sentiment: {war_sentiment['compound']:.2f} (Compound Score)")

# Define news sources and topic
news_sources = [
    "https://www.theguardian.com/world/2023/oct/18/why-israel-palestine-conflict-history",
    "https://www.washingtonpost.com/world/2023/10/17/israel-hamas-war-reason-explained-gaza/",
    "https://www.reuters.com/world/middle-east/israel-palestinian-dispute-hinges-statehood-land-jerusalem-refugees-2023-10-10/",
    "https://www.aljazeera.com/news/2023/10/9/whats-the-israel-palestine-conflict-about-a-simple-guide",
    "https://www.vox.com/2023/10/7/23907912/israel-palestine-conflict-history-explained-gaza-hamas",
]
topic = "Israel-Hamas Conflict Explainers"

# Scrape articles using Newspaper3k
articles = []
for url in news_sources:
    article = Article(url)
    article.download()
    article.parse()
    articles.append({"content": article.text, "date": article.publish_date})

# Perform sentiment analysis for news articles
sentiment_scores = []

for article in articles:
    text = article["content"]
    sentiment = analyzer.polarity_scores(text)
    sentiment_scores.append(sentiment)

# Analyze and interpret the sentiment results for news articles
for i, article in enumerate(articles):
    sentiment = sentiment_scores[i]
    compound_score = sentiment["compound"]

    if compound_score >= 0.05:
        sentiment_label = "Positive"
    elif compound_score <= -0.05:
        sentiment_label = "Negative"
    else:
        sentiment_label = "Neutral"

    print(f"Article {i + 1}:")
    print(f"Publication Date: {article['date']}")
    print(f"Sentiment: {sentiment_label} (Compound Score: {compound_score:.2f})")
    print()
