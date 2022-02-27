import pyautogui as gui
import keyboard
import time
import math

# Helper function to get value of pixel in image
def getPixel(Image,x, y):
    px = Image.load()
    return px[x, y]

# Screen Dimensions
top, left, width, height = 102, 0, 1902, 776
screenDimensions = {
    "top": top,
    "left": left,
    "width": width,
    "height": height
}

# helper variables to calculate time
last = 0
total_time = 0

# the intervals where the bot will search for obstacles
y_search, x_start, x_end = 434, 410, 440
y_search2 = 335 # for the birds
y_search3 = 390
y_search4 = 420

time.sleep(1)
while True:
    t1 = time.time()
    if keyboard.is_pressed('q'): # Emergency Button
        break

    # increase the search width every second to simulate the dino acceleration
    if math.floor(total_time) != last:
        x_end += 5
        if x_end >= width:
            x_end = width
        last = math.floor(total_time)

    # a way to get a screen shot but it was too slow
    # sct_img = sct.grab(screenDimensions)
    # mss.tools.to_png(sct_img.rgb, sct_img.size, output="test.png")

    # Get a screen shot
    sct_img = gui.screenshot(region=(left,top, width, height))

    # Get the color of the world background
    bgColor = getPixel(sct_img, 440, 30)
    


    for i in reversed(range(x_start, x_end)):
        if gui.pixel(722, 417)[0] == 173:
            if gui.pixel(722, 417) == 118:
                if gui.pixel(722, 417) == 87:
                    # then press the down key
                    # I do not know how to initiate the down key so you do this part 
                    # just put the code over here 
                    print("saw brown obstacle")
        
        if getPixel(sct_img,i,y_search2) != bgColor and getPixel(sct_img,i,y_search) == bgColor:
             keyboard.press('down') #crouch
        elif getPixel(sct_img,i,y_search) != bgColor and getPixel(sct_img,i,y_search2) == bgColor:
             keyboard.release('down')
             keyboard.press(' ') #jump
        elif getPixel(sct_img,i,y_search3) != bgColor and getPixel(sct_img,i,y_search4) == bgColor:
             keyboard.press(' ') #mid bird jump
        else:
             
             break

    t2 = time.time()-t1
    total_time += t2

    # DEBUG
    print(x_end)

