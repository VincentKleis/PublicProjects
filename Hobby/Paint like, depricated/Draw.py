import cv2 as cv
import numpy as np
from PIL import Image
from os import listdir, curdir

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
            
            return canvas


class icons():
    icons = []
    positions = []
    icon_mode = ""

    def __init__(self, window_size, positions):
        for icon in listdir(f"icons"):
            self.icons.append(f"icons/{icon}")
        
        self.icons = [Image.open(icon) for icon in self.icons]
        self.positions = positions
    
    def icon_draw(self, mouse_pos:tuple[int, int], clicked:bool, window:np.array) -> np.array:
        """draws each of the icons and if the position overlapps the icon then draw it with a gey outlined background

        Args:
            position (tuple): _description_
        """
        
        for x in range(len(self.icons)):
            current_icon = self.icons[x]
            pos_icon = self.positions[x]

            # mous pos is between upper x and lower x, and between upper y and lower y of pos_icon
            if mouse_pos[0] > pos_icon[0][0] and mouse_pos[0] < pos_icon[1][0] and \
                mouse_pos[1] > pos_icon[0][1] and mouse_pos[1] < pos_icon[1][1]:
                selected = True
            else:
                selected = False
            
            height = pos_icon[1][1] - pos_icon[0][1]
            width = pos_icon[1][0] - pos_icon[0][0]

            if selected == False:
                image = np.full((height, width, 4), 255, np.uint8)
            else:
                image = np.full((height, width, 4), 200, np.uint8)
                image = [[[x[0], x[0], x[0], 255] for x in image[y]] for y in len(image)]
                print(image)

                #draws outline around the selected icon
                top_left, top_right = pos_icon[0], (pos_icon[1][0], pos_icon[0][1])
                bot_left, bot_right = (pos_icon[0][0], pos_icon[1][1]), pos_icon[1]
                image = cv.line(image, top_left, top_right, [180, 180, 180], 2)
                image = cv.line(image, top_right, bot_right, [180, 180, 180], 2)
                image = cv.line(image, bot_right, bot_left, [180, 180, 180], 2)
                image = cv.line(image, bot_left, top_left, [180, 180, 180], 2)
            
            # composit icon and background that is visual indication of selection status
            # not shure if PIL is the moste efficient way of doing this.
            # The conversion to array and from array to Image is probably not the moste 
            # efficient way of doing thing either
            image = Image.fromarray(image, "RGBA")
            current_icon = np.array(current_icon)
            current_icon = Image.fromarray(current_icon)
            current_icon = current_icon.resize((50, 50))
            image = Image.alpha_composite(image, current_icon)

            # draw icons in the window
            window = window.copy()
            image = np.array(image.convert("RGB"))
            for y in range(len(image)):
                for x in range(len(image[0])):
                    window[y][x] = image[y][x]
            
            return window
