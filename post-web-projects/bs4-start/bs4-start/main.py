from bs4 import BeautifulSoup
# import lxml

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents,"html.parser")
#
# p_tag = soup.find_all(name="a")
# for tag in p_tag:
#     # print(tag.getText())
#     print(tag.get("href"))


# heading = soup.find(name="h1",id="name")
# print(heading)
# print(soup.title)
# print(soup.title.string)
# print(soup.a)
x = soup.select_one(selector=".heading")
print(x)