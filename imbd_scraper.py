import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.imdb.com/chart/top"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

movies = []
for row in soup.find_all("td", class_="titleColumn"):
    title = row.find("a").text
    year = row.find("span", class_="secondaryInfo").text.strip("()")
    movies.append({"title": title, "year": year})

df = pd.DataFrame(movies)
df.to_csv("top_imdb_movies.csv", index=False)
print("Scraping complete. Saved to top_imdb_movies.csv")
