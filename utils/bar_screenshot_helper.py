from pyautogui import position, screenshot
from keyboard import add_hotkey, wait

# variables to store the selected coordinates
top_left = None
bottom_right = None

def set_top_left():
    """Set the top-left corner based on the current mouse position."""
    global top_left
    x, y = position()
    top_left = (x, y)
    print(f"Top-left set at: {top_left}")

def set_bottom_right():
    """Set the bottom-right corner based on the current mouse position."""
    global bottom_right
    x, y = position()
    bottom_right = (x, y)
    print(f"Bottom-right set at: {bottom_right}")

def capture_region():
    """Capture the selected region and save it as an image."""
    global top_left, bottom_right
    if not top_left or not bottom_right:
        print("Define top-left and bottom-right before capturing.")
        return
    
    x1, y1 = top_left
    x2, y2 = bottom_right
    width = x2 - x1
    height = y2 - y1

    region = (x1, y1, width, height)
    print(f"Final coordinates (x, y, width, height): {region}")
    
    region_screenshot = screenshot(region=region)
    region_screenshot.save("region_capture.png")
    print("Capture saved as 'region_capture.png'")

# hotkeys to facilitate coordinate selection
add_hotkey("ctrl+shift+t", set_top_left)       # set top-left
add_hotkey("ctrl+shift+b", set_bottom_right)   # Set bottom-right
add_hotkey("ctrl+shift+c", capture_region)     # capture the region

print("Script started.")
print("Use CTRL+SHIFT+T to mark the top-left point.")
print("Use CTRL+SHIFT+B to mark the bottom-right point.")
print("Use CTRL+SHIFT+C to capture the selected region.")
print("Press ESC to exit.")

# keep the script running until ESC is pressed
wait("esc")