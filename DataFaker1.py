import random
import csv
import requests
import time
from pprint import pprint
import json


headers = [
    {
        "title": "",
        "company": "",
        "genre": "",
        "year": "",
        "rating": "",
        "length": "",
        "critic_score": "",
        "number_of_critics": "",
        "user_score": "",
        "number_of_users": "",
        "latitude": "",
        "longitude": "",
        "state_filmed": ""
    }
]


with open("Random.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=headers[0].keys())
    writer.writeheader()

vowels = "aeiou"
with open("WordsAsLetters.json") as j_file:
    words = json.loads(j_file.read())
    for i in range(2001):  # change range for amount of data entries
        title = f"{random.choice(words['words']['object_nouns'])} " \
                f"{random.choice(words['words']['prepositions'])} " \
                f"{random.choice(words['words']['concept_nouns'])}"
        article_choice = random.choice([1, 2])
        if article_choice == 1:
            title = f"the {title}"
        else:
            if title[0] in vowels:  # if title starts with a vowel
                title = f"an {title}"
            else:
                title = f"a {title}"
        user_score = random.choice(range(101))
        no_of_users = random.choice(range(3001))
        critic_score = random.choice(range(101))
        no_of_critics = random.choice(range(101))
        genre = random.choice(words['words']['genres'])
        year = random.choice(range(1974, 2024))  # maybe edit this to be a full date
        rating = random.choice(words['words']['movie_ratings'])
        length = random.choice(range(60, 121))
        company = random.choice(words['words']['companies'])

        resp = requests.get("https://api.3geonames.org/?randomland=US&json=1")  # Free API gives random lat/long in US
        print(resp)
        print(resp.content)
        json = resp.json()

        lat = json["nearest"]["inlatt"]
        long = json["nearest"]["inlongt"]
        state = json["nearest"]["prov"]
        # pprint(json)

        categories = [
            {
                "title": title.title(),
                "company": company,
                "genre": genre,
                "year": year,
                "rating": rating,
                "length": length,
                "critic_score": critic_score,
                "number_of_critics": no_of_critics,
                "user_score": user_score,
                "number_of_users": no_of_users,
                "latitude": lat,
                "longitude": long,
                "state_filmed": state
            }
        ]
        with open("Random.csv", "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=categories[0].keys())
            writer.writerow(categories[0])
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        print(current_time)
        time.sleep(5)
