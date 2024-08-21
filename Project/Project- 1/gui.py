import pyautogui
# import opencv

pyautogui.useImageNotFoundException()

try:
    location = pyautogui.locateCenterOnScreen('windows_', confidence=0.8)
    print(f"Image found at: {location}")
except pyautogui.ImageNotFoundException:
    print("Image not found on the screen.")



with open ("win.png", "png") as f:
    print(f)