import time

import requests
import random


def breed_choice():
    image = requests.get("https://dog.ceo/api/breeds/list/all")
    breed_list = image.json()['message']
    key_list = list(breed_list.keys())
    return key_list


def breed_image(breed: str):
    response = requests.get(f"https://dog.ceo/api/breed/{breed}/images")
    image_url = random.choice(response.json()['message'])
    return image_url


def download_iamge(image_url: str, breed: str):
    photo = requests.get(image_url)
    f = open(f"{breed}.png", "wb")
    f.write(photo.content)
    f.close()


def download_random_dog():
    breed_list = breed_choice()
    print(breed_list)
    user_input = input("breed\n")
    for i in range(1,4):
        image_url = breed_image(user_input)
        download_iamge(image_url,user_input)
        time.sleep((5))


download_random_dog()