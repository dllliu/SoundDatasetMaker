from __future__ import print_function
import freesound
import os
import sys
import time

api_key = os.getenv('FREESOUND_API_KEY', "BLkaRWL7Vr8nl6K2yvzDw3q3SKKYiuMlclJU7ECy")
client_secret = "BLkaRWL7Vr8nl6K2yvzDw3q3SKKYiuMlclJU7ECy"
client_id = "uPkz0WfINfbiy8r7exNy"
token = client_secret

delay = 2; #set time between execution of each download

client = freesound.FreesoundClient()
client.set_token(token,"token")

#Voice Class
strOfVoices = "";


page = client.text_search(query="talking",fields="id,name,previews,duration,analysis,username,tags,description")
for sound in page:
    sound.retrieve_preview(".",sound.name)
    strOfVoices += "Sound Name:" + sound.name + " Duration:" + str(sound.duration)+ " User:" + sound.username + " Tags:" + str(sound.tags);
    strOfVoices  += "\n"

nextPage = page.next_page();
for sound in nextPage:
    sound.retrieve_preview(".",sound.name)
    strOfVoices += "Sound Name:" + sound.name + " Duration:" + str(sound.duration)+ " User:" + sound.username + " Tags:" + str(sound.tags);
    strOfVoices  += "\n"

print("Download of Human Voice Class Completed")
with open('voices.txt', "a") as file:
    file.write(strOfVoices)

#Beginning of Movement class

strOfActions = ""

mvmnt_arr = ["home walking","house eating","setting table","washing dishes","cutting food"]
for x in mvmnt_arr:
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username,description,tags")
    for sound in page:
        time.sleep(delay)
        sound.retrieve_preview(".",sound.name)
        strOfActions += "Sound Name:" + sound.name + " Duration:" + str(sound.duration)+ " User:" + sound.username + " Tags:" + str(sound.tags);
        strOfActions  += "\n"
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username,description,tags")

file = open('Actions.txt', "a")
file.write(strOfActions)
file.close()

strOfItems = ""

r_arr = ["box moving","coins","match","keys","velcro","zippers,","box moving"]
for x in r_arr:
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username,description,tags")
    for sound in page:
        time.sleep(delay)
        sound.retrieve_preview(".",sound.name)
        strOfItems += "Sound Name:" + sound.name + " Duration:" + str(sound.duration)+ " User:" + sound.username+ " Tags:" + str(sound.tags);
        strOfItems  += "\n"
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username,description,tags")


file = open('Items.txt', "a")
file.write(strOfItems)
file.close()


strOfBev= ""

bev_arr = ["ice cubes","beverage"]
for x in bev_arr:
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username,description,tags")
    for sound in page:
        time.sleep(delay)
        sound.retrieve_preview(".",sound.name)
        strOfBev += "Sound Name:" + sound.name + " Duration:" + str(sound.duration)+ " User:" + sound.username + " Tags:" + str(sound.tags);
        strOfBev  += "\n"
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username,description,tags")


print("Movement Class Downloaded")



#Hygiene CLass
strOfhyg = ""
Hyg_arr = ["hygiene","vaccum","shaving","cleaning home","brushing teeth","washing clothes"]
for x in Hyg_arr:
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username,description,tags")
    for sound in page:
        time.sleep(delay)
        sound.retrieve_preview(".",sound.name+".wav")
        strOfhyg += "Sound Name:" + sound.name + " Duration:" + str(sound.duration)+ " User:" + sound.username+ " Tags:" + str(sound.tags);
        strOfhyg  += "\n"
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username,description,tags")

print("Hygiene Class Downloaded")
file = open('hygiene.txt', "a")
file.write(strOfhyg)
file.close()

#Nature Class
strOfntr = ""
ntr_arr = ["weather","hail","thunder"]
for x in ntr_arr:
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username,description,tags")
    for sound in page:
        time.sleep(delay)
        sound.retrieve_preview(".",sound.name+".wav")
        strOfntr += "Sound Name:" + sound.name + " Duration:" + str(sound.duration)+ " User:" + sound.username+ " Tags:" + str(sound.tags);
        strOfntr  += "\n"
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username,description,tags")

print("Nature Class Downloaded")
file = open('elements.txt', "a")
file.write(strOfntr)
file.close()

strOfanm = ""
anm_arr = ["bark","mews","tweet"]
for x in anm_arr:
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username,description,tags")
    for sound in page:
        time.sleep(delay)
        sound.retrieve_preview(".",sound.name+".wav")
        strOfanm += "Sound Name:" + sound.name + " Duration:" + str(sound.duration)+ " User:" + sound.username+ " Tags:" + str(sound.tags);
        strOfanm += "\n"
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username,description,tags")

print("Animal Class Finished Downloading")
file = open('animals.txt', "a")
file.write(strOfanm)
file.close()


