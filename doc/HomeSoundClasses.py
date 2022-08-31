from __future__ import print_function
import freesound
import os
import sys
import time
import csv
import numpy as np
from uuid import uuid4

api_key = os.getenv('FREESOUND_API_KEY', "BLkaRWL7Vr8nl6K2yvzDw3q3SKKYiuMlclJU7ECy")
client_secret = "BLkaRWL7Vr8nl6K2yvzDw3q3SKKYiuMlclJU7ECy"
client_id = "uPkz0WfINfbiy8r7exNy"
token = client_secret

delay = 2;

client = freesound.FreesoundClient()
client.set_token(token,"token")
#Voice Class

DataOuptut=[]

TARGETITEMCOUNT=60

TotalItemCount=0

finished = False

def setTarget(target):
    global TARGETITEMCOUNT
    TARGETITEMCOUNT = target

def setTotal(total):
    global TotalItemCount
    TotalItemCount = total

def setFinished(completed):
    global finished
    finished = completed

def getFinished():
    global finished
    return finished

def IncrementTarget():
    global TARGETITEMCOUNT
    TARGETITEMCOUNT += 1

def IncrementTotal():
    global TotalItemCount
    TotalItemCount += 1


def DownloadDictOfSoundResults(arr,target):
    for x in arr:
        page = client.text_search(query=x,fields="id,name,previews,duration,username,tags,description,geotag,license,url")
        for sound in page:
            if "\\" in sound.name or sound.duration <= 5:
                continue
            tags = str(sound.tags)
            New_Tags = tags.replace(",","+")
            uuid = uuid4()
            rowDictionary={
            "name":sound.name,
            "url":sound.url,
            "uuid":uuid,
            "tags":New_Tags,
            "username":sound.username,
            "license":sound.license,
            "description":sound.description,
            "duration":str(sound.duration),
            "geotags":sound.geotag
            }
            sound.retrieve_preview(".",str(uuid)+".wav")
            DataOuptut.append(rowDictionary)
            IncrementTotal()
            print(TotalItemCount,sound.name)

        if page.next_page() != None:
            nextPage = page.next_page()
        while nextPage!=None:
            for sound in nextPage:
                if "\\" in sound.name or sound.duration <= 5:
                    continue
                tags = str(sound.tags)
                New_Tags = tags.replace(",","+")
                uuid = uuid4()
                rowDictionary={
                "name":sound.name,
                "url":sound.url,
                "uuid":uuid,
                "tags":New_Tags,
                "username":sound.username,
                "license":sound.license,
                "description":sound.description,
                "duration":str(sound.duration),
                "geotags":sound.geotag
                }
                sound.retrieve_preview(".",str(uuid)+".wav")
                DataOuptut.append(rowDictionary)
                IncrementTotal()
                print(TotalItemCount,sound.name)
                if(TotalItemCount>=target):
                    setFinished(True)
            if(getFinished()):
                break
            nextPage = nextPage.next_page()

voice_arr = ["talking"]
DownloadDictOfSoundResults(voice_arr,60)
print("Download of Human Voice Class Completed")
with open('Voices.csv', 'w') as csvfile:
    fieldnames = DataOuptut[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames,delimiter=',')
    writer.writeheader()
    for row in DataOuptut:
        writer.writerow(row);

setFinished(False)
setTotal(0)
bev_arr = ["ice cubes","beverage"]
targetEachEntry=int(100/len(bev_arr))
DownloadDictOfSoundResults(bev_arr,targetEachEntry)
with open('Beverages.csv', 'w') as csvfile:
    fieldnames = DataOuptut[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames,delimiter=',')
    writer.writeheader()
    for row in DataOuptut:
        writer.writerow(row);
print("Final Phase 3 of Movement Done")

setFinished(False)
setTotal(0)
mvmnt_arr = ["home walking","house eating","clapping","kids fighting home","home movement"]
try:
    DownloadDictOfSoundResults(mvmnt_arr,int(100/mvmnt_arr.length))
except ValueError:
    print("next page is not accessible")
finally:
    with open('Actions.csv', 'w') as csvfile:
        fieldnames = DataOuptut[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,delimiter=',')
        writer.writeheader()
        for row in DataOuptut:
            writer.writerow(row);

print("Phase 1 of Movement Done")



setFinished(False)
setTotal(0)
items_arr = ["box moving","coins","plastic bags","keys","velcro","zippers,"]
targetEachEntry=int(100/len(items_arr))
try:
    DownloadDictOfSoundResults(items_arr,targetEachEntry)
except ValueError:
    print("next page is not accessible")
finally:
    with open('EverydayItems.csv', 'w') as csvfile:
        fieldnames = DataOuptut[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,delimiter=',')
        writer.writeheader()
        for row in DataOuptut:
            writer.writerow(row);

print("Phase 2 of Movement Done")


setFinished(False)
setTotal(0)
bev_arr = ["ice cubes","beverage"]
targetEachEntry=int(100/len(bev_arr))
DownloadDictOfSoundResults(bev_arr,targetEachEntry)
with open('Beverages.csv', 'w') as csvfile:
    fieldnames = DataOuptut[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames,delimiter=',')
    writer.writeheader()
    for row in DataOuptut:
        writer.writerow(row);
print("Final Phase 3 of Movement Done")




