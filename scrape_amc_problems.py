from bs4 import BeautifulSoup
import urllib.request
import random
    
# issue with pulling answers from AMC 12 -- .txt modified manually
def scrape_amc_problems(url, version): # code from youtube tutorial on web scraping: https://youtu.be/LC9yE7T93cs?si=MUecCEbKP-lDsD5Q
    r = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(r, 'lxml')
    type(soup)
    problem_links = []
    actual_problems = []
    answer_links = []
    actual_answers = []
    
    for link in soup.find_all('a', href=True): # technically not necessary to scrape when links are similar but will help for addiitonal functionality in future
        href = link['href']
        # print(href)
        if ((f"AMC_{version}A" in href or f"AMC_{version}B" in href) and "2024" not in href): # blank page for 2024
            full_url = f"https://artofproblemsolving.com{href}"
            problem_links.append(full_url)
    problem_links.reverse() 
    
    for num in range(2002, 2024): # realized not necessary to web scrape links since links mostly follow same format
        answer_links.append(f"https://artofproblemsolving.com/wiki/index.php/{num}_AMC_{version}B_Answer_Key") # problem links reversed makes it so it goes B -> A
        answer_links.append(f"https://artofproblemsolving.com/wiki/index.php/{num}_AMC_{version}A_Answer_Key")
        if (num == 2021):
            answer_links.append(f"https://artofproblemsolving.com/wiki/index.php/{num}_Fall_AMC_{version}B_Answer_Key")
            answer_links.append(f"https://artofproblemsolving.com/wiki/index.php/{num}_Fall_AMC_{version}A_Answer_Key")
            
    with open(f'questions{version}.txt', 'w') as file:
        for link in problem_links:
            for problem in range(1, 26):
                file.write(f"{link}_Problems#Problem_{problem}\n")
                actual_problems.append(f"{link}_Problems#Problem_{problem}")
    # print(actual_problems)
    
    count: int = 0 # 2015 AMC 10A Problems/Problem 20 has an issue where the problem was incorrectly displayed and needs to be added independently
    with open(f'answers{version}.txt', 'w') as file:
        for link in answer_links:
            r2 = urllib.request.urlopen(link).read()

            soup2 = BeautifulSoup(r2, 'lxml')

            problem_div = soup2.find('div', class_='mw-parser-output')
            
            list_items = problem_div.find_all('li')

            for li in list_items:
                if (len(li.get_text().strip()) == 1):
                    answer_text = li.get_text().strip()
                    if (count == 669):
                        file.write(f"B\n{answer_text}\n")
                    else:
                        file.write(f"{answer_text}\n")
                    count += 1
                    actual_answers.append(answer_text)
                    
        # print(actual_answers)
    rand_num: int = random.randint(0, 1149) # generates random problem from 2002 to 2023 AMC A/B
    
    return [actual_problems[rand_num], actual_answers[rand_num]] # this is no longer practical since pulling all problems and answers for each function call is unnecessary
    # instead of using return, i'm now storing all problems/answers in .txt file generated by this function and randomly generating in picture_problem.py
    
# scrape_amc_problems("https://artofproblemsolving.com/wiki/index.php/AMC_10_Problems_and_Solutions", "10")
# scrape_amc_problems("https://artofproblemsolving.com/wiki/index.php/AMC_12_Problems_and_Solutions", "12")