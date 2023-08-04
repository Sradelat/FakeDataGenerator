import random
import csv
import requests
import time
import json
from config import Settings


def iseven(num):
    """Checks if the number passed is even or not."""
    if num % 2 == 0:  # if no remainder
        return True
    else:  # if remainder
        return False


def back_weight(lst):
    """Creates a list for weighting which can be used in a function like random.choices. The weighting favors elements
    near the end of the list. The list being weighted must be passed into the function."""
    length = len(lst)  # need the length of the list so that the length of the weighting list can be identical
    weight = [(x + 1) * 10 for x in range(0, length)]  # append list starting with lowest num up to highest num
    return weight


def front_weight(lst):
    """Creates a list for weighting which can be used in a function like random.choices. The weighting favors elements
    near the start of the list. The list being weighted must be passed into the function."""
    length = len(lst)  # need the length of the list so that the length of the weighting list can be identical
    weight = [x * 10 for x in range(length, 0, -1)]  # append list starting with highest num down to lowest num
    return weight


def middle_weight(lst):
    """Creates a list for weighting which can be used in a function like random.choices. The weighting favors elements
    near the middle of the list. The list being weighted must be passed into the function."""
    length = len(lst)  # need the length of the list so that the length of the weighting list can be identical
    weight = []
    for x in range(length, 0, -1):  # start with highest num - creates a list which tapers down from the mid-point
        if x == length:  # highest num enters list first
            weight.append(x * 10)
            continue
        elif x % 2 == 0:  # if num is even: append to the right of highest num
            weight.append(x * 10)
            continue
        else:  # if num is not even: insert to the left of highest num
            weight.insert(0, x * 10)
    return weight


def high_middle_weight(lst):
    """Creates a list for weighting which can be used in a function like random.choices. The weighting favors elements
    near the last 3/4s of the list. The list being weighted must be passed into the function."""
    length = len(lst)  # need the length of the list so that the length of the weighting list can be identical
    weight = []
    for x in range(length, 0, -1):  # start with highest num - creates a list which tapers down from the 3/4s position
        if x == length:  # highest num enters list first
            weight.append(x * 10)
            continue
        elif x % 4 == 0:  # every fourth number appends to the right
            weight.append(x * 10)
            continue
        else:  # every other number inserts at index 0
            weight.insert(0, x * 10)
    return weight


def low_middle_weight(lst):
    """Creates a list for weighting which can be used in a function like random.choices. The weighting favors elements
    near the first 3/4s of the list. The list being weighted must be passed into the function."""
    length = len(lst)  # need the length of the list so that the length of the weighting list can be identical
    weight = []
    for x in range(length, 0, -1):  # start with highest num - creates a list which tapers down from the 1/4 position
        if x == length:  # highest num enters list first
            weight.append(x * 10)
            continue
        elif x % 4 == 0:    # every fourth number inserts at index 0
            weight.insert(0, x * 10)
        else:  # every other number appends to the right
            weight.append(x * 10)
            continue
    return weight


def lucky_metrics():
    """Chooses a random number with HIGH MIDDLE weighting for each metric:
    user score, number of users, critic score, and number of critics."""
    u_score = random.choices(range(Settings.u_score_max + 1), weights=lucky_user_score_weight)[0]
    users = random.choices(range(Settings.no_users + 1), weights=lucky_no_of_users_weight)[0]
    c_score = random.choices(range(Settings.c_score_max + 1), weights=lucky_critic_score_weight)[0]
    critics = random.choices(range(Settings.no_critics + 1), weights=lucky_no_of_critics_weight)[0]
    return u_score, users, c_score, critics


def unlucky_metrics():
    """Chooses a random number with LOW MIDDLE weighting for each metric:
    user score, number of users, critic score, and number of critics."""
    u_score = random.choices(range(Settings.u_score_max + 1), weights=unlucky_user_score_weight)[0]
    users = random.choices(range(Settings.no_users + 1), weights=unlucky_no_of_users_weight)[0]
    c_score = random.choices(range(Settings.c_score_max + 1), weights=unlucky_critic_score_weight)[0]
    critics = random.choices(range(Settings.no_critics + 1), weights=unlucky_no_of_critics_weight)[0]
    return u_score, users, c_score, critics


def normal_metrics():
    """Chooses a random number with MIDDLE weighting for each metric:
    user score, number of users, critic score, and number of critics."""
    u_score = random.choices(range(Settings.u_score_max + 1), weights=user_score_weight)[0]
    users = random.choices(range(Settings.no_users + 1), weights=no_of_users_weight)[0]
    c_score = random.choices(range(Settings.c_score_max + 1), weights=critic_score_weight)[0]
    critics = random.choices(range(Settings.no_critics + 1), weights=no_of_critics_weight)[0]
    return u_score, users, c_score, critics


def show_lucky():
    """Call this if you want to know which companies and genres are lucky and unlucky."""
    return print(
        f"Lucky Genre: {lucky_genre}\n"
        f"Lucky Company: {lucky_company}\n"
        f"Unlucky Genre: {unlucky_genre}\n"
        f"Unlucky Company: {unlucky_company}\n"
    )


# DEFINE COLUMN HEADERS
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

