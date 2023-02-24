# https://realpython.com/python-web-scraping-practical-introduction/

# A Practical Introduction to Web Scraping in Python

from urllib.request import urlopen
url = "http://olympus.realpython.org/profiles/aphrodite"

page = urlopen(url)
page

html_bytes = page.read()
html = html_bytes.decode("utf-8")

html

title_index = html.find("<title>")
title_index

html.find("<head>")

start_index = title_index + len("<title>")
end_index = html.find("</title>")

title = html[start_index:end_index]
title



url = "http://olympus.realpython.org/profiles/poseidon"
page = urlopen(url)
html = page.read().decode("utf-8")
start_index = html.find("<title>") + len("<title>")
end_index = html.find("</title>")
title = html[start_index:end_index]
title

# Get to Know Regular Expressions
import re

re.findall("ab*c", "abcbed")

re.findall("ab*c", "ABCEDDE", re.IGNORECASE)

re.findall("a.*c", "abc")
re.findall("a.*c", "abbc")
re.findall("a.*c", "ac")
re.findall("a.*c", "acc")

string = "Everything is <replaced> blue if it's in <tags>."
string = re.sub("<.*>", "ELEPHANTS", string)
string

string = re.sub("<.*?>", "ELEPHANTS", string)
string



url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")

pattern = "<title.*?>.*?</title.*?>"
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()
title = re.sub("<.*?>", "", title) # Remove HTML tags

print(title)

"""Take a closer look at the first regular expression in the pattern 
string by breaking it down into three parts:

<title.*?> matches the opening <TITLE > tag in html. 
The <title part of the pattern matches with <TITLE because re.search() 
is called with re.IGNORECASE, and .*?> 
matches any text after <TITLE up to the first instance of >.

.*? non-greedily matches all text after the opening <TITLE >, 
stopping at the first match for </title.*?>.

</title.*?> differs from the first pattern only in its use of the 
/ character, so it matches the closing </title  / > tag in html.
"""

for string in ["Name: ", "Favorite animal:"]:
    string_start_idx = html.find(string)
    text_start_idx = string_start_idx + len(string)
    next_html_tag_offset = html[text_start_idx:].find("<")
    text_end_idx = text_start_idx + next_html_tag_offset
    raw_text = html[text_start_idx : text_end_idx]
    clean_text = raw_text.strip(" \r\n\t")
    print(clean_text)


from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

print(soup.get_text())

soup.find_all("img")

image1, image2 = soup.find_all("img")

image1["src"]
image2["src"]

soup.title.string

base_url = "http://olympus.realpython.org"

html_page = urlopen(f"{base_url}/profiles")
html_text = html_page.read().decode("utf-8")

soup = BeautifulSoup(html_text, "html.parser")

for link in soup.find_all("a"):
    link_url = base_url + link["href"]
    print(link_url)
