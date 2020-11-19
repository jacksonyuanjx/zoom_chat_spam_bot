import pyautogui

print(pyautogui.getAllWindows())
win = pyautogui.getWindowsWithTitle("Zoom Meeting")
if (not len(win)):
    win = pyautogui.getWindowsWithTitle("Zoom")[0]
else:
    win = win[0]
print("===", win)
win.activate()

pyautogui.hotkey("alt", "h")

for i in range(0, 2):
    pyautogui.write("https://sites.google.com/view/ubc-cpsc310-20w1-intro-to-se/calendar")
pyautogui.press("enter")

# Logs current position of cursor
# try:
#     while True:
#         x, y = pyautogui.position()
#         positionStr = "X: " + str(x).rjust(4) + " Y: " + str(y).rjust(4)
#         print(positionStr, end="")
#         print("\b" * len(positionStr), end="", flush=True)
# except KeyboardInterrupt:
#     print("\n")