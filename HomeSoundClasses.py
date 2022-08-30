from __future__ import print_function
import freesound
import os
import sys
import time
import csv
import numpy as np

api_key = os.getenv('FREESOUND_API_KEY', "BLkaRWL7Vr8nl6K2yvzDw3q3SKKYiuMlclJU7ECy")
client_secret = "BLkaRWL7Vr8nl6K2yvzDw3q3SKKYiuMlclJU7ECy"
client_id = "uPkz0WfINfbiy8r7exNy"
token = client_secret

delay = 2;

client = freesound.FreesoundClient()
client.set_token(token,"token")
#Voice Class

DataOuptut=[]

TARGETITEMCOUNT=50

TotalItemCount=0

finished=False
page = client.text_search(query="talking",fields="id,name,previews,duration,username,tags,description,geotag,license,url")
nextPage = page
while nextPage!=None:
    for sound in page:
        if "\\" in sound.name:
            continue
        tags = str(sound.tags)
        New_Tags = tags.replace(",","+")
        rowDictionary={
            "name":sound.name,
            "url":sound.url,
            "tags":New_Tags,
            "username":sound.username,
            "license":sound.license,
            "description":sound.description,
            "duration":str(sound.duration),
            "geotags":sound.geotag
        }
        sound.retrieve_preview(".",sound.name)
        DataOuptut.append(rowDictionary)
        TotalItemCount+=1
        if(TotalItemCount>=TARGETITEMCOUNT):
            finished=True
    if(finished):
        break
    nextPage = page.next_page()

print("Download of Human Voice Class Completed")

def reset():
    TotalItemCount=0
    finished=False
return None

reset()
TARGETITEMCOUNT=20

mvmnt_arr = ["home walking","house eating","setting table","washing dishes","cutting food"]
for x in mvmnt_arr:
    page = client.text_search(query=x,fields="id,name,previews,duration,username,tags,description,geotag,license,url")
    nextPage = page
    while nextPage!=None:
        for sound in page:
            if "\\" in sound.name:
                continue
            tags = str(sound.tags)
            New_Tags = tags.replace(",","+")
            rowDictionary={
            "name":sound.name,
            "url":sound.url,
            "tags":New_Tags,
            "username":sound.username,
            "license":sound.license,
            "description":sound.description,
            "duration":str(sound.duration),
            "geotags":sound.geotag
            }
            sound.retrieve_preview(".",sound.name)
            DataOuptut.append(rowDictionary)
            TotalItemCount+=1
            if(TotalItemCount>=TARGETITEMCOUNT):
                finished=True
        if(finished):
            break
        nextPage = page.next_page()


reset()
items_arr = ["box moving","coins","match","keys","velcro","zippers,","box moving"]
TARGETITEMCOUNT=int(100/items_arr.length)

for x in items_arr:
    page = client.text_search(query=x,fields="id,name,previews,duration,username,tags,description,geotag,license,url")
    nextPage = page
    while nextPage!=None:
        for sound in page:
            if "\\" in sound.name:
                continue
            tags = str(sound.tags)
            New_Tags = tags.replace(",","+")
            rowDictionary={
            "name":sound.name,
            "url":sound.url,
            "tags":New_Tags,
            "username":sound.username,
            "license":sound.license,
            "description":sound.description,
            "duration":str(sound.duration),
            "geotags":sound.geotag
            }
            sound.retrieve_preview(".",sound.name)
            DataOuptut.append(rowDictionary)
            TotalItemCount+=1
            if(TotalItemCount>=TARGETITEMCOUNT):
                finished=True
        if(finished):
            break
        nextPage = page.next_page()

reset()
bev_arr = ["ice cubes","beverage"]
TARGETITEMCOUNT=int(100/bev_arr.length)

