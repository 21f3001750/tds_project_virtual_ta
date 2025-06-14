# /// script
# dependencies = ["requests < 3.0", "rich","BeautifulSoup4"]
# ///

import requests
from bs4 import BeautifulSoup

base_url = "https://discourse.onlinedegree.iitm.ac.in"
search_url = base_url + "/search?context=category&context_id=34&q=after%3A2025-01-01&skip_context=false"

# Replace with your actual cookies
headers = {
    "User-Agent": "Mozilla/5.0",
    "cookie": "_t=YxR38pUAG8aCZ0Lpj4LbjvPDLarvii8LiKqLt4dZ%2BrQ00XcfXpYycDDeYNA4cA2pB34mqQ2b%2B3F6KX7uy9Xasz2pFrT%2BX%2BXvYMBf8sNF1i3RoFJpZ0WVJEF5CtIrlCC%2BZVi0st1DqFJR8FiwEbXhsGlGBaX01qgbrxoy1yRWJJCPlPC4%2B%2BcuCbM9wKCrIB960wZ2qT%2BipVdnRc5WVICazPtkfEYqJywks9RPd37Nmc%2FyqBMV2Zu08HqrBIUvjEU%2F7QsiVpApbOeTdx8j5Akh6XythXRErYg%2FmcPe9Ch8pJJlhaFesxguTnBhX5WLQNmnuHkRdw%3D%3D--60bIc%2BcsAB58GihU--zAyGOnE%2FGY6r2xj2tWj48w%3D%3D; _forum_session=Ycr6Fo5BhKqDDMQOInqKtBebg86VliBM2XTdPvLPM2IB9aslVUZWGYn3zNMlqIr1fQeTinMMa8C%2F1UrwZLc2nUbyjgrGzvlDUIAI5fk4ydG0w6b8FVepNAjsyGNvRE%2BZRM59oSteWxJffxAv4jP1MhHnk1aiBI04KiXJ9BcAnm4Y%2B0nvGShbvInaUJFyv3GxKGsThvKKCBzFDMim%2FzY0dQ6%2BBxJMCuFeR0z8k96I7F3c636o0EKCnNpNyHiVsE4q%2B99t9MNuuQhISrHwaF3Oi538g29Z4g%3D%3D--yYg0c5ly077Xei%2Fk--9%2BwUO%2FEUqGY4yiwkBqhvWg%3D%3D"
}

response = requests.get(search_url, headers=headers)

if response.status_code != 200:
    print("❌ Failed to fetch the page:", response.status_code)
    exit()

soup = BeautifulSoup(response.text, "html.parser")

posts = soup.select(".topic-title")
if not posts:
    print("⚠️ No posts found. Make sure your cookies are correct and you're logged in.")
else:
    for post in posts:
        title = post.text.strip()
        link = base_url + post['href']
        print("📌", title)
        print("🔗", link)
        print("---")

