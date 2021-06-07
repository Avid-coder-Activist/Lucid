from tkinter import *
import pygame
import subprocess as cmdLine
import time
import os
def testerror(code):
    speak("there was an error while running diagnostics. error code" + code, myvce)
def fatal_error(code):
    file = "lucid_fatal_error_sound.mp3"
    os.system("omxplayer " + file)
    speak("There was a fatal error in the system.", "bot")
    speak("error code" + code, "bot")
    speak("Would you like to call Avid for help or factory reset?", "bot")
    decision = input("What do you want to do?")
def error(text):
    pygame.mixer.init()
    pygame.mixer.music.load("lucid_error_sound.mp3")
    pygame.mixer.music.play()
    time.sleep(1)
def speak(text, vce):
    cmdLine.run("clear")
    if vce == "girl":
        try:
            command = "espeak -ven-us+f4 -s170 " + chr(34) + text+ chr(34)
            cmdLine.run(command, shell=True)
            cmdLine.run("clear")
        except:
            fatal_error("three")
    elif vce == "boy":
        try:
            command = "espeak -ven-us+f9 -s169 " + chr(34) + text + chr(34)
            cmdLine.run(command, shell=True)
            cmdLine.run("clear")
        except:
            fatal_error("three")
    elif vce == "bot":
        try:
            command = "espeak -ven-us+f9 -s130 -p0 " + chr(34) + text + chr(34)
            cmdLine.run(command, shell=True)
            cmdLine.run("clear")
        except:
            fatal_error("three")
myvce = "x"
myname = "x"
mycity = "x"
def scan():
    global myvce
    global myname
    global mycity
    try:
        f = open("DISC/voice.txt", "r")
        myvce = f.read()
        f.close
    except:
        fatal_error("four")
    try:
        f = open("DISC/name.txt", "r")
        myname = f.read()
        f.close
    except:
        fatal_error("four")
    try:
        f = open("DISC/city.txt", "r")
        mycity = f.read()
        f.close
    except:
        fatal_error("four")
    try:
        f = open("DISC/burner.txt", "r")
        burnfile = f.read()
        f.close
    except:
        fatal_error("four")
    if not "WORMBURNER" in burnfile:
        def config3():
            try:
                speak("what is your city with proper capitalization?", "bot")
                city = input("What is your city with proper capitalization?")
                f = open("DISC/city.txt", "w")
                f.write(city)
                f.close()
                f = open("DISC/burner.txt", "w")
                f.write("WORMBURNER")
                f.close()
                speak("Thank you.", "bot")
                scan()
            except:
                fatal_error("five")
        def config2():
            try:
                speak("What is your first name?", "bot")
                name = input("What is your first name?")
                f = open("DISC/name.txt", "w")
                f.write(name)
                f.close()
                config3()
            except:
                fatal_error("five")
        def config1():
            speak("Hello. I am lucid, your new voice assistant.", "bot")
            speak("What voice would you like?", "bot")
            voice = input("Would you like bot, girl, or boy? (all lowercase.)")
            if voice == "bot":
                f = open("DISC/voice.txt", "w")
                f.write(voice)
                f.close()
                config2()
            elif voice == "girl":
                f = open("DISC/voice.txt", "w")
                f.write(voice)
                f.close()
                config2()
            elif voice == "boy":
                f = open("DISC/voice.txt", "w")
                f.write(voice)
                f.close()
                config2()
            else:
                error("Sorry, enter that agin.")
                config1()
        config1()
    else:
        main()
def main():
    speak("what can I do for you?", myvce)
    explorer = input("what can I do for you?")
    if "test" or "diagnostics" and not "not" in explorer:
        speak("Running diagnostics.", myvce)
        try:
            error("testing")
        except:
            testerror("two")
        speak("There were no Problems.", myvce)
        speak("Thanks " + myname, myvce)
        main()
            


def intro():
    def lucid_logo():
        window = Tk()
        window.title("Lucid")
        canvas = Canvas(window, width = 1710, height = 1407)
        canvas.pack()
        my_image = PhotoImage(file = "lucid_logo.png")
        canvas.create_image(0, 0, anchor = NW, image=my_image)
        pygame.mixer.init()
        pygame.mixer.music.load("lucid_intro.mp3")
        pygame.mixer.music.play()
        window.after(5000, window.destroy)
        canvas.mainloop()
        window.mainloop()
    def mtech_logo():
        window = Tk()
        window.title("Lucid")
        canvas = Canvas(window, width = 1928, height = 1415)
        canvas.pack()
        my_image = PhotoImage(file = "mtechlogo.png")
        canvas.create_image(0, 0, anchor = NW, image=my_image)
        pygame.mixer.init()
        pygame.mixer.music.load("mtechstartup.mp3")
        pygame.mixer.music.play()
        window.after(5000, window.destroy)
        canvas.mainloop()
        window.mainloop()
    lucid_logo()
    mtech_logo()
    scan()
intro()