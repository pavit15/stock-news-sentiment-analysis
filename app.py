from flask import Flask, render_template, request, jsonify
import requests
import os
from textblob import TextBlob
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

apiKey = os.getenv('API_KEY')

if not apiKey:
    raise ValueError("API_KEY not found in .env file")

def fetchStockNews(stockSymbols):
    articles = []
    for stockSymbol in stockSymbols:
        url = f'https://newsapi.org/v2/everything?q={stockSymbol}&apiKey={apiKey}&language=en'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if 'articles' in data:
                for article in data['articles']:
                    article['stockSymbol'] = stockSymbol
                    articles.append(article)
    return articles

def getSentimentLabelAndColor(score):
    if score >= 0.75:
        return 'Surely Positive', '#c8e6c9', 'Buy or Hold'
    elif score >= 0.5:
        return 'Positive', '#a5d6a7', 'Buy'
    elif score >= 0.25:
        return 'Slightly Positive', '#bbdefb', 'Hold or Buy'
    elif score >= 0:
        return 'Less Positive', '#e3f2fd', 'Hold or Sell'
    elif score >= -0.25:
        return 'Neutral', '#f0f0f0', 'Hold or Stay Neutral'
    elif score >= -0.5:
        return 'Slightly Negative', '#ffe082', 'Sell or Avoid'
    elif score >= -0.75:
        return 'Negative', '#ffccbc', 'Sell'
    else:
        return 'Surely Negative', '#ef9a9a', 'Sell Immediately'

@app.route('/')
def index():
    stockSymbols = ['AAPL', 'TSLA', 'AMZN', 'GOOGL', 'MSFT']
    return render_template('index.html', stockSymbols=stockSymbols)

@app.route('/filter-news', methods=['POST'])
def filterNews():
    data = request.json
    selectedStocks = data.get('stocks', [])
    sentimentFilter = data.get('sentiment', 'Any')
    traderActionFilter = data.get('trader_action', 'Any')

    stockList = selectedStocks if selectedStocks else ['AAPL', 'TSLA', 'AMZN', 'GOOGL', 'MSFT']
    articles = fetchStockNews(stockList)

    processedArticles = []
    for article in articles:
        description = article.get('description', '')
        if not description:
            continue

        blob = TextBlob(description)
        sentimentScore = blob.sentiment.polarity
        sentimentLabel, backgroundColor, traderRelevance = getSentimentLabelAndColor(sentimentScore)

        processedArticle = {
            "title": article.get('title', 'No Title'),
            "description": description,
            "url": article.get('url', '#'),
            "stockSymbol": article['stockSymbol'],
            "sentimentScore": sentimentScore,
            "sentimentLabel": sentimentLabel,
            "backgroundColor": backgroundColor,
            "traderRelevance": traderRelevance,
            "publishedAt": article.get('publishedAt', 'Unknown')
        }
        processedArticles.append(processedArticle)

    filteredArticles = []
    for article in processedArticles:
        if sentimentFilter != 'Any' and article['sentimentLabel'] != sentimentFilter:
            continue
        if traderActionFilter != 'Any' and article['traderRelevance'] != traderActionFilter:
            continue
        filteredArticles.append(article)

    return jsonify(filteredArticles)

if __name__ == '__main__':
    app.run(debug=True)
