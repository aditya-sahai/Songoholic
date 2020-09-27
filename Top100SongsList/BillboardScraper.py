from bs4 import BeautifulSoup
import requests


class BillboardScraper:
    def __init__(self):
        self.TOP_100_SONGS_URL = "https://www.billboard.com/charts/hot-100"
        self.DATA_FILE_NAME = "billboard-data.csv"

    def get_table_soup(self):
        """Sends a request to scraping url and gets the table soup."""
        response = requests.get(self.TOP_100_SONGS_URL)
        print(f"Response Status Code: {response.status_code}")

        self.table_soup = BeautifulSoup(response.content, "html.parser").find("ol", {"class": "chart-list__elements"})

    def get_table_data(self):
        """Returns a list of dictionaries representing a row."""

        self.table_data = []
        table_rows = self.table_soup.find_all("li")

        for index, row in enumerate(table_rows):
            rank = index + 1
            song_name = row.find("span", {"class": "chart-element__information__song text--truncate color--primary"}).get_text().strip()
            artists = row.find("span", {"class": "chart-element__information__artist text--truncate color--secondary"}).get_text().strip()
            peak_rank = int(row.find("span", {"class": "chart-element__information__delta__text text--peak"}).get_text().split(" ")[0])
            wks_on_chart = int(row.find("span", {"class": "chart-element__information__delta__text text--week"}).get_text().split(" ")[0])
            
            if row.find("span", {"class": "sr--only"}) != None:
                rank_last_week = int(row.find("span", {"class": "chart-element__information__delta__text text--last"}).get_text().split(" ")[0])

            else:
                rank_last_week = "-"

            # print(f"\nRank: {rank}")
            # print(f"Song: {song_name}")
            # print(f"Artists: {artists}")
            # print(f"Rank Last Week: {rank_last_week}")
            # print(f"Peak Rank: {peak_rank}")
            # print(f"Weeks On Chart: {wks_on_chart}")

            data_dict = {
                "rank": rank,
                "song_name": song_name,
                "artists": artists,
                "peak_rank": peak_rank,
                "weeks_on_chart": wks_on_chart,
                "rank_last_week": rank_last_week,
            }

            self.table_data.append(data_dict)

    def make_csv(self):
        """Makes/updates the csv file."""

        with open(self.DATA_FILE_NAME, "w") as data_write_file:
            data_write_file.write('"Rank","Artists","Peak Rank","Weeks On Chart","Rank Last Week"\n')
            for row in self.table_data:
                line = f'\"{row["rank"]}\",\"{row["song-name"]}\",\"{row["artists"]}\",\"{row["peak-rank"]}\",\"{row["weeks-on-chart"]}\",\"{row["rank-last-week"]}\"\n'
                data_write_file.write(line)

    def write_data_in_database(self):
        """Deletes all the pre-existing data in database and writes new data."""
        
        Hot100Data.objects.all.delete()
        
        for row in self.table_data:
            song = Hot100Data()
            song.rank = row["rank"]
            song.song_name = row["song_name"]
            song.artists = row["artists"]
            song.peak_rank = row["peak_rank"]
            song.weeks_on_chart = row["week_-on_chart"]
            song.rank_last_week = row["rank_last_week"]

            song.save()


if __name__ == "__main__":

    Scraper = BillboardScraper()
    Scraper.get_table_soup()
    Scraper.get_table_data()
    Scraper.make_csv()