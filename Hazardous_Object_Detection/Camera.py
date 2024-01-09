import cv2
class camera:
    def __init__(self):
        self.__ret = None
        self.__frame = None

        self.x = None
        self.y = None
        self.w = None
        self.h = None

    def turn_on_carmera(self):
        return True

    def turn_off_camera(self):
        return False

    def draw(self):
        pass

    def __del__(self):
        pass