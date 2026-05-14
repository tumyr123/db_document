import os
import sys
import time

import pygame.mixer as sound

import keyboard
import pyautogui as mouse





ring_mp3 = "ring.mp3"

img_bad = "img/1bad.png"
img_back = "img/back.png"
#img_back = 'back.png'
img_btnRegisrer = "img/btnRegisrer.png"

print(os.path.exists(img_bad))
print(os.path.exists(img_back))
print(os.path.exists(img_btnRegisrer))
print(os.path.exists(ring_mp3))


#mouse.locateOnScreen(img_back)


sound.init()
sound.music.load(ring_mp3)
sound.music.play()







keyboard.add_hotkey("2",lambda: main())
keyboard.add_hotkey("3",lambda: back() )
keyboard.add_hotkey("4",lambda: search_termin() )
keyboard.add_hotkey("5",lambda: bad_result() )






def quit():
    sys.exit(0)

def main():

    while True:
        search_termin()
        #mouse.move(0,200)
        time.sleep(1)
        bad_result()
        time.sleep(15)



def bad_result():
    try:

        pos = mouse.locateOnScreen(img_bad, confidence=0.6, grayscale=True)
        print(pos)
        # mouse.click()
        back()
    except mouse.ImageNotFoundException:
        sound.music.play(3)




def test_bad():
    try:
        pos = mouse.locateOnScreen(img_bad, confidence=0.6,grayscale=True)
        print(pos)
       # mouse.click()
        back()

    except mouse.ImageNotFoundException:
        #mouse.screenshot("current.png")
        print("Картинка не найдена2")


def search_termin():
    try:
        pos = mouse.locateOnScreen(img_btnRegisrer)
        print(pos)
        x,y = pos.left,pos.top
        left = pos.width/2
        down = pos.height/2

        print(x+left,y+down)
        mouse.moveTo(x+left,y+down)
        mouse.click()

    except mouse.ImageNotFoundException:
        print("Картинка не найдена")


def back():
    #local = mouse.locateOnScreen(img_back)
    #print(local)
    #mouse.moveTo(btnBack_located)
    try:
        pos = mouse.locateOnScreen(img_back)
        print(pos)
        x,y = pos.left,pos.top
        left = pos.width/2
        down = pos.height/2

        print(x+left,y+down)
        mouse.moveTo(x+left,y+down)
        mouse.click()

    except mouse.ImageNotFoundException:
        print("Картинка не найдена")





keyboard.wait()