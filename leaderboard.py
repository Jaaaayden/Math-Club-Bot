import aiofiles

async def restart_leaderboard(members):
    async with aiofiles.open('global_leaderboard.txt', 'w') as file:
        for member in members:
            await file.write(f"{member} 0\n") 

async def add_new_members_leaderboard(members):
    async with aiofiles.open('global_leaderboard.txt', 'r') as file:
        all_users = await file.readlines()
    
    existing_users = {user.split()[0].strip() for user in all_users}
    print(existing_users)

    async with aiofiles.open('global_leaderboard.txt', 'a') as file:
        for member in members:
            if str(member) not in existing_users:
                await file.write(f"{member} 0\n")
    
    """
    async with aiofiles.open('global_leaderboard.txt', 'r') as file:
        all_users = await file.readlines()
    print(all_users)
    """

async def update_leaderboard(username):
    async with aiofiles.open('order_answered.txt', 'r') as file:
        all_users = await file.readlines()
    order_answered = len(all_users) # (OLD) since first answer = 6 pts, second answer = 4 pts, third answer = 2 pts, and remaining = 1 pt, 
                                    # need to keep track of order_answered
    async with aiofiles.open('global_leaderboard.txt', 'r') as file:
        all_users = await file.readlines()
        
    async with aiofiles.open('times_answered.txt', 'r') as file:
        all_attempts = await file.readlines()
        
    leaderboard = {}
    for line in all_users:
        user, points = line.strip().split(maxsplit=1)  
        leaderboard[user] = int(points)      
    # print(leaderboard)
    
    attempts_dict ={}
    for line in all_attempts:
        user, attempts = line.strip().split(maxsplit=1)
        attempts_dict[user] = int(attempts)
    
    """ OLD
    if (order_answered == 1):
        leaderboard[username] = 6 - 2*(attempts[username])
    elif (order_answered == 2):
        leaderboard[username] = 4 - 2*(attempts[username])
    elif (order_answered == 3):
        leaderboard[username] = 2 - 2*(attempts[username])
    else:
        leaderboard[username] = 1 - 2*(attempts[username])
    """
    
    leaderboard[username] = leaderboard[username] + 6 - 2*(attempts_dict[username]) # new implementation uses only attempt count for point calculation
        
    sorted_leaderboard = sorted(leaderboard.items(), key=lambda item: item[1], reverse=True) # sorting list by descending after modifying pts of user who got correct

    async with aiofiles.open('global_leaderboard.txt', 'w') as file: # rewriting new sorted list
        for user, points in sorted_leaderboard:
            await file.write(f"{user} {points}\n")
    