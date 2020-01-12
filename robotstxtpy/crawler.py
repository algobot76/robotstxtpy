from bs4 import BeautifulSoup 
import requests
import requests.exceptions
from urllib.parse import urlsplit
from urllib.parse import urlparse
from collections import deque

# takes in a url
# ie. url = "https://scrapethissite.com"
def get_endpoints_from_url(url) -> set():
	new_urls = deque([url])

	# urls that have already been visited
	processed_urls = set()

	# urls that are local to the website
	local_urls = set()

	# urls that are not from the website
	foreign_urls = set()

	# urls that are broken
	broken_urls = set()

	# go through new urls
	while len(new_urls):
		url = new_urls.popleft()
		processed_urls.add(url)
		try:
			response = requests.get(url)
		except(requests.exceptions.MissingSchema,
			   requests.exceptions.ConnectionError,
			   requests.exceptions.InvalidURL,
			   requests.exceptions.InvalidSchema):
			broken_urls.add(url)
			continue
		parts = urlsplit(url)
		base = "{0.netloc}".format(parts)
		strip_base = base.replace("www.", "")
		base_url = "{0.scheme}://{0.netloc}".format(parts)
		path = url[:url.rfind('/')+1] if '/' in parts.path else url
		soup = BeautifulSoup(response.text, "lxml")
		for link in soup.find_all('a'):
			# extract link url from the anchor
			anchor = link.attrs["href"] if "href" in link.attrs else ''
			if anchor.startswith('/'):
				local_link = base_url + anchor
				local_urls.add(local_link)
			elif strip_base in anchor:
				local_urls.add(anchor)
			elif not anchor.startswith('http'):
				local_link = path + anchor
				local_urls.add(local_link)
			else:
				foreign_urls.add(anchor)
			for i in local_urls:
				if not i in new_urls and not i in processed_urls: 
					new_urls.append(i)

	return local_urls
