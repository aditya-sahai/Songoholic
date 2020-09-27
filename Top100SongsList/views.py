from django.shortcuts import render
from Top100SongsList.BillboardScraper import BillboardScraper


def top_100(request):
    Scraper = BillboardScraper()
    Scraper.get_table_soup()
    Scraper.get_table_data()
    
    return render(request, "Top100SongsList/billboard-top-100.html", {"data": Scraper.table_data})