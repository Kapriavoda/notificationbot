import json
import cloudscraper

scraper = cloudscraper.create_scraper()

def check_online(user):
    site_content = scraper.get(f"https://kick.com/api/v2/channels/{user}").text

    dict = json.loads(site_content)

    return dict["livestream"] != None



