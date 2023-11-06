# # from sentiment import perform_sentiment_analysis
# from wordcount import get_most_common_words

# def main():
#     # perform_sentiment_analysis()
#     get_most_common_words()

# if __name__ == "__main__":
#     main()

import nltk
from nltk.corpus import stopwords
from collections import Counter
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from mediawiki import MediaWiki
from newspaper import Article

# Initialize NLTK and download VADER lexicon
nltk.download("vader_lexicon")

# Initialize Sentiment Intensity Analyzer
analyzer = SentimentIntensityAnalyzer()

# Function to perform sentiment analysis
def perform_sentiment_analysis():
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
        
# Download NLTK stopwords
nltk.download("stopwords")

# Initialize NLTK stopwords
stop_words = set(stopwords.words("english"))

# Function to preprocess text
def preprocess_text(text):
    # Tokenization and lowercasing
    tokens = nltk.word_tokenize(text.lower())
    # Remove stopwords and non-alphanumeric tokens
    filtered_tokens = [
        word for word in tokens if word.isalnum() and word not in stop_words
    ]
    return filtered_tokens

# Function to get most common words in an article
def get_most_common_words(article_content):
    tokens = preprocess_text(article_content)
    word_counter = Counter(tokens)
    most_common_words = word_counter.most_common(10)  # Get the top 10 common words
    return most_common_words

# Function to run word count analysis
def perform_word_count_analysis():
    # Fetch content from Wikipedia
    wikipedia = MediaWiki()
    war = wikipedia.page("2023 Israel–Hamas war")
    war_title = war.title
    # Only consider content from the main article, ignore references
    war_content = war.section("Background") + war.section(
        "Events"
    )  # Adjust the section as needed

    # Fetch content from news articles
    news_sources = [
        "https://www.theguardian.com/world/2023/oct/18/why-israel-palestine-conflict-history",
        "https://www.washingtonpost.com/world/2023/10/17/israel-hamas-war-reason-explained-gaza/",
        "https://www.reuters.com/world/middle-east/israel-palestinian-dispute-hinges-statehood-land-jerusalem-refugees-2023-10-10/",
        "https://www.aljazeera.com/news/2023/10/9/whats-the-israel-palestine-conflict-about-a-simple-guide",
        "https://www.vox.com/2023/10/7/23907912/israel-palestine-conflict-history-explained-gaza-hamas",
    ]

    # Analyze most common words for Wikipedia
    print(f"Most Common Words in Wikipedia Article '{war_title}':")
    common_words_wikipedia = get_most_common_words(war_content)
    for word, count in common_words_wikipedia:
        print(f"{word}: {count}")

    # Analyze most common words for news articles
    for i, url in enumerate(news_sources):
        article = Article(url)
        article.download()
        article.parse()
        article_title = article.title

        print(f"\nMost Common Words in News Article {i + 1} - '{article_title}':")
        common_words_article = get_most_common_words(article.text)
        for word, count in common_words_article:
            print(f"{word}: {count}")

def main():
    perform_sentiment_analysis()
    perform_word_count_analysis()

if __name__ == "__main__":
    main()
