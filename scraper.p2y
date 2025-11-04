import requests
from bs4 import BeautifulSoup

def scrape_hollywoodbets():
    url = 'https://www.hollywoodbets.net/'
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        matches = soup.find_all('div', class_='match-item')  # Adjust the selector based on the actual HTML structure
        
        for match in matches:
            teamA = match.find('span', class_='teamA').text
            teamB = match.find('span', class_='teamB').text
            oddsA = match.find('span', class_='oddsA').text
            oddsB = match.find('span', class_='oddsB').text
            print(f'{teamA} vs {teamB} | Odds: {oddsA}, {oddsB}')
    else:
        print("Failed to retrieve data.")

scrape_hollywoodbets()