for x in bev_arr:
    page = client.text_search(query=x,fields="id,name,previews,duration,username,tags,description,geotag,license,url")
    nextPage = page
    while nextPage!=None:
        for sound in page:
            if "\\" in sound.name:
                continue
            tags = str(sound.tags)
            New_Tags = tags.replace(",","+")
            rowDictionary={
            "name":sound.name,
            "url":sound.url,
            "tags":New_Tags,
            "username":sound.username,
            "license":sound.license,
            "description":sound.description,
            "duration":str(sound.duration),
            "geotags":sound.geotag
            }
            sound.retrieve_preview(".",sound.name)
            DataOuptut.append(rowDictionary)
            TotalItemCount+=1
            if(TotalItemCount>=TARGETITEMCOUNT):
                finished=True
        if(finished):
            break
        nextPage = page.next_page()

print("Movement Class Downloaded")

reset()
Hyg_arr = ["hygiene","vaccum","shaving","cleaning home","brushing teeth","washing clothes"]
TARGETITEMCOUNT=int(100/Hyg_arr.length)

for x in Hyg_arr:
    page = client.text_search(query=x,fields="id,name,previews,duration,username,tags,description,geotag,license,url")
    nextPage = page
    while nextPage!=None:
        for sound in page:
            if "\\" in sound.name:
                continue
            tags = str(sound.tags)
            New_Tags = tags.replace(",","+")
            rowDictionary={
            "name":sound.name,
            "url":sound.url,
            "tags":New_Tags,
            "username":sound.username,
            "license":sound.license,
            "description":sound.description,
            "duration":str(sound.duration),
            "geotags":sound.geotag
            }
            sound.retrieve_preview(".",sound.name)
            DataOuptut.append(rowDictionary)
            TotalItemCount+=1
            if(TotalItemCount>=TARGETITEMCOUNT):
                finished=True
        if(finished):
            break
        nextPage = page.next_page()

reset()
ntitems_arr = ["weather","hail","thunder"]
TARGETITEMCOUNT=int(100/ntitems_arr.length)
for x in Hyg_arr:
    page = client.text_search(query=x,fields="id,name,previews,duration,username,tags,description,geotag,license,url")
    nextPage = page
    while nextPage!=None:
        for sound in page:
            if "\\" in sound.name:
                continue
            tags = str(sound.tags)
            New_Tags = tags.replace(",","+")
            rowDictionary={
            "name":sound.name,
            "url":sound.url,
            "tags":New_Tags,
            "username":sound.username,
            "license":sound.license,
            "description":sound.description,
            "duration":str(sound.duration),
            "geotags":sound.geotag
            }
            sound.retrieve_preview(".",sound.name)
            DataOuptut.append(rowDictionary)
            TotalItemCount+=1
            if(TotalItemCount>=TARGETITEMCOUNT):
                finished=True
        if(finished):
            break
        nextPage = page.next_page()

print("Nature Class Downloaded")

reset()
anm_arr = ["bark","mews","tweet"]
TARGETITEMCOUNT=int(100/anm_arr.length)
for x in anm_arr:
    page = client.text_search(query=x,fields="id,name,previews,duration,username,tags,description,geotag,license,url")
    nextPage = page
    while nextPage!=None:
        for sound in page:
            if "\\" in sound.name:
                continue
            tags = str(sound.tags)
            New_Tags = tags.replace(",","+")
            rowDictionary={
            "name":sound.name,
            "url":sound.url,
            "tags":New_Tags,
            "username":sound.username,
            "license":sound.license,
            "description":sound.description,
            "duration":str(sound.duration),
            "geotags":sound.geotag
            }
            sound.retrieve_preview(".",sound.name)
            DataOuptut.append(rowDictionary)
            TotalItemCount+=1
            if(TotalItemCount>=TARGETITEMCOUNT):
                finished=True
        if(finished):
            break
        nextPage = page.next_page()
#-----------------------------------

