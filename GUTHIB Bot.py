# Code By Krypto Kiddo
# Yes I know what this means.
# I respect your opinion on this, we all have our own perspectives.
# You know, things are not as black and white in life, You can't really differentiate right from wrong THAT easily.

# This is just to show you that judging people on people's number of contributions...
# You really need to revise your selection criteria bro

# Hence I bring to you the GUTHIB bot
# To prove that github's activity chart can be misleading
# ...unless you try to take a closer look

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


import time # TIME IS MINE ... MUAHAHAHA ... *ahem* okay, nvm.

import random
def randomCoolAddress(): # Skip this to avoid spoilers :P
    string = "000x"
    for i in range (0,20):
        if (random.randint(0,1)):
            string+=chr(random.randint(65,90))
        else:
            string+=chr(random.randint(48,57))
    return(string)

def randomShortMsg(): # Again, Skip this to avoid spoilers :P
    string = "0x"
    for i in range (0,3):
        string+=chr(random.randint(65,90))
    return(string) # What are the odds it will return 'SEX' xD , Yea Yea I know its 24 cubed. Fuck off, Nerd!




gecko_path = PATH TO YOUR GECKODRIVER.EXE FILE # EDIT THIS PATH WHILE PASTING
browser= webdriver.Firefox(executable_path=gecko_path)

# LOGGING IN
browser.get("https://github.com/login") # Navigate to Login Page
# Finding Email and Password fields
email = browser.find_element_by_name("login")
pwd = browser.find_element_by_name("password")
# Entering the username and password in respective fields
email.send_keys(YOUR USERNAME HERE)
pwd.send_keys(YOUR PASSWORD HERE) # ERASE THIS YOU IDIOT
loginBtn = browser.find_element_by_name("commit") # Finding the login button
loginBtn.click() # Do i even need to explain this ? O.O
# TAKES ABOUT 12secs uptill here on my PC (best specs but from 4 years ago xD)


for cumMeat in range(0,10): # cumeating 10 times in the repo
    browser.get("https://github.com/"+YOUR_USER_NAME+"/"+REPO_NAME+"/edit/"+BRANCH_NAME"/"+TARGET_FILE_NAME)# Opening the code editor for target file
    # time.sleep(3) # Enable this when your network is slow.
    codeBox = browser.find_elements_by_id("code-editor")[0] # Finding the code editor area on the page
    codeBox.click() # Seriously?
    codeBox.send_keys(randomCoolAddress()) # Write a random cool looking text in the code editor
    comeEatBox = browser.find_element_by_name("message") # comeEat == Commit ... get it? .. get it? .. ahahahah .. *ahem* nvm again.
    comeEatBox.send_keys(randomShortMsg())
    submitBtn = browser.find_elements_by_class_name("js-blob-submit")[0]
    submitBtn.click() # Okay Okay, basically, this inbuilt function/method is used to re-enact the clicking action on a selenium web object, usually buttons and text areas. Happy ?

# Takes like 40 secs for 10 commits. Voila!
