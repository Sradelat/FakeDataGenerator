
## Weight System
After running the original program and visualizing the resulting data, I realized that the data did not have as much variance as I would have liked. Therefore, I wrote a bit of code to make my data generator a little less random in order to be able to make stronger coorelations with visualizations. In other words, I wanted my bar charts to be less flat. The first thing I did was give a weight to the frequency of each category such as, genre, company, or rating.
<br>
<br>
![GenreWords](https://github.com/Sradelat/FakeDataGenerator/assets/98350632/0bc1b3df-add7-43db-b4df-a030f1a96caa)
![FrontWeight](https://github.com/Sradelat/FakeDataGenerator/assets/98350632/844fc64b-541d-474d-9dfd-f376a610782e)
<br>
<br>
Above is a list of all the genres used and a chart to prove to myself that it is weighted correctly. Genres at the top of the list are more likely to be picked compared to a genre at the bottom of the list. I called this "front weighting."
<br>
<br>

![RatingsWords](https://github.com/Sradelat/FakeDataGenerator/assets/98350632/dc1140c3-dbb9-440e-8f9b-2420c2f6b222)
![BackWeight](https://github.com/Sradelat/FakeDataGenerator/assets/98350632/af4e4fa3-435a-44c4-9124-49c392053113)
<br>
<br>
The above chart shows what I called "back weighting." Its the same as front weighting but in reverse. Elements near the end of the list are more likely to be chosen. The chart proves to me, once again, that it worked.
<br>
<br>
![MiddleWeight](https://github.com/Sradelat/FakeDataGenerator/assets/98350632/ddd54cba-75eb-49fe-8e1a-f6bd3b8a23c0)
<br>
<br>
This is a histogram of the number of occurances of all 2000 critic scores ranged from 0-100. The weight skews the program so that it is more likely choosing a number around 50 on average. This chart above once more proves my "middle weighting" functions correctly.
## Luck System
Once I added the above weight system, I knew that my charts would still be pretty flat if I took an average of all user scores, user amounts, ect. I succeeded in varying my data, but only in one dimension. I wanted to create a system that would favor a certain metric and perhaps disfavor another metric. The result of that is the luck system.
<br>
<br>
I wrote some code to choose two completely random companies and define each of them as either lucky or unlucky. I did the same with the genres category. Then, I created a "high middle" and a "low middle" weight. A "high middle" weight skews the program into choosing a number closer to 75 (out of 100) on average. The "low middle" weight does the opposite by skewing it to a number around 25 (out of 100) on average.
<br>
<br>
If a company or genre ended up being lucky, it would receive scores and number of reviews using the "high middle" weight. If it ended up being unlucky, it would have "low middle" weight. For instance, I have my program pick as follows:
<br>
<br>
![DefinedLucky](https://github.com/Sradelat/FakeDataGenerator/assets/98350632/68276bb6-d8b7-45d4-bf27-1bd90e23f36a)
<br>
<br>
Now, let's see if it worked correctly with companies keeping in mind that "Kind Soldier" is lucky and "Sure Way" is unlucky:
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
Looks like it checks out! I learned a lot of things and encountered many problems that I did not expect during this project. Thank you for taking the time to read this!

