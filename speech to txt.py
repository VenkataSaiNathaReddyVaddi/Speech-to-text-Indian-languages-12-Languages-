import pyttsx3
import time
import speech_recognition as sr
import googletrans
import pyautogui
import pynput
import datetime
import playsound as ps
from pynput.keyboard import Key,Controller
#import googletrans
import os
import tkinter
from tkinter import messagebox
import random
from PIL import Image,ImageTk
root=tkinter.Tk()
root.title("SPEECH TO TEXT")
root.geometry("1100x700")
root.configure(bg="#141414")
#root.iconbitmap(r'E:\delhi_police_logo_fnR_icon.ico')
gt=googletrans.Translator()

def stop():
    pyautogui.hotkey('alt','f4')

def takecomtel():
    messagebox.showinfo("speech to text software","you have selected telugu as the language")
    root.destroy()
    pyautogui.hotkey('win','s')
    time.sleep(1)
    pyautogui.write('notepad')
    time.sleep(1)
    pyautogui.press('enter')
    pyautogui.press('enter')
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 0.5
            audio = r.listen(source)

        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='te-in')
            print(f"User said: {query}\n")
            try:
                keyboard=Controller()
                keyboard.type(query)
            except Exception as e:
                print(e)
        except Exception as e:
                # print(e)
            print("Sir!please say that again...")  


def takecomhin():
    messagebox.showinfo("speech to text software","you have selected hindi as the language")
    root.destroy()
    pyautogui.hotkey('win','s')
    time.sleep(1)
    pyautogui.write('notepad')
    time.sleep(1)
    pyautogui.press('enter')
    pyautogui.press('enter')
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 2
            audio = r.listen(source)

        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='hi-in')
            print(f"User said: {query}\n")
            try:
                keyboard=Controller()
                keyboard.type(query)
            except Exception as e:
                print(e)
        except Exception as e:
                # print(e)
            print("Sir!please say that again...") 


def takecomeng():
    messagebox.showinfo("speech to text software","you have selected english as the language")
    root.destroy()
    pyautogui.hotkey('win','s')
    time.sleep(1)
    pyautogui.write('notepad')
    time.sleep(1)
    pyautogui.press('enter')
    pyautogui.press('enter')
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 0.5
            audio = r.listen(source)

        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
            try:
                keyboard=Controller()
                keyboard.type(query)
            except Exception as e:
                print(e)
        except Exception as e:
                # print(e)
            print("Sir!please say that again...")


def takecomtam():
    messagebox.showinfo("speech to text software","you have selected tamil as the language")
    root.destroy()
    pyautogui.hotkey('win','s')
    time.sleep(1)
    pyautogui.write('notepad')
    time.sleep(1)
    pyautogui.press('enter')
    pyautogui.press('enter')
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 0.5
            audio = r.listen(source)

        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='ta-in')
            print(f"User said: {query}\n")
            try:
                if 'close' in query:
                    pyautogui.hotkey('ctrl','s')
                    time.sleep(5)
                    pyautogi.hotkey('alt','f4')
                keyboard=Controller()
                keyboard.type(query)
            except Exception as e:
                print(e)
        except Exception as e:
                # print(e)
            print("Sir!please say that again...") 


def takecommal():
    messagebox.showinfo("speech to text software","you have selected malyalam as the language")
    root.destroy()
    pyautogui.hotkey('win','s')
    time.sleep(1)
    pyautogui.write('notepad')
    time.sleep(1)
    pyautogui.press('enter')
    pyautogui.press('enter')
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 0.5
            audio = r.listen(source)

        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='ml-in')
            print(f"User said: {query}\n")
            try:
                keyboard=Controller()
                keyboard.type(query)
            except Exception as e:
                print(e)
        except Exception as e:
                # print(e)
            print("Sir!please say that again...")


def takecommar():
    messagebox.showinfo("speech to text software","you have selected marathi as the language")
    root.destroy()
    pyautogui.hotkey('win','s')
    time.sleep(1)
    pyautogui.write('notepad')
    time.sleep(1)
    pyautogui.press('enter')
    pyautogui.press('enter')
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 0.5
            audio = r.listen(source)

        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='mr-in')
            print(f"User said: {query}\n")
            try:
                keyboard=Controller()
                keyboard.type(query)
            except Exception as e:
                print(e)
        except Exception as e:
                # print(e)
            print("Sir!please say that again...")

def takecomguj():
    messagebox.showinfo("speech to text software","you have selected gujrati as the language")
    root.destroy()
    pyautogui.hotkey('win','s')
    time.sleep(1)
    pyautogui.write('notepad')
    time.sleep(1)
    pyautogui.press('enter')
    pyautogui.press('enter')
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 0.5
            audio = r.listen(source)

        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='gu-in')
            print(f"User said: {query}\n")
            try:
                keyboard=Controller()
                keyboard.type(query)
            except Exception as e:
                print(e)
        except Exception as e:
                # print(e)
            print("Sir!please say that again...")

