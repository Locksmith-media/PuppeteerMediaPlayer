# PuppeteerMediaPlayer

Media Player for Escape Room Management System 

This is a standalone MediaPlayer which is part of the Puppeteer Escape Room Management System.
It consists of several audio and one video player that can be edited to play automatically or manually. 
It is running on a RPi 3B+ with Debian Buster Lite, a HifiBerry DAC Hat and optional a UPS (Uninterruptible Power Supply).
It is edited and controlled via a web UI and capable of receiving network messages and GPIO Ins to autostart and stop players or choose an audio or videofile.

The Webserver is created with flask linking to html files to generate the Web UI. 
