#!/usr/bin/python3

# Puppeteer MediaPlayer V0.04
#
#
# Part of the EscapeRoom Management System Puppeteer
#
# What it should do:
# play audio and video files on a raspberry pi
# controlled by a web UI
# edited in another web UI
# Consists of 5 Players
# 1 Video player
# 1 Music Player
# 1 Sound Scape Player
# 1 Sound FX Player
# 1 additional Audio Player for Sound FX, Hints etc.

# new:
# added black screen for background # not working yet

# problems:
# black background not working
# audio only via headphones

from flask import Flask, render_template, redirect, url_for
import os
import sys
from subprocess import Popen
import time
import pygame


# Der gesamte Abschnitt führt noch zum Absturz. Code prüfen!
#initialise Background
#pygame.init()
#screen = pygame.display.set_mode([800,600])
#black = [0, 0, 0]
#screen.fill(black)
#pygame.display.update()
# print('black background')



# initialise Mixer
pygame.mixer.pre_init(48000, -16, 2, 4096) # setup mixer to avoid sound lag
pygame.mixer.init() 
print('Mixer loaded')

player=False

# set Media Directoties
audioDirectory = 'Media/Audio/'
videoDirectory = 'Media/Video/'

# load Audio files for testing
startup=pygame.mixer.Sound("Media/Audio/winner.wav")
bingo=pygame.mixer.Sound("Media/Audio/Bingo.wav")
gitarre=pygame.mixer.Sound("Media/Audio/gitarre.wav")

# load Movie files for testing
movie1 = ("Media/Video/GAMEOVER.mov")
movie2 = ("Media/Video/CONGRATULATIONS.mov")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])  # Methode 'post' verwenden um Daten im Backend zu verarbeiten.
def index():
    return redirect(url_for('home'))

@app.route("/home")
def home():
    startup.play()
    return render_template('index.html')
    
    
    

@app.route("/puppeteer")

def puppeteer():
    return render_template('puppeteer.html')

@app.route("/video/", methods=['POST'])
def video():
    os.system('killall omxplayer.bin')
    omxc = Popen(['omxplayer', '-b', movie1])
    player = True
    return render_template('puppeteer.html')

@app.route("/music/", methods=['POST'])
def music():
    bingo.play()
    return render_template('puppeteer.html')

@app.route("/atmo/", methods=['POST'])
def atmo():
    gitarre.play()
    return render_template('puppeteer.html')
    

    
#@app.route('/editor')
#def editor():
#    for videoFiles in os.listdir(videoDirectory):
#        if os.path.isfile(os.path.join(videoDirectory, videoFiles)):
#            print(videoFiles)
#    
#    videos = ''.join(videoFiles)
#            
#    for audioFiles in os.listdir(audioDirectory):
#        if os.path.isfile(os.path.join(audioDirectory, audioFiles)):
#            print(audioFiles)
#            
#    audios = ''.join(audioFiles)
#        
#    return 'This is the Editor of the Puppeteer Media Player ' + videos + ' ' + audios
#
#@app.route('/ftp')
#def ftp():
#    return 'This is going to be a ftp server for uploading media files'

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
