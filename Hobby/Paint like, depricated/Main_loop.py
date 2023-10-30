import cv2 as cv
import Draw as draw
import numpy as np
import tkinter as tk
from PIL import Image
root = tk.Tk()
root.withdraw()

canv_perm = np.full((500, 500, 3), 255, np.uint8)
prev_canv = canv_perm.copy()
drawing = False

# start coordinats for mouse
ix, iy = -1, -1
mode = "Triangle"
screen_size = (root.winfo_screenheight(), root.winfo_screenmmwidth())
window = np.full((screen_size[1], screen_size[0], 3), 255, np.uint8)

x_offset = 50
y_offset = 50
x_limit = screen_size[1]
y_limit = screen_size[0]

icon_positions = []
for y in range(5):
    icon_positions.append([(0, 50*y), (50 ,50*y+50)])

def Mouse_event(event, x, y, flags, params):
        global drawing, canv_perm, prev_canv, ix, iy, mode, window, icon_positions
        tools = draw.mouse_tools()
        click = False

        # recods x and y at mous down click
        if event == cv.EVENT_LBUTTONDOWN:
            drawing = True
            ix, iy = x, y
        
        
        # as mouse is moved draws a triangle where it is moved and 
        elif event == cv.EVENT_MOUSEMOVE:
            if drawing == True:
                if mode == "Triangle":
                    # re draw based on permanent image to create the ilusion of see trough ness
                    prev_canv = canv_perm.copy()
                    prev_canv = tools.draw_triangel(prev_canv, (ix, iy), (x-ix)*2, 3, [0, 0, 0])
           

        # when mouse is let go draw the triangle to the permanent image
        elif event == cv.EVENT_LBUTTONUP:
            drawing = False
            click = True
            if mode == "Triangle":
                tools.draw_triangel(canv_perm, (ix, iy), (x-ix)*2, 3, [0, 0, 0])

        icons = draw.icons(screen_size, icon_positions)
        window = icons.icon_draw((x, y), click, window)

        # this list comprehension does the same as the code within the below docstring
        # that being drawing the canvas in the window
        # window = [window[y][x] if x < x_offset and y < y_offset else prev_canv[y-y_offset][x-x_offset] for x in range(len(window)) for y in range(len(window))]

        hold = [[] for y in range(screen_size[0])]
        for x in range(screen_size[1]):
            for y in range(screen_size[0]):
                if x < x_offset or y < y_offset:

                    print(x, y, len(window), len(window[0]), len(hold), screen_size[0], screen_size[1])
                    hold[x].append(window[y][x])
                else:

                    hold[x].append(prev_canv[y-y_offset][x-x_offset])

        window = hold
        window = Image.fromarray(window)

# main loop
cv.namedWindow("image")
cv.setMouseCallback("image", Mouse_event)

while True:
    cv.imshow("image", window)
    cv.waitKey(1)
    if cv.getWindowProperty("image", cv.WND_PROP_VISIBLE) < 1:
        break

cv.destroyAllWindows()