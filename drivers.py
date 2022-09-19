from bs4 import BeautifulSoup
import requests


def get_drivers_data():
    # Get BeautifulSoup data
    response_driver_standings = requests.get("https://www.formula1.com/en/results.html/2022/drivers.html")
    soup = BeautifulSoup(response_driver_standings.text, "html.parser")
    table = soup.find_all("tr")
    # Get drivers standings data and clean it
    drivers_standings = []
    for row in table:
        row = row.text
        drivers_standings.append(row.strip().split("\n"))
    # Get only position, name, team and points
    driver_standings_data = [['Pos', 'Driver', 'Team', 'PTS']]
    for driver in range(1, 23):
        driver_standings_data.append([drivers_standings[driver][0], drivers_standings[driver][4],
                                      drivers_standings[driver][10], drivers_standings[driver][12]])
    return driver_standings_data
