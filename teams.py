from bs4 import BeautifulSoup
import requests


def get_teams_data():
    # Get BeautifulSoup data
    response_teams_standings = requests.get("https://www.formula1.com/en/results.html/2022/team.html")
    soup = BeautifulSoup(response_teams_standings.text, "html.parser")
    table = soup.find_all("tr")
    # Get team standings data and clean it
    teams_standings = []
    for row in table:
        row = row.text
        teams_standings.append(row.strip().split("\n"))
    # Get only position, team and points
    teams_standings_data = [['Pos', 'Team', 'PTS']]
    for team in range(1, 11):
        teams_standings_data.append([teams_standings[team][0], teams_standings[team][2], teams_standings[team][4]])
    return teams_standings_data
