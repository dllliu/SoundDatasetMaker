from __future__ import print_function
import freesound
import os
import sys


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

results = client.text_search(query="human voices",fields="id,name,previews,duration")

strOfVoices = "";

for sound in results:
    sound.retrieve_preview(".",sound.name+".mp3")
    strOfVoices += "Sound Name:" + sound.name + " Duration:" + str(sound.duration)
    strOfVoices += "\n"
file = open('voices.txt', "a")
file.write(strOfVoices)
file.close()



print()
strOfMvmnt = "";

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

strOfhyg = "";
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
strOfntr = "";
print()
for sound in results4:
    sound.retrieve_preview(".",sound.name+".mp3")
    strOfntr += "Sound Name:" + sound.name + " Duration:" + str(sound.duration)
    strOfntr += "\n"

file = open('elements.txt', "a")
file.write(strOfntr)
file.close()

strOfanm = "";
results5 = client.text_search(query="urban animals",fields="id,name,previews,duration")
print()
for sound in results5:
    sound.retrieve_preview(".",sound.name+".mp3")
    strOfanm += "Sound Name:" + sound.name + " Duration:" + str(sound.duration)
    strOfanm += "\n"

file = open('animals.txt', "a")
file.write(strOfanm)
file.close()
"""
