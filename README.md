# Math-Club-Bot
With competition math getting tougher and tougher each year, it's becoming far more difficult for students with no prior experience to get into. This bot serves to introduce newcomers to the types of questions you'll see on the AMC 10/12 exams and also have a way to practice them through one of the most popular social media platforms. 

# Usage
```
!random amc_10  Generates a random AMC 10 question 
!random amc_12  Generates a random AMC 12 question
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
python-dotenv (referred to as dotenv in the actual code)
pillow (referred to as PIL in the actual code)
discord (if this doesn't work, import discord.py too)
asyncio
aiofiles
aiohttp
bs4
urllib3
sympy
```

Make a .env file and store your Discord token and PageSpeed Insights key in there. For more information, check out: https://developers.google.com/speed/docs/insights/v5/get-started and https://www.writebots.com/discord-bot-token/

Run main.py and the bot should come online

# Future Plans
Make leaderboard scrollable 

Make bot accept numerical answer too (difficult with questions with text in answer choice)

Use machine learning to create completely new questions based on existing ones

# Credits
This project was developed with the help of discord.py API and PageSpeed Insights API

Huge thanks to https://pylexnodes.net/ for providing free hosting for the bot 24/7
 

