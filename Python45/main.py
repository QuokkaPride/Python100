from bs4 import BeautifulSoup
import requests

# response = requests.get("https://news.ycombinator.com/news")
response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

# yc_web_page = response.text
empire_web_page = response.text

# soup = BeautifulSoup(yc_web_page, "html.parser")
soup = BeautifulSoup(empire_web_page, "html.parser")

movie_titles_h3 = soup.find_all(name="h3", class_="title")
movie_titles_text = [title.getText() for title in movie_titles_h3]
print(movie_titles_text)

with open("./movies.txt", "w") as file:
    for title in reversed(movie_titles_text):
        file.write(title + "\n")



# title_texts = [title.a.getText() for title in title_spans]
# print(title_texts)

# title_links = [title.a.get("href") for title in title_spans]
# print(title_links)

# upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
# print(upvotes)

# max_index_upvotes = upvotes.index(max(upvotes))
# print(max_index_upvotes)

# print("title: ", title_texts[max_index_upvotes])
# print("link: ", title_links[max_index_upvotes])
# print("upvotes: ", upvotes[max_index_upvotes])







# with open("website.html", "r") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")

# all_anchor_tags = soup.find_all(name="a")

# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)

# company_url = soup.select_one(selector="p a")
# print("company URL: ", 	company_url.get("href"))
