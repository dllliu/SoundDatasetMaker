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
voices_arr = ["people talking home"]
for x in voices_arr:
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username,description")
    for sound in page:
        time.sleep(delay)
        sound.retrieve_preview(".",sound.name+".mp3")
        strOfVoices += "Sound Name:" + sound.name + " Duration:" + str(sound.duration)+ " User:" + sound.username + " Description:" + sound.description;
        strOfVoices  += "\n"
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username,description")

print("Download of Human Voice Class Completed")
with open('voices.txt', "a") as file:
    file.write(strOfVoices)


#Beginning of Movement class

strOfMvmnt = ""

mvmnt_arr = ["beverages","home walking","house eating","setting table","washing dishes", "cutting food"]
for x in mvmnt_arr:
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username,description")
    for sound in page:
        time.sleep(delay)
        sound.retrieve_preview(".",sound.name+".mp3")
        strOfMvmnt += "Sound Name:" + sound.name + " Duration:" + str(sound.duration)+ " User:" + sound.username+ " Description:" + sound.description;
        strOfMvmnt  += "\n"
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username,description")

resultsItems = client.text_search(query="household items",fields="id,name,previews,duration,analysis,username,description")

for sound in resultsItems:
    sound.retrieve_preview(".",sound.name+".mp3")
    strOfMvmnt += "Sound Name:" + sound.name + " Duration:" + str(sound.duration)+ " User:" + sound.username+ " Description:" + sound.description;
    strOfMvmnt  += "\n"

resultsPG2 = resultsItems.next_page();
for sound in resultsPG2:
    sound.retrieve_preview(".",sound.name+".mp3")
    strOfMvmnt += "Sound Name:" + sound.name + " Duration:" + str(sound.duration)+ " User:" + sound.username+ " Description:" + sound.description;
    strOfMvmnt  += "\n"

print("Movement Class Downloaded")
file = open('movement.txt', "a")
file.write(strOfMvmnt)
file.close()

#Hygiene CLass
strOfhyg = ""
Hyg_arr = ["hygiene","vaccum","shaving","cleaning home","brushing teeth","washing clothes"]
for x in Hyg_arr:
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username,description")
    for sound in page:
        time.sleep(delay)
        sound.retrieve_preview(".",sound.name+".mp3")
        strOfhyg += "Sound Name:" + sound.name + " Duration:" + str(sound.duration)+ " User:" + sound.username+ " Description:" + sound.description;
        strOfhyg  += "\n"
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username,description")

print("Hygiene Class Downloaded")
file = open('hygiene.txt', "a")
file.write(strOfhyg)
file.close()

#Nature Class
strOfntr = ""
ntr_arr = ["weather","hail","thunder"]
for x in ntr_arr:
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username,description")
    for sound in page:
        time.sleep(delay)
        sound.retrieve_preview(".",sound.name+".mp3")
        strOfntr += "Sound Name:" + sound.name + " Duration:" + str(sound.duration)+ " User:" + sound.username+ " Description:" + sound.description;
        strOfntr  += "\n"
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username,description")

print("Nature Class Downloaded")
file = open('elements.txt', "a")
file.write(strOfntr)
file.close()

strOfanm = ""
anm_arr = ["bark","mews","tweet"]
for x in anm_arr:
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username,description")
    for sound in page:
        time.sleep(delay)
        sound.retrieve_preview(".",sound.name+".mp3")
        strOfanm += "Sound Name:" + sound.name + " Duration:" + str(sound.duration)+ " User:" + sound.username+ " Description:" + sound.description;
        strOfanm += "\n"
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username,description")

print("Animal Class Finished Downloading")
file = open('animals.txt', "a")
file.write(strOfanm)
file.close()

strofPAplc = ""
PAplc_arr = ["cell phone","camera","computer"]
for x in PAplc_arr:
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username,description")
    for sound in page:
        time.sleep(delay)
        sound.retrieve_preview(".",sound.name+".mp3")
        strofPAplc += "Sound Name:" + sound.name + " Duration:" + str(sound.duration)+ " User:" + sound.username+ " Description:" + sound.description;
        strofPAplc += "\n"
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username,description")

print("Personal Appliance Class Finished Downloading")
file = open('PersonalAppliances.txt', "a")
file.write(strofPAplc)
file.close()

strKitApp = ""
KitAppArr = ["kitchen appliances","oven","blender","garbage disposal","stove","toaster","furnace"]

