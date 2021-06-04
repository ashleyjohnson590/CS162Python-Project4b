#Author: Ashley Johnson
#Date: 4/16/2021
#Description: Program uses insertion sort to sort a list of boxes from greatest volume to least.
class Box:
    """class initializes 3 private members: length, width, and height. Volume returns the volume
    of the box"""
    def __init__(self,length, width, height):
        self._length = length
        self._width = width
        self._height = height
    def volume(self):
        """returns volume of box"""
        volume = self._length * self._width * self._height
        return volume
    def get_length(self):
        """returns length of box"""
        return self._length
    def get_width(self):
        """returns width of box"""
        return self._width
    def get_height(self):
        """returns height of box"""
        return self._height

def box_sort(box_list):
    """uses insertion sort to sort a list of boxes from greatest volume to least."""
    for index in range(1, len(box_list)):
        value = box_list[index]
        pos = index - 1
        while pos >= 0 and box_list[pos].volume() < value.volume():
            box_list[pos + 1] = box_list[pos]
            pos -= 1
        box_list[pos + 1] = value