setFinished(False)
setTotal(0)
Hyg_arr = ["hygiene","vaccum","shaving","cleaning home","washing clothes"]
DownloadDictOfSoundResults(Hyg_arr,15)
with open('Hygiene.csv', 'w', encoding="utf-8") as csvfile:
    fieldnames = DataOuptut[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames,delimiter=',')
    writer.writeheader()
    for row in DataOuptut:
        writer.writerow(row);


setFinished(False)
setTotal(0)
nature_arr = ["weather","home rain","thunder"]
targetEachEntry=int(100/len(nature_arr))
DownloadDictOfSoundResults(nature_arr,targetEachEntry)
with open('Nature.csv', 'w', encoding="utf-8") as csvfile:
    fieldnames = DataOuptut[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames,delimiter=',')
    writer.writeheader()
    for row in DataOuptut:
        writer.writerow(row);

print("Nature Class Downloaded")

setFinished(False)
setTotal(0)
anm_arr = ["bark","mews","tweet"]
targetEachEntry=int(100/len(anm_arr))
DownloadDictOfSoundResults(anm_arr,targetEachEntry)
with open('Animals.csv', 'w', encoding="utf-8") as csvfile:
    fieldnames = DataOuptut[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames,delimiter=',')
    writer.writeheader()
    for row in DataOuptut:
        writer.writerow(row);

setFinished(False)
setTotal(0)
PersonalAppliances = ["cell phone","camera","computer"]
targetEachEntry=int(100/len(PersonalAppliances))
DownloadDictOfSoundResults(PersonalAppliances,targetEachEntry)
with open('PersonalAppliances.csv', 'w', encoding="utf-8") as csvfile:
    fieldnames = DataOuptut[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames,delimiter=',')
    writer.writeheader()
    for row in DataOuptut:
        writer.writerow(row);

print("Personal Appliance Class Finished Downloading")

setFinished(False)
setTotal(0)
KitchenApp = ["kitchen appliances","oven","blender","garbage disposal","stove","toaster","furnace"]
targetEachEntry=int(100/len(KitchenApp))
DownloadDictOfSoundResults(KitchenApp,targetEachEntry)
with open('Kitchen.csv', 'w', encoding="utf-8") as csvfile:
    fieldnames = DataOuptut[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames,delimiter=',')
    writer.writeheader()
    for row in DataOuptut:
        writer.writerow(row);

print("Kitchen Appliance Class Finished Downloading")

setFinished(False)
setTotal(0)
LivingApp = ["Sofa","TV","Fan","Light Switch","Blinds"]
targetEachEntry=int(100/len(LivingApp))
DownloadDictOfSoundResults(LivingApp,targetEachEntry)
with open('LivingRoom.csv', 'w', encoding="utf-8") as csvfile:
    fieldnames = DataOuptut[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames,delimiter=',')
    writer.writeheader()
    for row in DataOuptut:
        writer.writerow(row);

print("Living Room Appliance Class Finished Downloading")

setFinished(False)
setTotal(0)
Bathroom = ["bathroom","ventilator","hair dryer","soap dispenser"]
targetEachEntry=int(100/len(Bathroom))
DownloadDictOfSoundResults(Bathroom,targetEachEntry)
with open('Bathroom.csv', 'w', encoding="utf-8") as csvfile:
    fieldnames = DataOuptut[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames,delimiter=',')
    writer.writeheader()
    for row in DataOuptut:
        writer.writerow(row);

print("Bathroom Appliance Class Finished Downloading")

setFinished(False)
setTotal(0)
OfficeApp = ["office","keyboard","printer","Light Switch Office"]
targetEachEntry=int(100/len(OfficeApp))
DownloadDictOfSoundResults(OfficeApp,targetEachEntry)
with open('Office.csv', 'w', encoding="utf-8") as csvfile:
    fieldnames = DataOuptut[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames,delimiter=',')
    writer.writeheader()
    for row in DataOuptut:
        writer.writerow(row);


setFinished(False)
setTotal(0)
bed_arr = ["bed","bedroom"]
DownloadDictOfSoundResults(bed_arr,60)
with open('Bedroom.csv', 'w', encoding="utf-8") as csvfile:
    fieldnames = DataOuptut[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames,delimiter=',')
    writer.writeheader()
    for row in DataOuptut:
        writer.writerow(row);

print("Bedroom Appliance Class Finished Downloading")

setFinished(False)
setTotal(0)
FurnArr = ["furniture","carpet","closet","cabinet","chair"]
targetEachEntry=int(100/len(FurnArr))
DownloadDictOfSoundResults(FurnArr,targetEachEntry)
with open('Furniture.csv', 'w', encoding="utf-8") as csvfile:
    fieldnames = DataOuptut[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames,delimiter=',')
    writer.writeheader()
    for row in DataOuptut:
        writer.writerow(row);

print("Furniture Class Finished Downloading")

setFinished(False)
setTotal(0)
InstrumentsArr = ["guitar","piano","violin","drums","saxophone","flute"]
targetEachEntry=int(100/len(InstrumentsArr))
DownloadDictOfSoundResults(InstrumentsArr,targetEachEntry)
with open('Instruments.csv', 'w', encoding="utf-8") as csvfile:
    fieldnames = DataOuptut[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames,delimiter=',')
    writer.writeheader()
    for row in DataOuptut:
        writer.writerow(row);

print("Instrument Class Finished Downloading")
print("Finished Downloads!!!!!!!!")