reset()
PAplc_arr = ["cell phone","camera","computer"]
TARGETITEMCOUNT=int(100/PAplc.length)
for x in anm_arr:
    page = client.text_search(query=x,fields="id,name,previews,duration,username,tags,description,geotag,license,url")
    nextPage = page
    while nextPage!=None:
        for sound in page:
            if "\\" in sound.name:
                continue
            tags = str(sound.tags)
            New_Tags = tags.replace(",","+")
            rowDictionary={
            "name":sound.name,
            "url":sound.url,
            "tags":New_Tags,
            "username":sound.username,
            "license":sound.license,
            "description":sound.description,
            "duration":str(sound.duration),
            "geotags":sound.geotag
            }
            sound.retrieve_preview(".",sound.name)
            DataOuptut.append(rowDictionary)
            TotalItemCount+=1
            if(TotalItemCount>=TARGETITEMCOUNT):
                finished=True
        if(finished):
            break
        nextPage = page.next_page()

print("Personal Appliance Class Finished Downloading")

reset()
KitAppArr = ["kitchen appliances","oven","blender","garbage disposal","stove","toaster","furnace"]
TARGETITEMCOUNT=int(100/KitAppArr.length)
for x in KitAppArr_arr:
    page = client.text_search(query=x,fields="id,name,previews,duration,username,tags,description,geotag,license,url")
    nextPage = page
    while nextPage!=None:
        for sound in page:
            if "\\" in sound.name:
                continue
            tags = str(sound.tags)
            New_Tags = tags.replace(",","+")
            rowDictionary={
            "name":sound.name,
            "url":sound.url,
            "tags":New_Tags,
            "username":sound.username,
            "license":sound.license,
            "description":sound.description,
            "duration":str(sound.duration),
            "geotags":sound.geotag
            }
            sound.retrieve_preview(".",sound.name)
            DataOuptut.append(rowDictionary)
            TotalItemCount+=1
            if(TotalItemCount>=TARGETITEMCOUNT):
                finished=True
        if(finished):
            break
        nextPage = page.next_page()

print("Kitchen Appliance Class Finished Downloading")

reset()
LivApp = ["Sofa","TV","Fan","Light Switch","Blinds"]
TARGETITEMCOUNT=int(100/LivApp.length)

for x in LivApp:
    page = client.text_search(query=x,fields="id,name,previews,duration,username,tags,description,geotag,license,url")
    nextPage = page
    while nextPage!=None:
        for sound in page:
            if "\\" in sound.name:
                continue
            tags = str(sound.tags)
            New_Tags = tags.replace(",","+")
            rowDictionary={
            "name":sound.name,
            "url":sound.url,
            "tags":New_Tags,
            "username":sound.username,
            "license":sound.license,
            "description":sound.description,
            "duration":str(sound.duration),
            "geotags":sound.geotag
            }
            sound.retrieve_preview(".",sound.name)
            DataOuptut.append(rowDictionary)
            TotalItemCount+=1
            if(TotalItemCount>=TARGETITEMCOUNT):
                finished=True
        if(finished):
            break
        nextPage = page.next_page()

print("Living Room Appliance Class Finished Downloading")

reset()
BanoApp = ["bathroom","ventilator","hair dryer","soap dispenser"]
TARGETITEMCOUNT=int(100/BanoApp.length)

for x in LivApp:
    page = client.text_search(query=x,fields="id,name,previews,duration,username,tags,description,geotag,license,url")
    nextPage = page
    while nextPage!=None:
        for sound in page:
            if "\\" in sound.name:
                continue
            tags = str(sound.tags)
            New_Tags = tags.replace(",","+")
            rowDictionary={
            "name":sound.name,
            "url":sound.url,
            "tags":New_Tags,
            "username":sound.username,
            "license":sound.license,
            "description":sound.description,
            "duration":str(sound.duration),
            "geotags":sound.geotag
            }
            sound.retrieve_preview(".",sound.name)
            DataOuptut.append(rowDictionary)
            TotalItemCount+=1
            if(TotalItemCount>=TARGETITEMCOUNT):
                finished=True
        if(finished):
            break
        nextPage = page.next_page()

print("Bathroom Appliance Class Finished Downloading")


reset()
OfficeApp = ["office","keyboard","printer","Light Switch Office"]
TARGETITEMCOUNT=int(100/OfficeApp.length)

