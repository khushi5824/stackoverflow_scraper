import requests
from bs4 import BeautifulSoup

URL = "https://stackoverflow.com/questions/tagged/python"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# MAIN QUESTIONS CONTAINER
question_list = soup.select("div.s-post-summary")

print("\nPython Tagged Questions:\n")

for i, q in enumerate(question_list, start=1):
    title_tag = q.select_one("h3 a")
    title = title_tag.text.strip()
    link = title_tag.get("href")

    if not link.startswith("http"):
        link = "https://stackoverflow.com" + link

    print(f"{i}. {title}")
    print(f"   {link}\n")
