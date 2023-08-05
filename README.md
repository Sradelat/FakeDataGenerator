# Fake Data Generator
*An alternative to web scraping.*
### What inspired this project?
After my MetaCritic web scraping project, I was on the hunt for some locational data (latitude and longitude). I wanted
to experiment with it in SQL and Tableau to hone my skills. First, the Google Maps API caught my eye. Then, I realized what
I wanted to do would violate their Terms of Service. I would go on to try other APIs and attempt to find other 
workarounds when I finally discovered that webscraping itself is a huge legal gray area.

After spending more than two weeks working out the kinks of my new scraper, I made the painful decision to abandon the 
project. However, I was still determined to experiment with SQL and Tableau and get a project out of it. So, I decided I would 
create my own data. And the fastest way to do that, would be to fabricate it. Below I will show the steps I took to 
successfully create the data that I needed.

### You wrote too much text below. Give me a summary, please!
I created a program that generates random fake movie data and writes it to Random.csv. My main focus was locational 
data, for that reason, I utilized a free API to generate randomized latitude and longitude within the US. The first result 
is stored in FakeMovies.csv. I imported that into SQLiteStudio3 for some SQL Queries, which can be found in 
SQL_Queries.txt. Finally,I created a couple dashboards in Tableau to visualize some correlations, which can be found 
here: https://public.tableau.com/app/profile/shawn.radelat.

I did not like how one dimensional my data was due to the completely random choices. Therefore, I created a couple of 
functions to have certain metrics (such as genres) occur more often than others. The result of that is 
FakeMoviesWeighted.csv. However, I knew this alone would not produce my desired result. Therefore, I added a luck 
system that would promote an exploratory search into the database to find which metrics are performing well and which 
ones are not. The final result is LuckyFakeMovies.csv.

# My Thought Process
*A deep dive into my thought process aided by visuals!*

## The Data
Early on, I decided I would produce movie related data. That includes movie title, genre, movie rating, reviews, and 
year released. However, usually movie data does not include locational data. Improvising, I decided the data would 
include the location where the movie was filmed.

