# import re


class Phone(object):
    def __init__(self, phone_number):
        self.number = self.clean_number(phone_number)   # properties of class Phone
        self.area_code = self.clean_number(phone_number)[0:3]

    # Function to clean phone numbers
    def clean_number(self, phone_number):
        # number = re.findall('\\d', phone_number)
        number = [a for a in list(phone_number) if a.isnumeric()] # Loop to remove non numeric characters
        # print(number)
        # print(len(number))

        if len(number) == 11 and number[0] == '1':  # Remove international 1
            number = number[1:]

        if number[0] in ['0', '1']: 
            raise ValueError("Phone number starts with 0 or 1!")

        # print(number[3])
        if number[3] in ['0', '1']:
            raise ValueError("Exchange code starts with 0 or 1!")
 
        if len(number) != 10:
            raise ValueError("Phone number doesn't have 10 digits!")
        
        return(''.join(number))

    def pretty(self):
        return("(" + self.number[0:3] + ") " + self.number[3:6] + "-" + self.number[6:10])
