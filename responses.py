from picture_problem import take_picture
import asyncio
import aiofiles

async def get_response(user_input: str, channel: str) -> str:
    lowered: str = user_input.lower() # lowercase everything bc python is case-sensitive
    
    if (lowered == '!random amc_10'):
        await asyncio.create_task(take_picture("10")) # stops the function from getting blocked by running in separate thread
        async with aiofiles.open('order_answered.txt', 'w') as file: # clears order_answered because new problem generated
            pass
        return "Problem updated successfully"
    elif (lowered == '!random amc_12'):
        await asyncio.create_task(take_picture("12"))
        async with aiofiles.open('order_answered.txt', 'w') as file:
            pass
        return "Problem updated successfully"
