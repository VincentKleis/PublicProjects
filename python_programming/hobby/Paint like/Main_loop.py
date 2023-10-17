import cv2 as cv
import CVDraw as draw
import numpy as np

img = np.full((600, 800, 3), 255, np.uint8)
prev = img.copy()
drawing = False
# start coordinats for mouse
ix, iy = -1, -1
mode = "Triangle"


def Mouse_event(event, x, y, flags, params):
        global drawing, img, prev, ix, iy, mode
        tools = draw.mouse_tools()

        # recods x and y at mous down click
        if event == cv.EVENT_LBUTTONDOWN:
            drawing = True
            ix, iy = x, y
        
        # as mouse is moved draws a triangle where it is moved and 
        elif event == cv.EVENT_MOUSEMOVE:
            if drawing == True:
                if mode == "Triangle":
                    # re draw based on permanent image to create the ilusion of see trough ness
                    prev = img.copy()
                    tools.draw_triangel(prev, (ix, iy), (x-ix)*2, 3, [0, 0, 0])

        # when mouse is let go draw the triangle to the permanent image
        elif event == cv.EVENT_LBUTTONUP:
            drawing = False
            if mode == "Triangle":
                tools.draw_triangel(img, (ix, iy), (x-ix)*2, 3, [0, 0, 0])


# main loop
canvas = draw.mouse_tools()
cv.namedWindow("image")
cv.setMouseCallback("image", Mouse_event)

while True:
    draw.icon_draw(canvas, canvas)
    cv.imshow("image", prev)
    cv.waitKey(1)
    if cv.getWindowProperty("image", cv.WND_PROP_VISIBLE) < 1:
        break

cv.destroyAllWindows()