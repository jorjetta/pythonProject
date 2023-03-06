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
    for i in range(1, 4):
        image_url = breed_image(user_input)
        download_iamge(image_url, user_input)
        time.sleep((5))


download_random_dog()

"""
<div data-test-id="select-menu-wrapper"><div data-test-id="birth-date__month__menu" class="base-0-2-355 list-0-2-356" style="top: 41px;"><div class="base-0-2-361 dropdown-0-2-362"><div class="scrollViewport-0-2-360" style="max-height: 405px;"><div class="items-0-2-359"><div class="Select__option Select__option--is-focused Select__option--is-selected css-0" id="react-select-3-option-0" tabindex="-1"><div data-test-id="select-option-wrapper"><div class="base-0-2-369 focused-0-2-372" data-test-id="select-value:1" data-test-disabled="false" style="padding: 3px 20px 3px 3px;"><div class="iconContainer-0-2-370"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" class="base-0-2-37" ie-style=""><path fill-rule="evenodd" d="M12.4 5.6c-.4-.4-1-.4-1.4 0l-4 4-2-2c-.4-.4-1-.4-1.4 0-.4.4-.4 1 0 1.4l2.7 2.7c.2.2.4.3.7.3.3 0 .5-.1.7-.3L12.4 7c.4-.4.4-1 0-1.4z"></path></svg></div><div class="textContainer-0-2-371"><span class="base-0-2-218 control-0-2-226">Январь</span></div></div></div></div><div class="Select__option css-0" id="react-select-3-option-1" tabindex="-1"><div data-test-id="select-option-wrapper"><div class="base-0-2-369" data-test-id="select-value:2" data-test-disabled="false" style="padding: 3px 20px 3px 3px;"><div class="iconContainer-0-2-370"></div><div class="textContainer-0-2-371"><span class="base-0-2-218 control-0-2-226">Февраль</span></div></div></div></div><div class="Select__option css-0" id="react-select-3-option-2" tabindex="-1"><div data-test-id="select-option-wrapper"><div class="base-0-2-369" data-test-id="select-value:3" data-test-disabled="false" style="padding: 3px 20px 3px 3px;"><div class="iconContainer-0-2-370"></div><div class="textContainer-0-2-371"><span class="base-0-2-218 control-0-2-226">Март</span></div></div></div></div><div class="Select__option css-0" id="react-select-3-option-3" tabindex="-1"><div data-test-id="select-option-wrapper"><div class="base-0-2-369" data-test-id="select-value:4" data-test-disabled="false" style="padding: 3px 20px 3px 3px;"><div class="iconContainer-0-2-370"></div><div class="textContainer-0-2-371"><span class="base-0-2-218 control-0-2-226">Апрель</span></div></div></div></div><div class="Select__option css-0" id="react-select-3-option-4" tabindex="-1"><div data-test-id="select-option-wrapper"><div class="base-0-2-369" data-test-id="select-value:5" data-test-disabled="false" style="padding: 3px 20px 3px 3px;"><div class="iconContainer-0-2-370"></div><div class="textContainer-0-2-371"><span class="base-0-2-218 control-0-2-226">Май</span></div></div></div></div><div class="Select__option css-0" id="react-select-3-option-5" tabindex="-1"><div data-test-id="select-option-wrapper"><div class="base-0-2-369" data-test-id="select-value:6" data-test-disabled="false" style="padding: 3px 20px 3px 3px;"><div class="iconContainer-0-2-370"></div><div class="textContainer-0-2-371"><span class="base-0-2-218 control-0-2-226">Июнь</span></div></div></div></div><div class="Select__option css-0" id="react-select-3-option-6" tabindex="-1"><div data-test-id="select-option-wrapper"><div class="base-0-2-369" data-test-id="select-value:7" data-test-disabled="false" style="padding: 3px 20px 3px 3px;"><div class="iconContainer-0-2-370"></div><div class="textContainer-0-2-371"><span class="base-0-2-218 control-0-2-226">Июль</span></div></div></div></div><div class="Select__option css-0" id="react-select-3-option-7" tabindex="-1"><div data-test-id="select-option-wrapper"><div class="base-0-2-369" data-test-id="select-value:8" data-test-disabled="false" style="padding: 3px 20px 3px 3px;"><div class="iconContainer-0-2-370"></div><div class="textContainer-0-2-371"><span class="base-0-2-218 control-0-2-226">Август</span></div></div></div></div><div class="Select__option css-0" id="react-select-3-option-8" tabindex="-1"><div data-test-id="select-option-wrapper"><div class="base-0-2-369" data-test-id="select-value:9" data-test-disabled="false" style="padding: 3px 20px 3px 3px;"><div class="iconContainer-0-2-370"></div><div class="textContainer-0-2-371"><span class="base-0-2-218 control-0-2-226">Сентябрь</span></div></div></div></div><div class="Select__option css-0" id="react-select-3-option-9" tabindex="-1"><div data-test-id="select-option-wrapper"><div class="base-0-2-369" data-test-id="select-value:10" data-test-disabled="false" style="padding: 3px 20px 3px 3px;"><div class="iconContainer-0-2-370"></div><div class="textContainer-0-2-371"><span class="base-0-2-218 control-0-2-226">Октябрь</span></div></div></div></div><div class="Select__option css-0" id="react-select-3-option-10" tabindex="-1"><div data-test-id="select-option-wrapper"><div class="base-0-2-369" data-test-id="select-value:11" data-test-disabled="false" style="padding: 3px 20px 3px 3px;"><div class="iconContainer-0-2-370"></div><div class="textContainer-0-2-371"><span class="base-0-2-218 control-0-2-226">Ноябрь</span></div></div></div></div><div class="Select__option css-0" id="react-select-3-option-11" tabindex="-1"><div data-test-id="select-option-wrapper"><div class="base-0-2-369" data-test-id="select-value:12" data-test-disabled="false" style="padding: 3px 20px 3px 3px;"><div class="iconContainer-0-2-370"></div><div class="textContainer-0-2-371"><span class="base-0-2-218 control-0-2-226">Декабрь</span></div></div></div></div></div></div></div><div ie-style="margin-bottom: calc(40px + 1px)" style="position: absolute; display: none; margin-bottom: calc(41px);"></div></div></div>"""
