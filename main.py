import math
from PIL import Image, ImageColor
import pyautogui

pyautogui.countdown(3)
screenshot = pyautogui.screenshot()
screenshot.save("screen.png")
myImg = Image.open("screen.png")

drag_duration = 0.05
radius = 400
center_x, center_y = myImg.width / 2, myImg.height / 2

x = center_x + float(radius * math.cos(math.radians(0)))
y = center_y + float(radius * math.sin(math.radians(0)))
pyautogui.moveTo(x, y, duration=drag_duration)
pyautogui.mouseDown()
for angle in range(0, 361, 120):
    x = center_x + float(radius * math.cos(math.radians(angle)))
    y = center_y + float(radius * math.sin(math.radians(angle)))
    pyautogui.moveTo(x, y, duration=drag_duration)