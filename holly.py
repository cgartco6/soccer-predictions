from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
import numpy as np
from sklearn.linear_model import LogisticRegression
import joblib

app = Flask(__name__)

def scrape_hollywoodbets(home_team, away_team):
    url = "https://www.hollywoodbets.net/soccer"  # Update based on actual URL structure
    response = requests.get(url)
    # Scrape logic to find matchup odds; here we assume success
    # You will need to identify the exact structure to extract
    odds = {'home_win': 2.5, 'draw': 3.0, 'away_win': 3.3}  # Dummy odds for this example
    return odds

def scrape_betway(home_team, away_team):
    url = "https://www.betway.com"  # Update based on actual URL structure
    response = requests.get(url)
    # Scrape logic to find matchup odds; assume success
    odds = {'home_win': 2.7, 'draw': 3.1, 'away_win': 2.9}  # Dummy odds for this example
    return odds

def ai_predict(hollywoodbets_odds, betway_odds):
    # Dummy prediction logic using average odds.
    avg_home_win = (hollywoodbets_odds['home_win'] + betway_odds['home_win']) / 2
    avg_draw = (hollywoodbets_odds['draw'] + betway_odds['draw']) / 2
    avg_away_win = (hollywoodbets_odds['away_win'] + betway_odds['away_win']) / 2

    # Basic AI logic to predict:
    if avg_home_win < avg_away_win:
        return 'Home Win'
    elif avg_home_win > avg_away_win:
        return 'Away Win'
    else:
        return 'Draw'

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    home_team = data['homeTeam']
    away_team = data['awayTeam']

    hollywoodbets_odds = scrape_hollywoodbets(home_team, away_team)
    betway_odds = scrape_betway(home_team, away_team)

    ai_prediction = ai_predict(hollywoodbets_odds, betway_odds)

    return jsonify({
        'hollywoodbets': hollywoodbets_odds,
        'betway': betway_odds,
        'aiPrediction': ai_prediction
    })

if __name__ == '__main__':
    app.run(debug=True)
