# Math-Club-Bot
With competition math getting tougher and tougher each year, it's becoming far more difficult for students with no prior experience to get into. This bot serves to introduce newcomers to the types of questions you'll see on the AMC 10/12 exams and also have a way to practice them through one of the most popular social media platforms. 

# Usage
```
/amc_problem_generation Generates an AMC problem
/custom_problem_generation Generate a custom problem (just drop an image)
(~10s delay to take & save picture of problem but bot will respond when problem generation is complete)
/problem  Displays the generated problem in an embed
/answer  Takes an answer choice as an input and awards points for correct answer to question
/view_leaderboard  Displays the five highest scorers (6 points for correct answer first try, -2 points deducted for every additional attempt)
/reset_leaderboard  Completely resets the leaderboard (done on a monthly basis for club competition)
/reset_problem  Resets the attempt count for each user (stored to stop the same user from answering same question multiple times)
/add_new_members  Used when new members join to add them to leaderboard
```

# Clone bot
If you want to host your own clone of the bot, make a new application on Discord's development portal. Check that you have Python installed and install all necessary modules with pip install (module_name).

```
Current module list:
discord.py
python-dotenv (referred to as dotenv in the actual code)
pillow (referred to as PIL in the actual code)
aiofiles
bs4
```

Make a .env file and store your Discord token and PageSpeed Insights key in there. For more information, check out: https://developers.google.com/speed/docs/insights/v5/get-started and https://www.writebots.com/discord-bot-token/

Run main.py and the bot should come online


# Credits
This project was developed with the help of discord.py API and PageSpeed Insights API

Huge thanks to https://pylexnodes.net/ for providing free hosting for the bot 24/7
 