for x in KitAppArr:
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username,description")
    for sound in page:
        time.sleep(delay)
        sound.retrieve_preview(".",sound.name+".mp3")
        strKitApp += "Sound Name:" + sound.name + " Duration:" + str(sound.duration)+ " User:" + sound.username+ " Description:" + sound.description;
        strKitApp += "\n"
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username,description")

print("Kitchen Appliance Class Finished Downloading")
file = open('Kitchen.txt', "a")
file.write(strKitApp)
file.close()

strLiv = ""
LivApp = ["Sofa","TV","Fan","Light Switch","Blinds"]

for x in LivApp:
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username,description")
    for sound in page:
        time.sleep(delay)
        sound.retrieve_preview(".",sound.name+".mp3")
        strLiv += "Sound Name:" + sound.name + " Duration:" + str(sound.duration)+ " User:" + sound.username+ " Description:" + sound.description;
        strLiv += "\n"
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username,description")

print("Living Room Appliance Class Finished Downloading")
file = open('LivingRoom.txt', "a")
file.write(strLiv)
file.close()

strBano = ""
BanoApp = ["bathroom","ventilator","hair dryer","soap dispenser"]

for x in BanoApp:
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username,description")
    for sound in page:
        time.sleep(delay)
        sound.retrieve_preview(".",sound.name+".mp3")
        strBano += "Sound Name:" + sound.name + " Duration:" + str(sound.duration)+ " User:" + sound.username+ " Description:" + sound.description;
        strBano += "\n"
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username,description")

print("Bathroom Appliance Class Finished Downloading")
file = open('Bathroom.txt', "a")
file.write(strBano)
file.close()

strOffice = ""
OfficeApp = ["office","keyboard","clock","printer","coffee grinder","Air Conditioner","Fan","Light Switch Office"]
for x in OfficeApp:
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username,description")
    for sound in page:
        time.sleep(delay)
        sound.retrieve_preview(".",sound.name+".mp3")
        strOffice += "Sound Name:" + sound.name + " Duration:" + str(sound.duration)+ " User:" + sound.username+ " Description:" + sound.description;
        strOffice += "\n"
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username,description")

print("Office Appliance Class Finished Downloading")
file = open('Office.txt', "a")
file.write(strOffice)
file.close()

strbedRm = ""
bedRmApp = ["bedroom","fan","drawers","lamp","smoke alarm","bells","lock"]
for x in bedRmApp:
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username,description")
    for sound in page:
        time.sleep(delay)
        sound.retrieve_preview(".",sound.name+".mp3")
        strbedRm += "Sound Name:" + sound.name + " Duration:" + str(sound.duration)+ " User:" + sound.username+ " Description:" + sound.description;
        strbedRm += "\n"
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username,description")

print("Bedroom Appliance Class Finished Downloading")
file = open('Bedroom.txt', "a")
file.write(strbedRm)
file.close()

strFurn = ""
FurnArr = ["sofa","furniture","door","carpet","cabinet","closet","curtains","chair","fireplace"]
for x in FurnArr:
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username,description")
    for sound in page:
        time.sleep(delay)
        sound.retrieve_preview(".",sound.name+".mp3")
        strFurn += "Sound Name:" + sound.name + " Duration:" + str(sound.duration)+ " User:" + sound.username+ " Description:" + sound.description;
        strFurn += "\n"
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username,description")

print("Furniture Class Finished Downloading")
file = open('Furniture.txt', "a")
file.write(strFurn)
file.close()

strInstruments = ""
InsArr = ["guitar","piano","flute","trumpet","trombone","drum"]
for x in InsArr:
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username,description")
    for sound in page:
        time.sleep(delay)
        sound.retrieve_preview(".",sound.name+".mp3")
        strInstruments += "Sound Name:" + sound.name + " Duration:" + str(sound.duration)+ " User:" + sound.username+ " Description:" + sound.description;
        strInstruments += "\n"
    page = client.text_search(query=x,fields="id,name,previews,duration,analysis,username,description")

print("Instrument Class Finished Downloading")
file = open('Instrument.txt', "a")
file.write(strInstruments)
file.close()


strofMusic = ""
results8 = client.text_search(query="instruments",fields="id,name,previews,duration,description")
print()
for sound in results8:
    sound.retrieve_preview(".",sound.name+".mp3")
    strofMusic += "Sound Name:" + sound.name + " Duration:" + str(sound.duration)+ " User:" + sound.username+ " Description:" + sound.description;
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
    strofNoti += "Sound Name:" + sound.name + " Duration:" + str(sound.duration)+ " User:" + sound.username+ " Description:" + sound.description;
    strofNoti += "\n"

file = open('Notifications.txt', "a")
file.write(strofNoti)
file.close()
