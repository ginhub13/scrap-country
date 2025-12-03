import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3




url = "https://www.scrapethissite.com/pages/simple/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

country_blocks = soup.select("div.col-md-4.country")

data = []

for block in country_blocks:
    name = block.find("h3", class_="country-name").get_text(strip=True)
    capital = block.find("span", class_="country-capital").get_text(strip=True)
    population = block.find("span", class_="country-population").get_text(strip=True)

    data.append({
        "name": name,
        "capital": capital,
        "population": population
    })

df = pd.DataFrame(data)
print("iniiiiiii df \n", df)

df.to_csv("../data/countries.csv", index=False)
df.to_excel("../data/countries.xlsx", index=False)
df.to_json("../data/countries.json", orient="records", indent=4)

conn = sqlite3.connect("../data/countries.db")
df.to_sql("countries", conn, if_exists="replace", index=False)
conn.close()

print("Semua file berhasil dibuat di folder ../data/")

print("Current working directory:", os.getcwd())
