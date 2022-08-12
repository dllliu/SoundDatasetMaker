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

client = freesound.FreesoundClient()
client.set_token(token,"token")

results = client.text_search(query="human voices",fields="id,name,previews,duration,analysis")

strOfVoices = "";

for sound in results:
    sound.retrieve_preview(".",sound.name+".mp3")
    strOfVoices += "Sound Name:" + sound.name + " Duration:" + str(sound.duration)
    strOfVoices += "\n"

resultsP2 = results.next_page();
    for sound in resultsP2:
        sound.retrieve_preview(".",sound.name+".mp3")
        strOfVoices += "Sound Name:" + sound.name + " Duration:" + str(sound.duration)
        strOfVoices += "\n"

resultsP3 = resultsP2.next_page();
    for sound in resultsP3:
        sound.retrieve_preview(".",sound.name+".mp3")
        strOfVoices += "Sound Name:" + sound.name + " Duration:" + str(sound.duration)
        strOfVoices += "\n"

resultsP4 = resultsP3.next_page();
    for sound in resultsP4:
        sound.retrieve_preview(".",sound.name+".mp3")
        strOfVoices += "Sound Name:" + sound.name + " Duration:" + str(sound.duration)
        strOfVoices += "\n"

file = open('voices.txt', "a")
file.write(strOfVoices)
file.close()

print()

"""
strOfMvmnt = ""

results1 = client.text_search(query="beverages",fields="id,name,previews,duration")
for sound in results1:
    sound.retrieve_preview(".",sound.name+".mp3")
    strOfMvmnt+= "Sound Name:" + sound.name + " Duration:" + str(sound.duration)
    strOfMvmnt += "\n"

rsults2 = client.text_search(query="household actions",fields="id,name,previews,duration")
print()
for sound in rsults2:
    sound.retrieve_preview(".",sound.name+".mp3")
    strOfMvmnt += "Sound Name:" + sound.name + " Duration:" + str(sound.duration)
    strOfMvmnt += "\n"

results2 = client.text_search(query="household items",fields="id,name,previews,duration")
print()
for sound in results2:
    sound.retrieve_preview(".",sound.name+".mp3")
    strOfMvmnt += "Sound Name:" + sound.name + " Duration:" + str(sound.duration)
    strOfMvmnt += "\n"

file = open('movement.txt', "a")
file.write(strOfMvmnt)
file.close()

strOfhyg = ""
results3 = client.text_search(query="hygiene",fields="id,name,previews,duration")
print()
for sound in results3:
    sound.retrieve_preview(".",sound.name+".mp3")
    strOfhyg += "Sound Name:" + sound.name + " Duration:" + str(sound.duration)
    strOfhyg += "\n"

file = open('hygiene.txt', "a")
file.write(strOfhyg)
file.close()

results4 = client.text_search(query="nature elements",fields="id,name,previews,duration")
strOfntr = ""
print()
for sound in results4:
    sound.retrieve_preview(".",sound.name+".mp3")
    strOfntr += "Sound Name:" + sound.name + " Duration:" + str(sound.duration)
    strOfntr += "\n"

file = open('elements.txt', "a")
file.write(strOfntr)
file.close()

strOfanm = ""
results5 = client.text_search(query="urban animals",fields="id,name,previews,duration")
print()
for sound in results5:
    sound.retrieve_preview(".",sound.name+".mp3")
    strOfanm += "Sound Name:" + sound.name + " Duration:" + str(sound.duration)
    strOfanm += "\n"

file = open('animals.txt', "a")
file.write(strOfanm)
file.close()

strofApp = ""
results6 = client.text_search(query="urban animals",fields="id,name,previews,duration")
print()
for sound in results6:
    sound.retrieve_preview(".",sound.name+".mp3")
    strOfApp += "Sound Name:" + sound.name + " Duration:" + str(sound.duration)
    strOfApp += "\n"

file = open('Appliances.txt', "a")
file.write(strOfApp)
file.close()

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
"""
