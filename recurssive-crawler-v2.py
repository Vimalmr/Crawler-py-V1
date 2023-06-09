import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from queue import Queue

# Initialize queue and add starting URL
queue = Queue()
queue.put("https://kongu.ac.in/")
visited = set()
tot_web = set()

# Set recursion limit
MAX_RECURSION = 10

while not queue.empty() and len(visited) < MAX_RECURSION:
    # Get next URL from queue
    try:
        url = queue.get()

        # Skip URL if already visited
        if url in visited:
            continue

        # Print progress
        print(f"Crawling {url}...")

        # Add URL to visited set
        visited.add(url)

        # Send GET request and parse HTML content
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract links from HTML content
        for link in soup.find_all("a"):
            # Get absolute URL
            href = link.get("href")
            if href is not None:
                href = urljoin(url, href)

                # Add URL to queue if it hasn't been visited yet
                if href not in visited:
                    queue.put(href)
            tot_web.add(href)
    except:
        print("Access Denied")

print("Done crawling!")
print(tot_web)
