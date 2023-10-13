import cv2
import numpy as np

img = np.full((500, 500, 3), 255, np.uint8)

def draw_triangel(canvas:list , centerpoint:tuple, sidelenght:int, thickness:int, color):
    height = round(sidelenght*((3**(1/2)/2)))
    top = (centerpoint[0], round(centerpoint[1]-height/2))
    left = (round(centerpoint[0]-sidelenght/2), round(centerpoint[1]+height/2))
    right = (round(centerpoint[0]+sidelenght/2), round(centerpoint[1]+height/2))

    image = cv2.line(canvas, top, left, color, thickness)
    image = cv2.line(image, top, right, color, thickness)
    image = cv2.line(image, left, right, color, thickness)

    return image

def stack_based_fill(canvas:list, point:tuple, color:list):
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
                        image[x[1]][x[0]] = color

            pixels_front = []
            cv2.imshow("Drawline", image)

            for pixel in new_front:
                pixels_front.append(pixel)

            new_front = []

def Mouse_event(event, x, y, flags, params)

image = draw_triangel(img, (250, 250), 500, 3, (0, 0, 0))

cv2.imshow("Drawline", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