for x in OfficeApp:
    page = client.text_search(query=x,fields="id,name,previews,duration,username,tags,description,geotag,license,url")
    nextPage = page
    while nextPage!=None:
        for sound in page:
            if "\\" in sound.name:
                continue
            tags = str(sound.tags)
            New_Tags = tags.replace(",","+")
            rowDictionary={
            "name":sound.name,
            "url":sound.url,
            "tags":New_Tags,
            "username":sound.username,
            "license":sound.license,
            "description":sound.description,
            "duration":str(sound.duration),
            "geotags":sound.geotag
            }
            sound.retrieve_preview(".",sound.name)
            DataOuptut.append(rowDictionary)
            TotalItemCount+=1
            if(TotalItemCount>=TARGETITEMCOUNT):
                finished=True
        if(finished):
            break
        nextPage = page.next_page()


reset()
TARGETITEMCOUNT=50
page = client.text_search(query="bed",fields="id,name,previews,duration,username,tags,description,geotag,license,url")
nextPage = page
while nextPage!=None:
    for sound in page:
        if "\\" in sound.name:
            continue
        tags = str(sound.tags)
        New_Tags = tags.replace(",","+")
        rowDictionary={
        "name":sound.name,
        "url":sound.url,
        "tags":New_Tags,
        "username":sound.username,
        "license":sound.license,
        "description":sound.description,
        "duration":str(sound.duration),
        "geotags":sound.geotag
        }
        sound.retrieve_preview(".",sound.name)
        DataOuptut.append(rowDictionary)
        TotalItemCount+=1
        if(TotalItemCount>=TARGETITEMCOUNT):
            finished=True
    if(finished):
        break
    nextPage = page.next_page()


print("Bedroom Appliance Class Finished Downloading")


reset()
FurnArr = ["furniture","carpet","closet","cabinet","chair"]
TARGETITEMCOUNT=int(100/FurnArr.length)

for x in FurnArr:
    page = client.text_search(query=x,fields="id,name,previews,duration,username,tags,description,geotag,license,url")
    nextPage = page
    while nextPage!=None:
        for sound in page:
            if "\\" in sound.name:
                continue
            tags = str(sound.tags)
            New_Tags = tags.replace(",","+")
            rowDictionary={
            "name":sound.name,
            "url":sound.url,
            "tags":New_Tags,
            "username":sound.username,
            "license":sound.license,
            "description":sound.description,
            "duration":str(sound.duration),
            "geotags":sound.geotag
            }
            sound.retrieve_preview(".",sound.name)
            DataOuptut.append(rowDictionary)
            TotalItemCount+=1
            if(TotalItemCount>=TARGETITEMCOUNT):
                finished=True
        if(finished):
            break
        nextPage = page.next_page()

print("Furniture Class Finished Downloading")

reset()
InsArr = ["guitar","piano","violin","drums","saxophone","flute"]
TARGETITEMCOUNT=int(100/InsArr.length)

for x in InsArr:
    page = client.text_search(query=x,fields="id,name,previews,duration,username,tags,description,geotag,license,url")
    nextPage = page
    while nextPage!=None:
        for sound in page:
            if "\\" in sound.name:
                continue
            tags = str(sound.tags)
            New_Tags = tags.replace(",","+")
            rowDictionary={
            "name":sound.name,
            "url":sound.url,
            "tags":New_Tags,
            "username":sound.username,
            "license":sound.license,
            "description":sound.description,
            "duration":str(sound.duration),
            "geotags":sound.geotag
            }
            sound.retrieve_preview(".",sound.name)
            DataOuptut.append(rowDictionary)
            TotalItemCount+=1
            if(TotalItemCount>=TARGETITEMCOUNT):
                finished=True
        if(finished):
            break
        nextPage = page.next_page()

print("Instrument Class Finished Downloading")
print("Finished Downloads!!!!!!!!")

with open('voices.csv', 'w') as csvfile:
    fieldnames = DataOuptut[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames,delimiter=',')
    writer.writeheader()
    for row in DataOuptut:
        writer.writerow(row);
