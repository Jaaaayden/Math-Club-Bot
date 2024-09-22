import base64
import traceback
import urllib.parse as ul
from PIL import Image # GPT helped with this to make text readable from PageSpeedInsight API
from io import BytesIO
from dotenv import load_dotenv
import os
import random
import aiofiles
import aiohttp
import asyncio

# It's possible to make requests without the api key, but the number of requests is very limited  
# code from https://stackoverflow.com/questions/1197172/how-can-i-take-a-screenshot-image-of-a-website-using-python

load_dotenv()

async def take_picture(version):
    rand_int = random.randint(0, 1149) # implemenatation from scrape_amc_problem
    
    # code for reading specific lines from .txt file merged with async https://stackoverflow.com/questions/7523001/how-do-you-read-a-specific-line-of-a-text-file-in-python
    async with aiofiles.open(f'questions{version}.txt', 'r') as load_questions:
        lines = await load_questions.readlines()
        url = lines[rand_int].strip()
        print(url)

    async with aiofiles.open(f'answers{version}.txt', 'r') as load_answers:
        lines = await load_answers.readlines()
        letter = lines[rand_int].strip()
        print(letter)

    async with aiofiles.open('question.txt', 'w') as file:
        await file.write(f"{version}-{letter}")
        
    urle = ul.quote_plus(url)
    image_path: str = "question.jpg"

    key: str = os.getenv('PAGESPEED_INSIGHTS_KEY') # using PageSpeedInsightAPI
    strategy: str = "mobile" # mobile works best because of text readability
    u = f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed?key={key}&strategy={strategy}&url={urle}"

    try:
        async with aiohttp.ClientSession() as session: # aiohttp/async is necessary to stop blocking functions
            async with session.get(u) as response:
                j = await response.json()
                ss_encoded = j['lighthouseResult']['audits']['final-screenshot']['details']['data'].replace("data:image/jpeg;base64,", "")
                ss_decoded = base64.b64decode(ss_encoded) 

                loop = asyncio.get_event_loop() # more non-blocking function stuff
                await loop.run_in_executor(None, process_image, ss_decoded, image_path)
    except:
        print(traceback.format_exc())
        exit(1)
        
# GPT helped with upscale
def process_image(ss_decoded, image_path):
    # Open the image using PIL
    image = Image.open(BytesIO(ss_decoded))

    # Optionally increase the resolution by resizing the image
    width, height = image.size
    upscale_factor = 2
    image = image.resize((width * upscale_factor, height * upscale_factor), Image.BICUBIC)

    # Crop the image to keep only the top half
    cropped_image = image.crop((0, 0, width * upscale_factor, (height * upscale_factor) // 2))

    # Save the cropped image with high quality
    cropped_image.save(image_path, quality=95)