Here is preview of the final result:
<br>
<br>
![DataPrint](https://github.com/Sradelat/FakeDataGenerator/assets/98350632/08d0dfcc-a0cb-47bd-b114-7e877e295516)


### Movie Title, Genre, Rating, and Movie Companies
Generating a random movie title ended up becoming a fun little project itself. I determined each title would have the
format: 
<br><br>
{article} {object noun} {preposition} {concept noun}<br><br>
"A Robot During Despair" is a title with an example of such format. In order to accomplish this, I knew I would need at
least three separate lists of words. I also wanted the list to be able to be edited using a function. 
<br>
<br>
This is where I discovered that generally data such as this should be stored in a json file. Therefore, I formatted a 
json file that included a list of all words that could be used in the title, along with lists for genres, ratings, 
and movie companies.

### Year, Movie Length, and Review Metrics
To generate and year, movie length, and some review metrics, I created a config file that could be edited to change the
desired ranges of each without having to delve into the code.

### Locational Data
At first, I had the idea that maybe I could pick from a random range of latitude and longitude that I predetermined
was at least "around" the United States. However, the location could end up in another country or out in the ocean. I
had no control over that.

I began searching once again for an API that I could utilize for this project. Most APIs have free plans that you can
sign up for but with far too limited usage for the scope of 2000 datapoints that I was hoping for. Then, I found 
3geonames.org.

It turned out that 3geonames.org was the perfect candidate for my project because the user can request a random location
within a specific region. It provided the latitude, longitude, and the state datapoints for my program. I only had to
be sure not to overload the API, so I created a delay for each loop.

## First Execution
The program successfully created a CSV file of 2000 rows of fake data. I loaded it into SQLite Studio for some SQL
queries and then exported the result into Tableau. Here, I discovered that my data was really flat. It was difficult
to make any distinctions with the data and the ones that I did manage to make were small. The teal shows the number of
occurrences of a genre and the orange shows the average user scores of each company. Notice how close to 50 all the
averages are. Compare these charts to the ones further below.
<br>
<br>
![Flat1](https://github.com/Sradelat/FakeDataGenerator/assets/98350632/77183645-dda3-4a78-8923-32b31a8ff316)
![Flat2](https://github.com/Sradelat/FakeDataGenerator/assets/98350632/e6711b14-276f-4953-acdb-6f3ad8ffc816)
<br>
<br>
I went ahead and created my dashboards with the data I already had. After that, I would return to my program to improve
it. My dashboards can be found here: https://public.tableau.com/app/profile/shawn.radelat

## Weight System
After running the original program and visualizing the resulting data, I realized that the data did not have as much 
variance as I would have liked. Therefore, I wrote a bit of code to make my data generator a little less random in 
order to be able to make stronger correlations with visualizations. In other words, I wanted my bar charts to be 
less flat. The first thing I did was give a weight to the frequency of each category such as, genre, company, or rating.
<br>
<br>
![FrontWeight](https://github.com/Sradelat/FakeDataGenerator/assets/98350632/844fc64b-541d-474d-9dfd-f376a610782e)
![GenreWords](https://github.com/Sradelat/FakeDataGenerator/assets/98350632/0bc1b3df-add7-43db-b4df-a030f1a96caa)
<br>
<br>
Above is a list of all the genres used and a chart to prove to myself that it is weighted correctly. 
Genres at the top of the list are more likely to be picked compared to a genre at the bottom of the list. 
I called this "front weighting."
<br>
<br>

![RatingsWords](https://github.com/Sradelat/FakeDataGenerator/assets/98350632/dc1140c3-dbb9-440e-8f9b-2420c2f6b222)
![BackWeight](https://github.com/Sradelat/FakeDataGenerator/assets/98350632/af4e4fa3-435a-44c4-9124-49c392053113)
<br>
<br>
The above chart shows what I called "back weighting." It's the same as front weighting but in reverse. 
Elements near the end of the list are more likely to be chosen. The chart proves to me, once again, that it worked.
<br>
<br>
![MiddleWeight](https://github.com/Sradelat/FakeDataGenerator/assets/98350632/ddd54cba-75eb-49fe-8e1a-f6bd3b8a23c0)
<br>
<br>
This is a histogram of the number of occurrences of all 2000 critic scores ranged from 0-100. 
The weight skews the program so that it is more likely choosing a number around 50 on average. 
This chart above once more proves my "middle weighting" functions correctly.
## Luck System
Once I added the above weight system, I knew that my charts would still be pretty flat if I took an average of all user 
scores, user amounts, ect. I succeeded in varying my data, but only in one dimension. I wanted to create a system that 
would favor a certain metric and perhaps disfavor another metric. The result of that is the luck system.
<br>
<br>
I wrote some code to choose two completely random companies and define each of them as either lucky or unlucky. I did 
the same with the genres category. Then, I created a "high middle" and a "low middle" weight. A "high middle" weight 
skews the program into choosing a number closer to 75 (out of 100) on average. The "low middle" weight does the 
opposite by skewing it to a number around 25 (out of 100) on average.
<br>
<br>
If a company or genre ended up being lucky, it would receive scores and number of reviews using the "high middle" 
weight. If it ended up being unlucky, it would have "low middle" weight. For instance, I have my program pick as 
follows:
<br>
<br>
![DefinedLucky](https://github.com/Sradelat/FakeDataGenerator/assets/98350632/68276bb6-d8b7-45d4-bf27-1bd90e23f36a)
<br>
<br>
Now, let's see if it worked correctly with companies keeping in mind that "Kind Soldier" is lucky and "Sure Way" is 
unlucky:
<br>
<br>
![LuckyCompany](https://github.com/Sradelat/FakeDataGenerator/assets/98350632/113b4352-b28f-4d65-b7ee-163db6496abe)
<br>
<br>
Again, but with genres. "Musical" is lucky and "Drama" is unlucky:
<br>
<br>
![LuckyGenre](https://github.com/Sradelat/FakeDataGenerator/assets/98350632/866195a3-5e5b-484f-a40d-9ca458b5e8de)
<br>
<br>
Looks like it checks out! This system will make exploring my data more exciting than last time. In conclusion, I learned 
a lot of things and encountered many problems that I did not expect during this project. It is those unexpected problems
that keeps me coming back to programming. Thank you for taking the time to read this!

