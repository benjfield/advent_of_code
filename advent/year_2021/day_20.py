from advent.runner import register

class Image:
    def __init__(
        self,
        light_pixels
        ):
        self.min_x = 0
        self.max_x = 0
        self.min_y = 0
        self.max_y = 0
        
        self.light_pixels = light_pixels

        for pixel in light_pixels:
            if pixel[0] < self.min_x:
                self.min_x = pixel[0]
            elif pixel[0] > self.max_x:
                self.max_x = pixel[0]
            elif pixel[1] < self.min_y:
                self.min_y = pixel[1]
            elif pixel[1] > self.max_y:
                self.max_y = pixel[1]

    def get_image_number(self, coord, outside_light):
        image_number = 0
        for y_number, y in enumerate(range(1, -2, -1)):
            for x_number, x in enumerate(range(1, -2, -1)):
                test_coord = (coord[0] + x, coord[1] + y) 
                if test_coord in self.light_pixels:
                    image_number += 2 ** ((y_number) *3 + x_number)
                elif outside_light and (test_coord[0] <= self.min_x - 1 or test_coord[0] >= self.max_x + 1 or test_coord[1] <= self.min_y - 1 or test_coord[1] >= self.max_y + 1):
                    image_number += 2 ** ((y_number) *3 + x_number)
        return image_number

    def show_image(self):
        for y in range(self.min_y, self.max_y + 1):
            line = ""
            for x in range(self.min_x, self.max_x + 1):
                if (x, y) in self.light_pixels:
                    line += "#"
                else:
                    line += "."
            print(line)

    def return_enhanced_image(self, image_enhancement_list, alternating_outside, iteration):
        light_pixels = set()
        outside_light = False
        if alternating_outside and iteration % 2 == 1:
            outside_light = True

        for y in range(self.min_y - 1, self.max_y + 2):
            for x in range(self.min_x - 1, self.max_x + 2):
                coord = (x, y)
                image_number = self.get_image_number(coord, outside_light)
                if image_enhancement_list[image_number]:
                    light_pixels.add(coord)

        return Image(light_pixels)

def process_text(text):
    split_text = text.split("\n")
    image_enhancement_string = ""
    light_pixels = set()
    finished_image_enhancement_string = False
    light_pixel_start = 0

    for y, line in enumerate(split_text):
        if len(line) == 0:
            finished_image_enhancement_string = True
            light_pixel_start = y + 1
        elif finished_image_enhancement_string:
            for x, char in enumerate(line):
                if char == "#":
                    light_pixels.add((x, y - light_pixel_start))
        else:
            image_enhancement_string += line

    image_enhancement_list = []
    for char in image_enhancement_string:
        if char == "#":
            image_enhancement_list.append(True)
        else:
            image_enhancement_list.append(False)

    return image_enhancement_list, light_pixels

    
@register(20, 2021, 1)
def image_enhancement_1(text):
    image_enhancement_list, light_pixels = process_text(text)

    alternating_outside = False
    if image_enhancement_list[0]:
        if image_enhancement_list[-1]:
            raise Exception("Not Implement")
        else:
            alternating_outside = True 

    image = Image(light_pixels)

    for i in range(2):
        image = image.return_enhanced_image(image_enhancement_list, alternating_outside, i)

    return len(image.light_pixels)
    
@register(20, 2021, 2)
def image_enhancement_2(text):
    image_enhancement_list, light_pixels = process_text(text)

    alternating_outside = False
    if image_enhancement_list[0]:
        if image_enhancement_list[-1]:
            raise Exception("Not Implement")
        else:
            alternating_outside = True 

    image = Image(light_pixels)

    for i in range(50):
        image = image.return_enhanced_image(image_enhancement_list, alternating_outside, i)

    return len(image.light_pixels)