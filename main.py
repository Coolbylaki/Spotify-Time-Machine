import requests
from bs4 import BeautifulSoup

Billboard_endpoint = "https://www.billboard.com/charts/hot-100"

date_choice = input("Which year do you want to travel to?"
                    "Type the date in this format YYYY-MM-DD: ")

response = requests.get(f"{Billboard_endpoint}/{date_choice}/")

billboard_website = response.text

soup = BeautifulSoup(billboard_website, "html.parser")
songs = soup.select(selector="li h3#title-of-a-story")

top_100 = [song.getText().strip() for song in songs]
