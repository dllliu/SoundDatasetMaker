from __future__ import print_function
import freesound
import os
import sys
import time


api_key = os.getenv('FREESOUND_API_KEY', "BLkaRWL7Vr8nl6K2yvzDw3q3SKKYiuMlclJU7ECy")
if api_key is None:
    print("You need to set your API key as an evironment variable",)
    print("named FREESOUND_API_KEY")
    sys.exit(-1)

client_secret = "BLkaRWL7Vr8nl6K2yvzDw3q3SKKYiuMlclJU7ECy"
client_id = "uPkz0WfINfbiy8r7exNy"
token = "BLkaRWL7Vr8nl6K2yvzDw3q3SKKYiuMlclJU7ECy"

delay = 2; #set time between execution of each download

client = freesound.FreesoundClient()
client.set_token(token,"token")

#Voice Class
strOfVoices = "";
voices_arr = ["people talking house","people laughing house","singing home","coughing home","house shouting"]
for x in voices_arr:
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username")
    for sound in page:
        time.sleep(delay)
        sound.retrieve_preview(".",sound.name+".mp3")
        strOfVoices += "Sound Name:" + sound.name + " Duration:" + str(sound.duration)+ " User:" + sound.username
        strOfVoices  += "\n"
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username")

print("Download of Human Voice Class Completed")
with open('voices.txt', "a") as file:
    file.write(strOfVoices)


#Beginning of Movement class

strOfMvmnt = ""

mvmnt_arr = ["beverages","home walking","house eating","setting table","washing dishes", "cutting food"]
for x in mvmnt_arr:
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username")
    for sound in page:
        time.sleep(delay)
        sound.retrieve_preview(".",sound.name+".mp3")
        strOfMvmnt += "Sound Name:" + sound.name + " Duration:" + str(sound.duration)+ " User:" + sound.username
        strOfMvmnt  += "\n"
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username")

resultsItems = client.text_search(query="household items",fields="id,name,previews,duration,analysis,username")

for sound in resultsItems:
    sound.retrieve_preview(".",sound.name+".mp3")
    strOfMvmnt += "Sound Name:" + sound.name + " Duration:" + str(sound.duration)+ " User:" + sound.username
    strOfMvmnt  += "\n"

resultsPG2 = resultsItems.next_page();
for sound in resultsPG2:
    sound.retrieve_preview(".",sound.name+".mp3")
    strOfMvmnt += "Sound Name:" + sound.name + " Duration:" + str(sound.duration)+ " User:" + sound.username
    strOfMvmnt  += "\n"

print("Movement Class Downloaded")
file = open('movement.txt', "a")
file.write(strOfMvmnt)
file.close()

#Hygiene CLass
strOfhyg = ""
Hyg_arr = ["hygiene","vaccum","shaving","cleaning home","brushing teeth","washing clothes"]
for x in Hyg_arr:
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username")
    for sound in page:
        time.sleep(delay)
        sound.retrieve_preview(".",sound.name+".mp3")
        strOfhyg += "Sound Name:" + sound.name + " Duration:" + str(sound.duration)+ " User:" + sound.username
        strOfhyg  += "\n"
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username")

print("Hygiene Class Downloaded")
file = open('hygiene.txt', "a")
file.write(strOfhyg)
file.close()

#Nature Class
strOfntr = ""
ntr_arr = ["weather","hail","thunder"]
for x in ntr_arr:
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username")
    for sound in page:
        time.sleep(delay)
        sound.retrieve_preview(".",sound.name+".mp3")
        strOfntr += "Sound Name:" + sound.name + " Duration:" + str(sound.duration)+ " User:" + sound.username
        strOfntr  += "\n"
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username")

print("Nature Class Downloaded")
file = open('elements.txt', "a")
file.write(strOfntr)
file.close()

strOfanm = ""
anm_arr = ["bark","mews","tweet"]
for x in anm_arr:
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username")
    for sound in page:
        time.sleep(delay)
        sound.retrieve_preview(".",sound.name+".mp3")
        strOfanm += "Sound Name:" + sound.name + " Duration:" + str(sound.duration)+ " User:" + sound.username
        strOfanm += "\n"
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username")

print("Animal Class Finished Downloading")
file = open('animals.txt', "a")
file.write(strOfanm)
file.close()

"""
strofApp = ""
App_arr = []
for x in App_arr:
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username")
    for sound in page:
        time.sleep(delay)
        sound.retrieve_preview(".",sound.name+".mp3")
        strOfApp += "Sound Name:" + sound.name + " Duration:" + str(sound.duration)+ " User:" + sound.username
        strOfApp += "\n"
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username")

print("Appliance Class Finished Downloading")
file = open('Appliances.txt', "a")
file.write(strOfApp)
file.close()

time.sleep(delay)

strofFrnt = ""
results7 = client.text_search(query="urban animals",fields="id,name,previews,duration")
print()
for sound in results7:
    sound.retrieve_preview(".",sound.name+".mp3")
    strofFrnt += "Sound Name:" + sound.name + " Duration:" + str(sound.duration)
    strofFrnt += "\n"

file = open('Furniture.txt', "a")
file.write(strofFrnt)
file.close()

time.sleep(delay)

strofMusic = ""
results8 = client.text_search(query="instruments",fields="id,name,previews,duration")
print()
for sound in results8:
    sound.retrieve_preview(".",sound.name+".mp3")
    strofMusic += "Sound Name:" + sound.name + " Duration:" + str(sound.duration)
    strofMusic += "\n"

file = open('Instruments.txt', "a")
file.write(strofMusic)
file.close()

time.sleep(delay)

strofNoti = ""
results9 = client.text_search(query="device notifications",fields="id,name,previews,duration")
print()
for sound in results9:
    sound.retrieve_preview(".",sound.name+".mp3")
    strofNoti += "Sound Name:" + sound.name + " Duration:" + str(sound.duration)
    strofNoti += "\n"

file = open('Notifications.txt', "a")
file.write(strofNoti)
file.close()

time.sleep(delay)
"""
