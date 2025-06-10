#This file is going to look for the folder inside user upload and convert them into reel if they are not already converted
import os
from text_to_audio import text_to_speech_file
import time
import subprocess

def text_to_audio(folder):
    print("TTA-",folder)
    with open(f"user_upload/{folder}/desc.txt") as f:
        text=f.read()
    print(text, folder)
    text_to_speech_file(text,folder)

#before creating the reel we have to convert the text into audio
def create_reel(folder):
    command = f'''ffmpeg -f concat -safe 0 -i user_upload/{folder}/input.txt -i user_upload/{folder}/audio.mp3 -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:black" -c:v libx264 -c:a aac -shortest -r 30 -pix_fmt yuv420p static/reels/{folder}.mp4'''
    subprocess.run(command, shell=True, check=True)
    
    print("CR-",folder)
if __name__=="__main__":
    while True:
        print("Processing Queue...")
        with open("done.txt","r") as f:
            done_folders=f.readlines()
        
        done_folders=[f.strip() for f in done_folders]
        folders=os.listdir("user_upload")
        #print(folders,done_folders) i have checked the problem adn the problem is ther is \n in done_folders so i have to strip the folder name. so that it can compare it with the folders
        
        for folder in folders:
            if (folder not in done_folders): 
                text_to_audio(folder)#Generate the audio from desc.txt
                create_reel(folder)# this will convert the images and audio.mp3 inside the folder into a reel 
                with open("done.txt","a") as f:# after completion i want to add the filename in the done.txt file
                    f.write(folder + "\n")
        time.sleep(4)