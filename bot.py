import pyautogui
import sys

file = open("spam.txt", "r")
spam_msg = file.read()

win = pyautogui.getWindowsWithTitle("Zoom Meeting")
if (not len(win)):
    win = pyautogui.getWindowsWithTitle("Zoom")[0]
else:
    win = win[0]

# print("===", win)
win.activate()
if "zoom_chat_spam_bot" in pyautogui.getActiveWindow().title:
    sys.exit("Zoom application window is not open")

pyautogui.hotkey("alt", "h")

# while True:
for i in range(0, 10):
    pyautogui.write(spam_msg)
    pyautogui.press("enter")

sys.exit("Spam bot operation complete")


# Logs current position of cursor
# try:
#     while True:
#         x, y = pyautogui.position()
#         positionStr = "X: " + str(x).rjust(4) + " Y: " + str(y).rjust(4)
#         print(positionStr, end="")
#         print("\b" * len(positionStr), end="", flush=True)
# except KeyboardInterrupt:
#     print("\n")
