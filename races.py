from bs4 import BeautifulSoup
import requests


def get_races_data():
    # Data for all races
    races_results_data = [['Grand Prix', 'Winner', 'Second', 'Third']]
    # Variations in url for each race
    race_response_list = ["1124/bahrain", "1125/saudi-arabia", "1108/australia", "1109/italy", "1110/miami", "1111/spain",
                          "1112/monaco", "1126/azerbaijan", "1113/canada", "1114/great-britain", "1115/austria",
                          "1116/france", "1117/hungary", "1118/belgium", "1119/netherlands", "1120/italy", "1133/singapore",
                          "1134/japan", "1135/united-states", "1136/mexico", "1137/brazil", "1138/abu-dhabi"]
    # Get data for each race
    for each in race_response_list:
        response_race_result = requests.get(f"https://www.formula1.com/en/results.html/2022/races/{each}/race-result.html")
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
        except:
            race_result.append("To be raced")
        # Append to list of data for all races
        races_results_data.append(race_result)
    return races_results_data
