from requests_html import HTMLSession

url = "https://tvshows4mobile.com/search/list_all_tv_series/drama?sort=a-z"
file_name = "shows_list.html"
html_template = """
<h1>All TV Shows Available</h1>
"""
session = HTMLSession()
data = session.get(url)

a_tags = data.html.find("div.data_list div.data a")
file = open(file_name, "w")

for a_tag in a_tags:
	tag = f"<a href='{a_tag.attrs['href']}'>{a_tag.text}</a><br>"
	html_template += tag

file.write(f"<i><h3>Total Shows: {len(a_tags)}</h3></i>" + html_template)
