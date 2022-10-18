from bs4 import BeautifulSoup
import requests


RACE_RESULT_URL = 'https://www.formula1.com/en/results.html/2022/races/'
URL_VARIATIONS_FOR_EACH_RACE = ['1124/bahrain/race-result.html', '1125/saudi-arabia/race-result.html',
                                '1108/australia/race-result.html', '1109/italy/race-result.html',
                                '1110/miami/race-result.html', '1111/spain/race-result.html',
                                '1112/monaco/race-result.html', '1126/azerbaijan/race-result.html',
                                '1113/canada/race-result.html', '1114/great-britain/race-result.html',
                                '1115/austria/race-result.html', '1116/france/race-result.html',
                                '1117/hungary/race-result.html', '1118/belgium/race-result.html',
                                '1119/netherlands/race-result.html', '1120/italy/race-result.html',
                                '1133/singapore/race-result.html', '1134/japan/race-result.html',
                                '1135/united-states/race-result.html', '1136/mexico/race-result.html',
                                '1137/brazil/race-result.html', '1138/abu-dhabi/race-result.html']


def get_races_data():
    """Returns list with top 3 results for each race"""
    # Data for all races
    races_results_data = [['Grand Prix', 'Winner', 'Second', 'Third']]
    # Get data for each race
    for race in URL_VARIATIONS_FOR_EACH_RACE:
        response_race_result = requests.get(f"{RACE_RESULT_URL + race}")
        soup = BeautifulSoup(response_race_result.text, "html.parser")
        result_table = soup.find_all("tr")
        # Get finishing order of a race and clean data
        driver_order = []
        for row in result_table:
            row = row.text
            driver_order.append(row.strip("\n").split("\n"))
        # Make list of country and top 3 drivers
        country = soup.select("a.resultsarchive-filter-item-link.FilterTrigger.selected")[2].text.strip("\n")
        race_result = [country]
        try:
            for driver in range(1, 4):
                race_result.append(driver_order[driver][4])
        except IndexError:
            race_result.append("To be raced")
        # Append to list of data for all races
        races_results_data.append(race_result)
    return races_results_data
