from bs4 import BeautifulSoup
import requests

TEAMS_STANDINGS_URL = "https://www.formula1.com/en/results.html/2022/team.html"


def get_teams_data():
    """Returns list with teams standings data"""
    # Get BeautifulSoup data
    response_teams_standings = requests.get(TEAMS_STANDINGS_URL)
    soup = BeautifulSoup(response_teams_standings.text, "html.parser")
    table = soup.find_all("tr")
    # Get team standings data and clean it
    teams_standings = []
    number_of_rows = 0
    for row in table:
        number_of_rows += 1
        row = row.text
        teams_standings.append(row.strip().split("\n"))
    # Get only position, team and points
    teams_standings_data = [['Pos', 'Team', 'PTS']]
    for team in range(1, number_of_rows):
        teams_standings_data.append([teams_standings[team][0], teams_standings[team][2], teams_standings[team][4]])
    return teams_standings_data
