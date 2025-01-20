from bs4 import BeautifulSoup
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

music_date = input("what date would you like to travel to sonicly? (format: YYYY-MM-DD): ")
billboard_url = f"https://www.billboard.com/charts/hot-100/{music_date}"
response = requests.get(billboard_url, headers=headers)

billboard_web_page = response.text

soup = BeautifulSoup(billboard_web_page, "html.parser")

song_containers = soup.find_all("ul", class_="o-chart-results-list-row")
# print(song_containers)

songs = []

for container in song_containers:
    rank_tag = container.find("span", class_="c-label")
    rank = rank_tag.get_text(strip=True) if rank_tag else "Unknown Rank"
    
    title_tag = container.find("h3", id="title-of-a-story", class_="c-title")
    title = title_tag.get_text(strip=True) if title_tag else "Unknown Title"

    singer_container_tag = container.find("ul", class_="lrv-a-unstyle-list")
    singer_tag = singer_container_tag.find("span", class_="c-label")
    singer = singer_tag.get_text(strip=True) if singer_tag else "Unknown Singer"

    songs.append({"rank": rank, "title": title, "singer": singer})    

for song in songs:
    print(f"{song['rank']}: {song['title']} by {song['singer']}")