strofPAplc = ""
PAplc_arr = ["cell phone","camera","computer"]
for x in PAplc_arr:
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username,description,tags")
    for sound in page:
        time.sleep(delay)
        sound.retrieve_preview(".",sound.name+".wav")
        strofPAplc += "Sound Name:" + sound.name + " Duration:" + str(sound.duration)+ " User:" + sound.username+ " Tags:" + str(sound.tags);
        strofPAplc += "\n"
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username,description,tags")

print("Personal Appliance Class Finished Downloading")
file = open('PersonalAppliances.txt', "a")
file.write(strofPAplc)
file.close()



strKitApp = ""
KitAppArr = ["kitchen appliances","oven","blender","garbage disposal","stove","toaster","furnace"]

for x in KitAppArr:
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username,description,tags")
    for sound in page:
        time.sleep(delay)
        sound.retrieve_preview(".",sound.name+".wav")
        strKitApp += "Sound Name:" + sound.name + " Duration:" + str(sound.duration)+ " User:" + sound.username+ " Tags:" + str(sound.tags);
        strKitApp += "\n"
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username,description,tags")

print("Kitchen Appliance Class Finished Downloading")
file = open('Kitchen.txt', "a")
file.write(strKitApp)
file.close()


strLiv = ""
LivApp = ["Sofa","TV","Fan","Light Switch","Blinds"]

for x in LivApp:
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username,description,tags")
    for sound in page:
        time.sleep(delay)
        sound.retrieve_preview(".",sound.name+".wav")
        strLiv += "Sound Name:" + sound.name + " Duration:" + str(sound.duration)+ " User:" + sound.username+ " Tags:" + str(sound.tags);
        strLiv += "\n"
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username,description,tags")

print("Living Room Appliance Class Finished Downloading")
file = open('LivingRoom.txt', "a")
file.write(strLiv)
file.close()

strBano = ""
BanoApp = ["bathroom","ventilator","hair dryer","soap dispenser"]

for x in BanoApp:
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username,description,tags")
    for sound in page:
        time.sleep(delay)
        sound.retrieve_preview(".",sound.name+".wav")
        strBano += "Sound Name:" + sound.name + " Duration:" + str(sound.duration)+ " User:" + sound.username+ " Tags:" + str(sound.tags);
        strBano += "\n"
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username,description,tags")

print("Bathroom Appliance Class Finished Downloading")
file = open('Bathroom.txt', "a")
file.write(strBano)
file.close()

strOffice = ""
OfficeApp = ["office","keyboard","printer","Light Switch Office"]
for x in OfficeApp:
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username,description,tags")
    for sound in page:
        time.sleep(delay)
        sound.retrieve_preview(".",sound.name+".wav")
        strOffice += "Sound Name:" + sound.name + " Duration:" + str(sound.duration)+ " User:" + sound.username+ " Tags:" + str(sound.tags);
        strOffice += "\n"
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username,description,tags")

print("Office Appliance Class Finished Downloading")
file = open('Office.txt', "a")
file.write(strOffice)
file.close()


strbedRm = ""
bedRmApp = ["bed"]
for x in bedRmApp:
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username,description,tags")
    for sound in page:
        time.sleep(delay)
        sound.retrieve_preview(".",sound.name+".wav")
        strbedRm += "Sound Name:" + sound.name + " Duration:" + str(sound.duration)+ " User:" + sound.username+ " Tags:" + str(sound.tags);
        strbedRm += "\n"
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username,description,tags")


print("Bedroom Appliance Class Finished Downloading")
file = open('Bedroom.txt', "a")
file.write(strbedRm)
file.close()



strFurn = ""
FurnArr = ["furniture","carpet","closet","cabinet","chair"]
for x in FurnArr:
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username,description,tags")
    for sound in page:
        time.sleep(delay)
        sound.retrieve_preview(".",sound.name+".wav")
        strFurn += "Sound Name:" + sound.name + " Duration:" + str(sound.duration)+ " User:" + sound.username+ " Tags:" + str(sound.tags);
        strFurn += "\n"
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username,description,tags")

print("Furniture Class Finished Downloading")
file = open('Furniture.txt', "a")
file.write(strFurn)
file.close()

strInstruments = ""
InsArr = ["guitar","piano","violin","drums","saxophone","flute"]
for x in InsArr:
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username,description,tags")
    for sound in page:
        time.sleep(delay)
        sound.retrieve_preview(".",sound.name+".wav")
        strInstruments += "Sound Name:" + sound.name + " Duration:" + str(sound.duration)+ " User:" + sound.username+ " Tags:" + str(sound.tags);
        strInstruments += "\n"
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username,description,tags")

print("Instrument Class Finished Downloading")
file = open('Instrument.txt', "a")
file.write(strInstruments)
file.close()


strofNoti = ""
results9 = client.text_search(query="notifications",fields="id,name,previews,duration,description,username,tags,analysis")
print()
for sound in results9:
    sound.retrieve_preview(".",sound.name+".wav")
    strofNoti += "Sound Name:" + sound.name + " Duration:" + str(sound.duration)+ " User:" + sound.username+ " Tags:" + str(sound.tags);
    strofNoti += "\n"

file = open('Notifications.txt', "a")
file.write(strofNoti)
file.close()
