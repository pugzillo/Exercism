import random
import string 

class Robot(object):
    oldnames = list()   # List holding all robot names

    def __init__(self):
        self.name = self.genName()

    # Generates new robot names
    def genName(self):
        temp_name = ''.join(random.sample(string.ascii_uppercase, 2)) + ''.join(random.sample(string.digits,k=3))
        if temp_name in Robot.oldnames:
            return self.genName()
        Robot.oldnames.append(temp_name)
        return temp_name

    def reset(self):
        self.name = self.genName()

    



