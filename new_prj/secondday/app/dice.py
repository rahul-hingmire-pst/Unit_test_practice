import random
import requests

def rolldice():
    print("Rolling a Dice")
    num = random.randint(1,6)
    return num

def guess_number(num):
    result = rolldice()
    if(result == num):
       return "You Won the match"
    else:
        return "You lost the match"
    
def get_ip():
    response = requests.get("https://httpbin.org/ip")
    if response.status_code == 200:
        return response.json()['origin']











