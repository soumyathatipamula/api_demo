from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)


NEWSAPI_KEY = "c730d0b384a8497d8a4084bc21532521"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search_news', methods=['POST'])
def search_news():
    query = request.form['query']
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": query,
        "apiKey": NEWSAPI_KEY,
        "pageSize": 10,  
        "language": "en",
        "sortBy": "relevancy"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        news = response.json()
        return jsonify(news)
    else:
        return jsonify({"error": f"Failed to fetch news: {response.status_code}"}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
