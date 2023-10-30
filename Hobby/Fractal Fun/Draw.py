import numpy as np
from PIL import Image

class draw():
    def __init__(self, res:tuple) -> None:
        """initiates the draw class with a canvas

        Args:
            res (tuple): the resolution of the canvas, takes a tuple of lengt 2
        """
        self.canvas = np.full((res[1], res[0], 3), 255, np.uint8)
        self.uppdate()
        
    def plot_line(self, from_coords:tuple, to_coords:tuple, thicknes:int, colour:list, canvas:np.zeros):
        """takes the coordinates for two points (from and to) and draws a line between them

        Args:
            from_coords (tuple): a tuple with two ints that represent the coordinates of a point on the canvas
            to_coords (tuple): same as from
            thicknes (int): the thicknes of the line
            colour (list): list of three RGB values
            canvas (np.zeros): a 2d grid of zeroes representing each pixel in an immage
        """

        if from_coords[1] > len(canvas[0]) or to_coords[1] > len(canvas[0]) \
            or from_coords[0] > len(canvas) or to_coords[0] > len(canvas):
            print("theese coordinates are outside of the image")


        # define coordinates based on x and y instead of to and from
        x_cords = [from_coords[0], to_coords[0]]
        y_cords = [from_coords[1], to_coords[1]]

        horizontal_distance = x_cords[0] - x_cords[1]
        vertical_distance = y_cords[0] - y_cords[1]

        distance = (horizontal_distance**2 + vertical_distance**2)**(1/2)

        #find the number of steps needed to be taken between each itteration in either direction
        if horizontal_distance == 0:
            horizontal_step = 0
        else:
            horizontal_step = horizontal_distance/distance

        if vertical_distance == 0:
            vertical_step = 0
        else:
            vertical_step = vertical_distance/distance

        for i in range(round(distance)):

            # uses min function because we want to start in the point that has 
            x = round(x_cords[1]+(i*horizontal_step))
            y = round(y_cords[1]+(i*vertical_step))

            for i in range(-thicknes, thicknes):
                for j in range(-thicknes, thicknes):
                    if x+i < 0 or x+i >= 500:
                        continue
                    if y+j < 0 or y+j >= 500:
                        continue

                    canvas[y+j][x+i] = colour

    def stack_based_fill(self, point:tuple, color:list):
        """takes a canvas color and point and changes every pixel of the same color in that regeon to the chosen color

        Args:
            color (list): list of rgb values
            point (tuple): tuple containing x and y coordinates for the startingpoint of a fill
        """
        pixels_front = []
        pixel_color = self.canvas[point[1]][point[0]].copy()
        pixels_front.append(point)
        new_front = []

        while len(pixels_front) > 0:
            for pixel in pixels_front:
                neighbours = [(pixel[0]+1, pixel[1]), (pixel[0], pixel[1]+1), (pixel[0]-1, pixel[1]), (pixel[0], pixel[1]-1)]

                for x in neighbours:
                    if f"{self.canvas[x[1]][x[0]]}" == f"{pixel_color}":
                        new_front.append(x)
                        self.canvas[x[1]][x[0]] = color

            self.uppdate()
            pixels_front = []

            for pixel in new_front:
                pixels_front.append(pixel)

            new_front = []
            
            

    def span_fill(self, point):
        ...

    def draw_triangle(self, center:tuple, side_length:int, thicknes:int, color:list):
        """takes draws a triangle around a center point

        Args:
            center (tuple): x and y coordinates that are the center of the triangle
            side_length (int): size of triangle
            thicknes (int): line thicknes
            color (list): color of lines as a list of rgb values
        """

        height = round(side_length*((3/2)**1/2))
        top_corner = [center[0], center[1]-height/2]
        left_corner = [center[0]-side_length/2, center[1]+side_length/2]
        right_corner = [center[0]+side_length/2, center[1]+side_length/2]

        self.plot_line(top_corner, left_corner, thicknes, color, self.canvas)
        self.plot_line(top_corner, right_corner, thicknes, color, self.canvas)
        self.plot_line(left_corner, right_corner, thicknes, color, self.canvas)

        self.uppdate()

    def triangle_on_triangle(self, center, side_length, thicknes, color, iterations):
        self.draw_triangle(center, side_length, thicknes, color, self.canvas)

    def show(self):
        image = Image.open("image.png")
        image.show("image.png")

    def uppdate(self):
        image = Image.fromarray(self.canvas)
        image.save("image.png")



canvas = draw((500, 500))
canvas.show()
canvas.draw_triangle((250, 250), 500, 1, [255, 215, 0])
canvas.stack_based_fill((250, 250), [255, 215, 0])