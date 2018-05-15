import win32com.client as wincl
import pyautogui as pg
import webbrower as wb

speak = wincl.Dispatch("SAPI.SpVoice")

speak.Speak("What is your favorite football team  ")

answer = pg.prompt("Enter your favorite football team?")

if answer == "titans":
    speak.Speak("Wow, that's my favorite too.")
elif answer == "Lions":
    speak.Speak
