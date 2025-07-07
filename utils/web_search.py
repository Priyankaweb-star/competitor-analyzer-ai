'''
from duckduckgo_search import DDGS
import time

def search_competitor_urls(description, keywords, max_results=100):
    query = f"{description} {' '.join(keywords)}"
    results = []

    with DDGS() as ddgs:
        for r in ddgs.text(query, region='wt-wt', safesearch='Off', max_results=max_results):
            results.append({
                "title": r.get("title"),
                "url": r.get("href"),
                "snippet": r.get("body")
            })
            time.sleep(0.5)  

    return results
'''

# utils/web_search.py
import requests

SERPER_API_KEY = ""  #write your serper api key

def search_competitor_urls(description, keywords, max_results=10):
    query = f"{description} {' '.join(keywords)} "#site:.com -blog -list -review -reddit -medium -quora -hubspot"

    
    headers = {
        "X-API-KEY": SERPER_API_KEY,
        "Content-Type": "application/json"
    }

    response = requests.post(
        "https://google.serper.dev/search",
        headers=headers,
        json={"q": query}
    )

    if response.status_code != 200:
        print(f"❌ Error: {response.status_code}")
        return []

    data = response.json()
    results = []
    for r in data.get("organic", [])[:max_results]:
        results.append({
            "title": r.get("title", ""),
            "url": r.get("link", ""),
            "snippet": r.get("snippet", "")
        })

    return results
