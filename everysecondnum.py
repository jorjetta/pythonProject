import random
import requests

breed_url = requests.get("https://dog.ceo/api/breeds/list/all")
my_keys = breed_url.json()['message']
key_list = list(my_keys.keys())
print(key_list)
user_choice = input("select breed\n")
user_url = requests.get(f"https://dog.ceo/api/breed/{user_choice}/images")
response = user_url.json()['message']
random_url = random.choice(response)
print(random_url)
data = requests.get(random_url).content
f = open(f'{user_choice}.png', 'wb')
f.write(data)
f.close()
