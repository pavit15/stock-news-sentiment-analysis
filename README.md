# Stock News Sentiment Analysis

A lightweight Flask application that integrates **news data**, **natural language processing**, and **sentiment analysis** to assist in stock market interpretation. This project applies data science techniques to analyze stock related news sentiment and generate trader friendly insights.

---

## Project Objective

To process stock market news using **natural language understanding (NLP)** and assess their potential market impact by:

- Extracting real time news from NewsAPI
- Performing **sentiment polarity scoring** using `TextBlob`
- Mapping scores to **interpretable trader actions** (e.g., Buy, Sell, Hold)
- Visualizing sentiment through color coded indicators

---

## Dashboard interface

![All Stocks](https://github.com/pavit15/stock-news-sentiment-analysis/blob/main/images/all%20stocks.jpg)  
  **Displays the overall sentiment trends for all stocks analyzed.**

![MSFT - Any Sentiment, Any Action](https://github.com/pavit15/stock-news-sentiment-analysis/blob/main/images/msft%20any%20sent%20any%20action.jpg)  
  **Sentiment and trader action recommendations for Microsoft (MSFT) under various sentiment conditions.**

 ![Tesla - Positive Sentiment](https://github.com/pavit15/stock-news-sentiment-analysis/blob/main/images/tesla%20positive.jpg)  
  **Positive sentiment analysis and recommended trading action for Tesla (TSLA).**


## Data Science Workflow Applied

### 1. **Data Acquisition**
- Uses **NewsAPI** to fetch articles for major stock tickers like `AAPL`, `TSLA`, `GOOGL`, `MSFT`, etc.
- Filters articles using user-selected stock symbols via AJAX.

### 2. **Text Preprocessing**
- Extracts news article descriptions.
- Applies basic NLP filtering (e.g. removing empty descriptions).

### 3. **Sentiment Analysis**
- Uses **TextBlob**, a rule based NLP tool, to assign **sentiment polarity scores** ranging from `-1.0` to `+1.0`.

### 4. **Sentiment Interpretation**
- Polarity score is mapped to:
  - A **sentiment label** (e.g., *Slightly Positive*)
  - A **trading relevance suggestion** (e.g., *Buy*, *Sell*)
  - A **visual tag** (background color for easier UX)

### 5. **Data Filtering & Presentation**
- Users can filter the news articles by:
  - **Sentiment class** (Neutral, Positive, Negative, etc.)
  - **Trader relevance** (Buy, Hold, Sell)
- Frontend dynamically reflects these selections using Flask routes + JSON + AJAX.

---

## Techniques Used

| Technique                 | Library     | Purpose                               |
|--------------------------|-------------|----------------------------------------|
| NLP Preprocessing         | `TextBlob`  | Extract polarity sentiment from text   |
| Sentiment Categorization  | Rule-based  | Convert numeric score into label       |
| Data Mapping              | Custom Logic | Assign trader actions via thresholds   |
| Real-Time Data Streaming  | `NewsAPI`   | Fetch external data for DS processing  |

---

## 🧰 Tech Stack

- **Backend:** Python, Flask
- **NLP / DS:** TextBlob
- **API:** NewsAPI
- **Frontend:** HTML, CSS, JS (AJAX)
- **Deployment Ready:** Environment variables with `python-dotenv`

---

## How To Run

1. Clone the repo:
```bash
git clone https://github.com/pavit15/stock-news-sentiment-analysis.git
cd stock-news-sentiment-analysis
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Add your .env file:
```bash
NEWSAPI_KEY=your_actual_api_key
```

4. Run the app:
```bash
python app.py
```

## Future Enhancements 

- **Advanced Sentiment Analysis:**
  - Incorporate more sophisticated NLP techniques, like `spaCy` or transformer models (e.g., BERT) for better sentiment accuracy.
  
- **Trading Strategy Backtesting:**
  - Develop a mechanism to backtest trading strategies based on sentiment analysis outcomes. 
  - Simulate trading decisions (Buy, Hold, Sell) based on historical data and sentiment trends.

- **Clustering & News Trend Analysis:**
  - Use clustering techniques (e.g., K-means) to group similar news articles and detect trends in market sentiment over time.
  - Build timeline-based analysis for visualizing sentiment changes over multiple days/weeks.

- **Additional Data Sources:**
  - Integrate multiple news sources for a more comprehensive sentiment analysis and broader coverage of stock market news.


