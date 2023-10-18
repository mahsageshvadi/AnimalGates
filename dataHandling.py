import requests
from bs4 import BeautifulSoup
from googlesearch import search

query = "Cats"

num_results = 10

search_results = list(search(query, num_results=num_results))

# Function to scrape image URLs from a Google search result URL
def get_image_urls(search_result_url):
    response = requests.get(search_result_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')
    img_urls = [img['src'] for img in img_tags if 'src' in img.attrs]
    return img_urls

# Loop through the search result URLs and scrape image URLs
for result_url in search_results:
    image_urls = get_image_urls(result_url)
    for url in image_urls:
        print(url)