# WRITE COLUMN HEADERS
with open("Random.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=headers[0].keys())
    writer.writeheader()
    f.close()

# READ FILE AND STORE IN VARIABLE
with open("WordsAsLetters.json") as j_file:
    words_contents = json.loads(j_file.read())
    j_file.close()  # can close after storing contents in a variable!

# DEFINE WEIGHTS FOR EACH CATEGORY - Settings in config.py
user_score_weight = middle_weight(list(range(Settings.u_score_max + 1)))
no_of_users_weight = middle_weight(list(range(Settings.no_users + 1)))
critic_score_weight = middle_weight(list(range(Settings.c_score_max + 1)))
no_of_critics_weight = middle_weight(list(range(Settings.no_critics + 1)))
genre_weight = front_weight(words_contents['words']['genres'])
rating_weight = back_weight(words_contents['words']['movie_ratings'])
movie_length_weight = middle_weight(range(Settings.len_min, Settings.len_max + 1))
company_weight = front_weight(words_contents['words']['companies'])

# CHOOSE 2 RANDOM KEYWORDS FROM EACH POOL WITHOUT REPLACEMENT
genre_lottery = random.sample(words_contents['words']['genres'], k=2)
company_lottery = random.sample(words_contents['words']['companies'], k=2)

# ONE LUCKY EACH
lucky_genre = genre_lottery[0]
lucky_company = company_lottery[0]

# ONE UNLUCKY EACH
unlucky_genre = genre_lottery[1]
unlucky_company = company_lottery[1]

# DEFINE LUCKY AND UNLUCKY WEIGHTS - Settings in config.py
lucky_user_score_weight = high_middle_weight(list(range(Settings.u_score_max + 1)))
lucky_no_of_users_weight = high_middle_weight(list(range(Settings.no_users + 1)))
lucky_critic_score_weight = high_middle_weight(list(range(Settings.c_score_max + 1)))
lucky_no_of_critics_weight = high_middle_weight(list(range(Settings.no_critics + 1)))

unlucky_user_score_weight = low_middle_weight(list(range(Settings.u_score_max + 1)))
unlucky_no_of_users_weight = low_middle_weight(list(range(Settings.no_users + 1)))
unlucky_critic_score_weight = low_middle_weight(list(range(Settings.c_score_max + 1)))
unlucky_no_of_critics_weight = low_middle_weight(list(range(Settings.no_critics + 1)))

# FOR USE ON ARTICLE CHOICE
vowels = "aeiou"

for i in range(Settings.number_of_data_points):  # Settings in config.py

    # CHOOSE 3 RANDOM WORDS FOR TITLE
    title = f"{random.choice(words_contents['words']['object_nouns'])} " \
            f"{random.choice(words_contents['words']['prepositions'])} " \
            f"{random.choice(words_contents['words']['concept_nouns'])}"

    # CHOOSE ARTICLE BASED ON FIRST WORD IN TITLE
    article_choice = random.choice([1, 2])  # 1 for "the" and two for "a" or "an"
    if article_choice == 1:  # choose "the"
        title = f"the {title}"
    else:
        if title[0] in vowels:  # if title starts with a vowel then "an"
            title = f"an {title}"
        else:  # else "a"
            title = f"a {title}"

    # CHOOSE VALUES FOR COLUMNS - Settings in config.py
    genre = random.choices(words_contents['words']['genres'], weights=genre_weight)[0]
    year = random.choice(range(Settings.year_min, Settings.year_max + 1))
    rating = random.choices(words_contents['words']['movie_ratings'], weights=rating_weight)[0]
    movie_length = random.choices(range(Settings.len_min, Settings.len_max + 1), weights=movie_length_weight)[0]
    company = random.choices(words_contents['words']['companies'], weights=company_weight)[0]

    # ASSIGN LUCKY METRICS
    if (genre == lucky_genre and company == lucky_company) or \
            (genre == lucky_genre and company != unlucky_company) or \
            (company == lucky_company and genre != unlucky_genre):
        user_score, no_of_users, critic_score, no_of_critics = lucky_metrics()

    # ASSIGN UNLUCKY METRICS
    elif (genre == unlucky_genre and company == unlucky_company) or \
            (genre == unlucky_genre and company != lucky_company) or \
            (company == unlucky_company and genre != lucky_genre):
        user_score, no_of_users, critic_score, no_of_critics = unlucky_metrics()

    # ASSIGN NORMAL METRICS
    else:
        user_score, no_of_users, critic_score, no_of_critics = normal_metrics()

    # API REQUEST - Free API gives random lat/long in US
    resp = requests.get("https://api.3geonames.org/?randomland=US&json=1")
    print(resp, resp.content)  # debug print
    json = resp.json()  # read json

    # DEFINE LOCATIONAL COLUMNS
    lat = json["major"]["inlatt"]
    long = json["major"]["inlongt"]
    state = json["major"]["prov"]

    # DEBUG PRINT BEAUTIFIED
    print(
        f"{'Title: ' + title.title():<40} Genre: {genre}\n"
        f"{'Year: ' + str(year):<40} Rating: {rating}\n"
        f"{'Rating: ' + rating:<40} Length: {movie_length}\n"
        f"{'Critic Score: ' + str(critic_score):<40} Critic Count: {no_of_critics}\n"
        f"{'User Score: ' + str(user_score):<40} User Count: {no_of_users}\n"
        f"{'Latitude: ' + str(lat):<40} {'Longitude: ' + str(long):<40} State: {state}"
          )

    # ASSIGN VARIABLES TO COLUMNS
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

    # WRITE ROW TO CSV
    with open("Random.csv", "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=categories[0].keys())
        writer.writerow(categories[0])
        f.close()

    # WAIT BEFORE LOOPING AGAIN WITH API
    time.sleep(5)

    # SHOW TIME AT THE END OF EACH LOOP
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(f"{current_time}\n")


