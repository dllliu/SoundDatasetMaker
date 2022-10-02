import pandas as pd
import numpy as np
from glob import glob
import librosa
import librosa.display
import os
import soundfile
import random
import ffmpeg

#Alrady Ran to Convert Files

parent_folder = 'AudioData'
all_og_child_directories = os.listdir(parent_folder)

#copy_parent_folder = 'Copy-AudioData'
#all_copy_child_directories = os.listdir(copy_parent_folder)

def ConvertFilesWithFFmpeg(input_dir,output_dir):
    files = os.listdir(input_dir)
    print(files)
    for eachfile in files:
        file_path = os.path.join(input_dir,eachfile)
        input = ffmpeg.input(file_path)
        output = ffmpeg.output(input,os.path.join(output_dir,(str(eachfile[:len(eachfile)-3] +"-.wav"))))
        print(output)
        ffmpeg.run(output)

ConvertFilesWithFFmpeg(os.path.join(parent_folder,'001 - Voices'),os.path.join(copy_parent_folder,'001 - Voices'))
ConvertFilesWithFFmpeg(os.path.join(parent_folder,'002 - Liquids'),os.path.join(copy_parent_folder,'002 - Liquids'))
ConvertFilesWithFFmpeg(os.path.join(parent_folder,'003 - Locomotion'),os.path.join(copy_parent_folder,'003 - Locomotion'))
ConvertFilesWithFFmpeg(os.path.join(parent_folder,'004 - HouseItems'),os.path.join(copy_parent_folder,'004 - HouseItems'))
ConvertFilesWithFFmpeg(os.path.join(parent_folder,'005 - Digestive'),os.path.join(copy_parent_folder,'005 - Digestive'))
ConvertFilesWithFFmpeg(os.path.join(parent_folder,'006 - Hygiene'),os.path.join(copy_parent_folder,'006 - Hygiene'))
ConvertFilesWithFFmpeg(os.path.join(parent_folder,'007 - Elements'),os.path.join(copy_parent_folder,'007 - Elements'))
ConvertFilesWithFFmpeg(os.path.join(parent_folder,'008 - Animals'),os.path.join(copy_parent_folder,'008 - Animals'))
ConvertFilesWithFFmpeg(os.path.join(parent_folder,'009 - Cooking_Appliances'),os.path.join(copy_parent_folder,'009 - Cooking_Appliances'))
ConvertFilesWithFFmpeg(os.path.join(parent_folder,'010 - Cleaning_Appliances'),os.path.join(copy_parent_folder,'010 - Cleaning_Appliances'))
ConvertFilesWithFFmpeg(os.path.join(parent_folder,'011 - Lighting_Appliances'),os.path.join(copy_parent_folder,'011 - Lighting_Appliances'))
ConvertFilesWithFFmpeg(os.path.join(parent_folder,'012 - Ventilation_Appliances'),os.path.join(copy_parent_folder,'012 - Ventilation_Appliances'))
ConvertFilesWithFFmpeg(os.path.join(parent_folder,'013 - Furniture'),os.path.join(copy_parent_folder,'013 - Furniture'))
ConvertFilesWithFFmpeg(os.path.join(parent_folder,'014 - Tools'),os.path.join(copy_parent_folder,'014 - Tools'))
ConvertFilesWithFFmpeg(os.path.join(parent_folder,'015 - Instruments'),os.path.join(copy_parent_folder,'015 - Instruments'))


#Test Function To Test If Number of Files Match in Original and Copy AudioData Folder
def findSum(input,output):
    count_files_og = 0
    for parent_dir in os.listdir(input):
        for files in os.listdir(os.path.join(input,parent_dir)):
            count_files_og += 1
    count_files_copy = 0
    for copy_parent_dir in os.listdir(output):
        for files in os.listdir(os.path.join(output,copy_parent_dir)):
            count_files_copy += 1
    return count_files_og, count_files_copy

print(findSum('AudioData','Folded-AudioData'))

def GenerateWAVEFromArray(input_dir,output_dir):
    files = os.listdir(input_dir)
    for eachfile in files:
        file_path = os.path.join(input_dir,eachfile)
        y,sr = librosa.load(file_path,duration=5.0)
        print("Converting " + file_path)
        soundfile.write(os.path.join(output_dir,(str(eachfile[:len(eachfile)-5]))) + "wav",y,sr)