def takecomben():
    messagebox.showinfo("speech to text software","you have selected bengali as the language")
    root.destroy()
    pyautogui.hotkey('win','s')
    time.sleep(1)
    pyautogui.write('notepad')
    time.sleep(1)
    pyautogui.press('enter')
    pyautogui.press('enter')
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 0.5
            audio = r.listen(source)

        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='bn-in')
            print(f"User said: {query}\n")
            try:
                keyboard=Controller()
                keyboard.type(query)
            except Exception as e:
                print(e)
        except Exception as e:
                # print(e)
            print("Sir!please say that again...")

def takecomodi():
    messagebox.showinfo("speech to text software","you have selected odia as the language")
    root.destroy()
    pyautogui.hotkey('win','s')
    time.sleep(1)
    pyautogui.write('notepad')
    time.sleep(1)
    pyautogui.press('enter')
    pyautogui.press('enter')
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 0.5
            audio = r.listen(source)

        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='or-in')
            print(f"User said: {query}\n")
            try:
                keyboard=Controller()
                keyboard.type(query)
            except Exception as e:
                print(e)
        except Exception as e:
                # print(e)
            print("Sir!please say that again...")

def takecompun():
    messagebox.showinfo("speech to text software","you have selected punjabi as the language")
    root.destroy()
    pyautogui.hotkey('win','s')
    time.sleep(1)
    pyautogui.write('notepad')
    time.sleep(1)
    pyautogui.press('enter')
    pyautogui.press('enter')
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 0.5
            audio = r.listen(source)

        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='pa-in')
            print(f"User said: {query}\n")
            try:
                keyboard=Controller()
                keyboard.type(query)
            except Exception as e:
                print(e)
        except Exception as e:
                # print(e)
            print("Sir!please say that again...")

def takecomurd():
    messagebox.showinfo("speech to text software","you have selected urdu as the language")
    root.destroy()
    pyautogui.hotkey('win','s')
    time.sleep(1)
    pyautogui.write('notepad')
    time.sleep(1)
    pyautogui.press('enter')
    pyautogui.press('enter')
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 0.5
            audio = r.listen(source)

        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='ur-in')
            print(f"User said: {query}\n")
            try:
                keyboard=Controller()
                keyboard.type(query)
            except Exception as e:
                print(e)
        except Exception as e:
                # print(e)
            print("Sir!please say that again...")

def takecomsindh():
    messagebox.showinfo("speech to text software","you have selected sindhi as the language")
    root.destroy()
    pyautogui.hotkey('win','s')
    time.sleep(1)
    pyautogui.write('notepad')
    time.sleep(1)
    pyautogui.press('enter')
        
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 0.5
            audio = r.listen(source)

        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='sd-in')
            print(f"User said: {query}\n")
            try:
                keyboard=Controller()
                keyboard.type(query)
            except Exception as e:
                print(e)
        except Exception as e:
                # print(e)
            print("Sir!please say that again...")
L1 = tkinter.Label(root, text="SPEECH TO TEXT SOFTWARE",bg="black",fg="yellow",font="InkFree 50 bold",width=500)
L1.pack( side = 'top')
im1=ImageTk.PhotoImage(Image.open("E:\delhi2.png"))
panel = tkinter.Label(root, image = im1)
panel.pack(side = "right", fill = "both")
b1=tkinter.Button(root,text="telugu",bg="black",fg="blue",font="Dungeon 13",width="20",command=takecomtel,bd=10)
b1.pack( side='top')
b2=tkinter.Button(root,text="hindi",bg="black",fg="blue",font="Dungeon 13",width="20",command=takecomhin,bd=10)
b2.pack(side='top')
b3=tkinter.Button(root,text="english",bg="black",fg="blue",font="Dungeon 13",width="20",command=takecomeng,bd=10)
b3.pack(side='top')
b4=tkinter.Button(root,text="tamil",bg="black",fg="blue",font="Dungeon 13",width="20",command=takecomtam,bd=10)
b4.pack(side='top')
b5=tkinter.Button(root,text="malayalam",bg="black",fg="blue",font="Dungeon 13",width="20",command=takecommal,bd=10)
b5.pack(side='top')
b6=tkinter.Button(root,text="marathi",bg="black",fg="blue",font="Dungeon 13",width="20",command=takecommal,bd=10)
b6.pack(side='top')
b7=tkinter.Button(root,text="gujrati",bg="black",fg="blue",font="Dungeon 13",width="20",command=takecomguj,bd=10)
b7.pack(side='top')
b8=tkinter.Button(root,text="bengali",bg="black",fg="blue",font="Dungeon 13",width="20",command=takecomben,bd=10)
b8.pack(side='top')
b9=tkinter.Button(root,text="odia",bg="black",fg="blue",font="Dungeon 13",width="20",command=takecomodi,bd=10)
b9.pack(side='top')
b10=tkinter.Button(root,text="punjabi",bg="black",fg="blue",font="Dungeon 13",width="20",command=takecompun,bd=10)
b10.pack(side='top')
b11=tkinter.Button(root,text="urdu",bg="black",fg="blue",font="Dungeon 13",width="20",command=takecomurd,bd=10)
b11.pack(side='top')
b12=tkinter.Button(root,text="sindhi",bg="black",fg="blue",font="Dungeon 13",width="20",command=takecomsindh,bd=10)
b12.pack(side='top')
messagebox.showinfo("speech to text software","welcome to speech to text software")
messagebox.showinfo("speech to text software","make sure you are connected to internet")
root.mainloop()

