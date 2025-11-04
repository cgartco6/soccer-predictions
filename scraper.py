from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def scrape_hollywoodbets(home_team, away_team):
    # Simulating scraping logic - replace this part with actual scraping logic
    url = "https://www.hollywoodbets.net/soccer"  # Placeholder URL
    response = requests.get(url)
    odds = {'home_win': 2.5, 'draw': 3.0, 'away_win': 3.3}  # Dummy odds
    return odds

def scrape_betway(home_team, away_team):
    # Simulating scraping logic - replace this part with actual scraping logic
    url = "https://www.betway.com"  # Placeholder URL
    response = requests.get(url)
    odds = {'home_win': 2.7, 'draw': 3.1, 'away_win': 2.9}  # Dummy odds
    return odds

def ai_predict(hollywoodbets_odds, betway_odds):
    # Basic AI logic based on average odds
    avg_home_win = (hollywoodbets_odds['home_win'] + betway_odds['home_win']) / 2
    avg_draw = (hollywoodbets_odds['draw'] + betway_odds['draw']) / 2
    avg_away_win = (hollywoodbets_odds['away_win'] + betway_odds['away_win']) / 2

    if avg_home_win < avg_away_win:
        return 'Home Win', avg_home_win, avg_draw, avg_away_win
    elif avg_home_win > avg_away_win:
        return 'Away Win', avg_home_win, avg_draw, avg_away_win
    else:
        return 'Draw', avg_home_win, avg_draw, avg_away_win

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    home_team = data['homeTeam'].strip()
    away_team = data['awayTeam'].strip()

    hologbets_odds = scrape_hollywoodbets(home_team, away_team)
    betway_odds = scrape_betway(home_team, away_team)

    ai_result, avg_home_win, avg_draw, avg_away_win = ai_predict(hologbets_odds, betway_odds)

    return jsonify({
        'hollywoodbets': hologbets_odds,
        'betway': betway_odds,
        'aiPrediction': ai_result,
        'avgOdds': {
            'home_win': avg_home_win,
            'draw': avg_draw,
            'away_win': avg_away_win
        }
    })

if __name__ == '__main__':
    app.run(debug=True)
