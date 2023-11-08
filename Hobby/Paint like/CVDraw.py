import cv2 as cv
import numpy as np
from PIL import Image

class mouse_tools():

    def draw_triangel(self, canvas:list , centerpoint:tuple, sidelenght:int, thickness:int, color):

        height = round(sidelenght*((3**(1/2)/2)))
        top = (centerpoint[0], round(centerpoint[1]-height/2))
        left = (round(centerpoint[0]-sidelenght/2), round(centerpoint[1]+height/2))
        right = (round(centerpoint[0]+sidelenght/2), round(centerpoint[1]+height/2))

        image = cv.line(canvas, top, left, color, thickness)
        image = cv.line(image, top, right, color, thickness)
        image = cv.line(image, left, right, color, thickness)

        return image
    

    def stack_based_fill(self, canvas:list, point:tuple, color:list):
            """takes a canvas color and point and changes every pixel of the same color in that regeon to the chosen color

            Args:
                color (list): list of rgb values
                point (tuple): tuple containing x and y coordinates for the startingpoint of a fill
            """
            pixels_front = []
            pixel_color = canvas[point[1]][point[0]].copy()
            pixels_front.append(point)
            new_front = []

            while len(pixels_front) > 0:
                for pixel in pixels_front:
                    neighbours = [(pixel[0]+1, pixel[1]), (pixel[0], pixel[1]+1), (pixel[0]-1, pixel[1]), (pixel[0], pixel[1]-1)]

                    for x in neighbours:
                        if f"{canvas[x[1]][x[0]]}" == f"{pixel_color}":
                            new_front.append(x)
                            canvas[x[1]][x[0]] = color

                for pixel in new_front:
                    pixels_front.append(pixel)

                new_front = []

def icon_draw(window, image):
    """draws icons at the top of canvas

    Args:
        window_size (tuple): size of the application window
    """
    brush = Image.open("icons/brush.png")
    brush = np.array(brush)
    color_palette = Image.open("icons/color-palette.png")
    paint_bucket = Image.open("icons/paint-bucket.png")
    shapes = Image.open("icons/shape.png")



def icon_select(coords:tuple):
    """checks if x and y are on an icon, and if it is, 
    it animates the pressing of a button

    Args:
        coords (tuple): the coordinates of the mouse
    """