GenerateWAVEFromArray(os.path.join(parent_folder,'001 - Voices'),os.path.join(copy_parent_folder,'001 - Voices'))
GenerateWAVEFromArray(os.path.join(parent_folder,'002 - Liquids'),os.path.join(copy_parent_folder,'002 - Liquids'))
GenerateWAVEFromArray(os.path.join(parent_folder,'003 - Locomotion'),os.path.join(copy_parent_folder,'003 - Locomotion'))
GenerateWAVEFromArray(os.path.join(parent_folder,'004 - HouseItems'),os.path.join(copy_parent_folder,'004 - HouseItems'))
GenerateWAVEFromArray(os.path.join(parent_folder,'005 - Digestive'),os.path.join(copy_parent_folder,'005 - Digestive'))
GenerateWAVEFromArray(os.path.join(parent_folder,'006 - Hygiene'),os.path.join(copy_parent_folder,'006 - Hygiene'))
GenerateWAVEFromArray(os.path.join(parent_folder,'007 - Elements'),os.path.join(copy_parent_folder,'007 - Elements'))
GenerateWAVEFromArray(os.path.join(parent_folder,'008 - Animals'),os.path.join(copy_parent_folder,'008 - Animals'))
GenerateWAVEFromArray(os.path.join(parent_folder,'009 - Cooking_Appliances'),os.path.join(copy_parent_folder,'009 - Cooking_Appliances'))
GenerateWAVEFromArray(os.path.join(parent_folder,'010 - Cleaning_Appliances'),os.path.join(copy_parent_folder,'010 - Cleaning_Appliances'))
GenerateWAVEFromArray(os.path.join(parent_folder,'011 - Lighting_Appliances'),os.path.join(copy_parent_folder,'011 - Lighting_Appliances'))
GenerateWAVEFromArray(os.path.join(parent_folder,'012 - Ventilation_Appliances'),os.path.join(copy_parent_folder,'012 - Ventilation_Appliances'))
GenerateWAVEFromArray(os.path.join(parent_folder,'013 - Furniture'),os.path.join(copy_parent_folder,'013 - Furniture'))
GenerateWAVEFromArray(os.path.join(parent_folder,'014 - Tools'),os.path.join(copy_parent_folder,'014 - Tools'))
GenerateWAVEFromArray(os.path.join(parent_folder,'015 - Instruments'),os.path.join(copy_parent_folder,'015 - Instruments'))

folded = 'Folded-AudioData'

def categorizeFiles(input_dir):
    files = glob(os.path.join(parent_folder,input_dir,'*.wav'))
    print(files)
    for eachfile in files:
        arr = eachfile.split("-")
        fold_no = str(arr[3])[0]
        print(fold_no)
        temp = eachfile.split("\\")
        outputfile = temp[2]
        if fold_no == '0':
            print("renaming:" + eachfile)
            os.rename(eachfile,os.path.join(folded,'fold0',outputfile))
        elif fold_no == '1':
            print("renaming:" + eachfile)
            os.rename(eachfile,os.path.join(folded,'fold1',outputfile))
        elif fold_no == '2':
            print("renaming:" + eachfile)
            os.rename(eachfile,os.path.join(folded,'fold2',outputfile))
        elif fold_no == '3':
            print("renaming:" + eachfile)
            os.rename(eachfile,os.path.join(folded,'fold3',outputfile))
        elif fold_no == '4':
            print("renaming:" + eachfile)
            os.rename(eachfile,os.path.join(folded,'fold4',outputfile))
        elif fold_no == '5':
            print("renaming:" + eachfile)
            os.rename(eachfile,os.path.join(folded,'fold5',outputfile))
        elif fold_no == '6':
            print("renaming:" + eachfile)
            os.rename(eachfile,os.path.join(folded,'fold6',outputfile))
        elif fold_no == '7':
            print("renaming:" + eachfile)
            os.rename(eachfile,os.path.join(folded,'fold7',outputfile))
        elif fold_no == '8':
            print("renaming:" + eachfile)
            os.rename(eachfile,os.path.join(folded,'fold8',outputfile))
        elif fold_no == '9' or fold_no == '10':
            print("renaming:" + eachfile)
            os.rename(eachfile,os.path.join(folded,'fold9',outputfile))    

for subdir in all_og_child_directories:
    categorizeFiles(subdir)
