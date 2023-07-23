import random
import csv
import requests
import time
from pprint import pprint
import json

headers = [
    {
        "title": "",
        "genre": "",
        "year": "",
        "score": "",
        "number_of_reviews": "",
        "latitude": "",
        "longitude": ""
    }
]


with open("Random.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=headers[0].keys())
    writer.writeheader()

vowels = "aeiou"
with open("WordsAsLetters.json") as j_file:
    words = json.loads(j_file.read())
    for i in range(50):
        title = f"{random.choice(words['words']['object_nouns'])} " \
                f"{random.choice(words['words']['prepositions'])} " \
                f"{random.choice(words['words']['concept_nouns'])}"
        article_choice = random.choice([1, 2])
        if article_choice == 1:
            title = f"the {title}"
        else:
            if title[0] in vowels:
                title = f"an {title}"
            else:
                title = f"a {title}"
        score = random.choice(range(100))
        genre = random.choice(words['words']['genres'])
        no_of_reviews = random.choice(range(3000))
        year = random.choice(range(1974, 2023))

        resp = requests.get("https://api.3geonames.org/?randomland=US&json=1")
        json = resp.json()
        lat = json["major"]["inlatt"]
        long = json["major"]["inlongt"]
        categories = [
            {
                "title": title.title(),
                "genre": genre,
                "year": year,
                "score": score,
                "number_of_reviews": no_of_reviews,
                "latitude": lat,
                "longitude": long
            }
        ]
        with open("Random.csv", "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=categories[0].keys())
            writer.writerow(categories[0])
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        print(current_time)
        # time.sleep(1)
