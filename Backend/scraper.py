import requests
from bs4 import BeautifulSoup

def scrape_wikipedia(url):
    if not url or not url.startswith("http"):
        raise ValueError("URL must start with http or https")

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/120.0 Safari/537.36"
    }

    try:
        res = requests.get(url, headers=headers, timeout=10, allow_redirects=True)
    except requests.exceptions.RequestException:
        raise ValueError("Unable to reach Wikipedia")

    # Accept ANY 2xx response
    if not (200 <= res.status_code < 300):
        raise ValueError(f"Wikipedia request blocked (status {res.status_code})")

    soup = BeautifulSoup(res.text, "html.parser")

    title_tag = soup.find("h1", id="firstHeading")
    if not title_tag:
        raise ValueError("Invalid Wikipedia page structure")

    paragraphs = soup.select("p")
    if len(paragraphs) < 3:
        raise ValueError("Insufficient content on Wikipedia page")

    text = " ".join(p.text.strip() for p in paragraphs[:15])

    return {
        "title": title_tag.text.strip(),
        "text": text.strip(),
        "raw_html": res.text
    }
