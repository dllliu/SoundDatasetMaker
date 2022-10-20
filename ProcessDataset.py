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

parent_folder = #OG SOURCE DIR WHERE ALL SUBFOLDERS OF FILE CLASSES WERE SAVED

copy_parent_folder = #COPY DIRS FOR EACH STEP

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
ConvertFilesWithFFmpeg(os.path.join(parent_folder,'002 - Locomotion'),os.path.join(copy_parent_folder,'002 - Locomotion'))
ConvertFilesWithFFmpeg(os.path.join(parent_folder,'003 - Digestive'),os.path.join(copy_parent_folder,'003 - Digestive'))
ConvertFilesWithFFmpeg(os.path.join(parent_folder,'004 - Elements'),os.path.join(copy_parent_folder,'004 - Elements'))
ConvertFilesWithFFmpeg(os.path.join(parent_folder,'005 - Animals'),os.path.join(copy_parent_folder,'005 - Animals'))
ConvertFilesWithFFmpeg(os.path.join(parent_folder,'006 - Cooking_Appliances'),os.path.join(copy_parent_folder,'006 - Cooking_Appliances'))
ConvertFilesWithFFmpeg(os.path.join(parent_folder,'007 - Cleaning_Appliances'),os.path.join(copy_parent_folder,'007 - Cleaning_Appliances'))
ConvertFilesWithFFmpeg(os.path.join(parent_folder,'008 - Ventilation_Appliances'),os.path.join(copy_parent_folder,'008 - Ventilation_Appliances'))
ConvertFilesWithFFmpeg(os.path.join(parent_folder,'009 - Furniture'),os.path.join(copy_parent_folder,'009 - Furniture'))
ConvertFilesWithFFmpeg(os.path.join(parent_folder,'010 - Instruments'),os.path.join(copy_parent_folder,'010 - Instruments'))


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

def GenerateWAVE(input_dir,output_dir):
    files = os.listdir(input_dir)
    for eachfile in files:
        file_path = os.path.join(input_dir,eachfile)
        y,sr = librosa.load(file_path,duration=5.0)
        print("Converting " + file_path)
        soundfile.write(os.path.join(output_dir,(str(eachfile[:len(eachfile)-5]))) + "wav",y,sr)

GenerateWAVE(os.path.join(parent_folder,'001 - Voices'),os.path.join(copy_parent_folder,'001 - Voices'))
GenerateWAVE(os.path.join(parent_folder,'002 - Locomotion'),os.path.join(copy_parent_folder,'002 - Locomotion'))
GenerateWAVE(os.path.join(parent_folder,'003 - Digestive'),os.path.join(copy_parent_folder,'003 - Digestive'))
GenerateWAVE(os.path.join(parent_folder,'004 - Elements'),os.path.join(copy_parent_folder,'004 - Elements'))
GenerateWAVE(os.path.join(parent_folder,'005 - Animals'),os.path.join(copy_parent_folder,'005 - Animals'))
GenerateWAVE(os.path.join(parent_folder,'006 - Cooking_Appliances'),os.path.join(copy_parent_folder,'006 - Cooking_Appliances'))
GenerateWAVE(os.path.join(parent_folder,'007 - Cleaning_Appliances'),os.path.join(copy_parent_folder,'007 - Cleaning_Appliances'))
GenerateWAVE(os.path.join(parent_folder,'008 - Ventilation_Appliances'),os.path.join(copy_parent_folder,'008 - Ventilation_Appliances'))
GenerateWAVE(os.path.join(parent_folder,'009 - Furniture'),os.path.join(copy_parent_folder,'009 - Furniture'))
GenerateWAVE(os.path.join(parent_folder,'010 - Instruments'),os.path.join(copy_parent_folder,'010 - Instruments'))


folded_dir = 'Folded-AudioData'

def make_file_structure():
    arr = ['fold0','fold1','fold2','fold3','fold4','fold5','fold6','fold7','fold8','fold9']
    for fold in arr:
        OutFolder = os.path.join(folded_dir,fold)
        if not os.path.exists(OutFolder):
            os.makedirs(OutFolder)
            
def categorizeFiles(input_dir):
    files = glob(os.path.join(parent_folder,input_dir,'*.wav'))
    print(files)
    for eachfile in files:
        arr = eachfile.split("-")
        fold_no = str(arr[3])[0]
        print("renaming:" + str(eachfile) + "with fold number of" + str(fold_no))
        temp = eachfile.split("\\")
        outputfile = temp[2]
        os.rename(eachfile,os.path.join(folded_dir,'fold'+str(fold_no),outputfile))

make_file_structure()
for subdir in os.listdir(parent_folder):
    categorizeFiles(subdir) 
  