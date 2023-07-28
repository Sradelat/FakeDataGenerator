import random
import csv
import requests
import time
from pprint import pprint
import json
from config import Settings

# How to decide which genre, rating, company ect is reviewed better
# Code RANDOM elements to perform better -maybe a favored and unfavored variable with a different weight applied to each
# Maybe write some tests for these functions


def add_word(word, container):
    """Adds a word into container specified. The word is written into a JSON file used for permanent storage. If the
    word is already in the container, the user will be notified."""
    with open("WordsAsLetters.json", "r") as jf:  # read only
        data = json.loads(jf.read())  # fetches text from JSON file and applies it to a variable
    jf.close()  # close document from read only

    if word not in data["words"][container]:  # edit datapoint
        data["words"][container].append(word)
        print(f"The word '{word}' was added to {container}")
    else:
        return print(f"The word '{word}' is already in {container}.")

    with open("WordsAsLetters.json", "w") as jf:  # write
        return json.dump(data, jf, indent=4)  # dumps entire file back in with edited datapoint


def delete_word(word, container):
    """Deletes a word from container specified. The word is deleted from a JSON file used for permanent storage. If
    the word does not exist in the container, the user will be notified."""
    with open("WordsAsLetters.json", "r") as jf:
        data = json.loads(jf.read())
    jf.close()
    if word in data["words"][container]:
        data["words"][container].remove(word)
        print(f"The word '{word}' was deleted from {container}")
    else:
        return print(f"The word '{word}' is not in {container}.")

    with open("WordsAsLetters.json", "w") as jf:
        return json.dump(data, jf, indent=4)


def iseven(num):
    """Checks if the number passed is even or not."""
    if num % 2 == 0:
        return True
    else:
        return False


def back_weight(lst):
    """Creates a list for weighting which can be used in a function like random.choices. The weighting favors elements
    near the end of the list."""
    length = len(lst)
    weight = [(x + 1) * 10 for x in range(0, length)]
    return weight


def front_weight(lst):
    """Creates a list for weighting which can be used in a function like random.choices. The weighting favors elements
    near the start of the list."""
    length = len(lst)
    weight = [x * 10 for x in range(length, 0, -1)]
    return weight


def middle_weight(lst):
    """Creates a list for weighting which can be used in a function like random.choices. The weighting favors elements
    near the middle of the list."""
    length = len(lst)
    weight = []
    for x in range(length, 0, -1):
        if x == length:
            weight.append(x * 10)
            continue
        elif x % 2 == 0:
            weight.append(x * 10)
            continue
        else:
            weight.insert(0, x * 10)
    return weight


def high_middle_weight(lst):
    """Creates a list for weighting which can be used in a function like random.choices. The weighting favors elements
    near the last 3/4s of the list."""
    length = len(lst)
    weight = []
    for x in range(length, 0, -1):
        if x == length:
            weight.append(x * 10)
            continue
        elif x % 3 == 0:
            weight.append(x * 10)
            continue
        else:
            weight.insert(0, x * 10)
    return weight


def low_middle_weight(lst):
    """Creates a list for weighting which can be used in a function like random.choices. The weighting favors elements
    near the first 3/4s of the list."""
    length = len(lst)
    weight = []
    for x in range(length, 0, -1):
        if x == length:
            weight.append(x * 10)
            continue
        elif x % 3 == 0:
            weight.insert(0, x * 10)
        else:
            weight.append(x * 10)
            continue
    return weight


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


with open("WordsAsLetters.json") as j_file:
    words_contents = json.loads(j_file.read())

    vowels = "aeiou"
    user_score_weight = middle_weight(list(range(Settings.u_score_max + 1)))
    no_of_users_weight = middle_weight(list(range(Settings.no_users + 1)))
    critic_score_weight = middle_weight(list(range(Settings.c_score_max + 1)))
    no_of_critics_weight = middle_weight(list(range(Settings.no_critics + 1)))
    genre_weight = front_weight(words_contents['words']['genres'])
    rating_weight = back_weight(words_contents['words']['movie_ratings'])
    movie_length_weight = middle_weight(range(Settings.len_min, Settings.len_max + 1))
    company_weight = front_weight(words_contents['words']['companies'])

    genre_lottery = random.sample(words_contents['words']['genres'], k=2)
    lucky_genre = genre_lottery[0]
    unlucky_genre = genre_lottery[1]

    company_lottery = random.sample(words_contents['words']['companies'], k=2)
    lucky_company = company_lottery[0]
    unlucky_company = company_lottery[1]

    for i in range(Settings.number_of_data_points + 1):  # change range for amount of data entries
        title = f"{random.choice(words_contents['words']['object_nouns'])} " \
                f"{random.choice(words_contents['words']['prepositions'])} " \
                f"{random.choice(words_contents['words']['concept_nouns'])}"
        article_choice = random.choice([1, 2])
        if article_choice == 1:
            title = f"the {title}"
        else:
            if title[0] in vowels:  # if title starts with a vowel
                title = f"an {title}"
            else:
                title = f"a {title}"

        genre = random.choices(words_contents['words']['genres'], weights=genre_weight)[0]
        year = random.choice(range(Settings.year_min, Settings.year_max + 1))  # maybe edit this to be a full date
        rating = random.choices(words_contents['words']['movie_ratings'], weights=rating_weight)[0]
        movie_length = random.choices(range(Settings.len_min, Settings.len_max + 1), weights=movie_length_weight)[0]
        company = random.choices(words_contents['words']['companies'], weights=company_weight)[0]

        # if genre == lucky_genre
        user_score = random.choices(range(Settings.u_score_max + 1), weights=user_score_weight)[0]
        no_of_users = random.choices(range(Settings.no_users + 1), weights=no_of_users_weight)[0]
        critic_score = random.choices(range(Settings.c_score_max + 1), weights=critic_score_weight)[0]
        no_of_critics = random.choices(range(Settings.no_critics + 1), weights=no_of_critics_weight)[0]

        # Free API gives random lat/long in US - actually ended up with data points outside the US
        # but that's okay because raw data is never perfect
        resp = requests.get("https://api.3geonames.org/?randomland=US&json=1")
        print(resp)
        print(resp.content)
        json = resp.json()  # getting json decoding errors - not sure why yet

        lat = json["major"]["inlatt"]
        long = json["major"]["inlongt"]
        state = json["major"]["prov"]

        # DEBUG PRINT - try to truncate this by creating another column with .left() or whatever it is
        print(
            f"Title: {title.title()}\n"
            f"Company: {company}\n"
            f"Genre: {genre}\n"
            f"Year: {year}\n"
            f"Rating: {rating}\n"
            f"Length: {movie_length}\n"
            f"Critic Score: {critic_score}\n"
            f"Critic Count: {no_of_critics}\n"
            f"User Score: {user_score}\n"
            f"User Count: {no_of_users}\n"
            f"Latitude: {lat}\n"
            f"Longitude: {long}\n"
            f"State: {state}"
              )

        categories = [
            {
                "title": title.title(),
                "company": company,
                "genre": genre,
                "year": year,
                "rating": rating,
                "length": movie_length,
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
        time.sleep(5)
        print(f"{current_time}\n")