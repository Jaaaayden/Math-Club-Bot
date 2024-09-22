import aiofiles

# same user can't earn points on same question
async def restart_times_answered(members):
    async with aiofiles.open('times_answered.txt', 'w') as file:
        for member in members:
            await file.write(f"{member} 0\n") 
            
async def update_times_answered(username):
    async with aiofiles.open('times_answered.txt', 'r') as file:
        all_users = await file.readlines()
        
    attempt_counts = {}
    for line in all_users:
        user, attempts = line.strip().split(maxsplit=1)  
        attempt_counts[user] = int(attempts)      
    
    attempt_counts[username] += 1

    async with aiofiles.open('times_answered.txt', 'w') as file: # rewriting new sorted list
        for user, attempts in attempt_counts.items():
            await file.write(f"{user} {attempts}\n")
    