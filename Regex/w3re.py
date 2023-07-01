import re

txt = "Rain doesn't appear in Spain"
x = re.search("^Rain.*Spain$", txt)
x