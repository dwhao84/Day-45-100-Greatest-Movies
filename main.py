from bs4 import BeautifulSoup
import requests

movie_url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(movie_url)
movie_page = response.text
soup = BeautifulSoup(movie_page, "html.parser")
# print(soup.prettify())

movies = soup.find_all(name="h3", class_="title") # 找到element是h3，並且class叫title。
movie_list = []

# for movie_title in movies:
#     movie_text = movie_title.get_text()
#     movie_list.append(movie_text)

movie_list = [movie_title.get_text() for movie_title in movies]
movie_list.reverse() # 調整movie_list的排序。
# 也可以用 movie_list[::-1] 去調整
print(movie_list)

file = open('items.txt','w')
for movie_name in movie_list:
    file.write(movie_name+"\n")
file.close()






