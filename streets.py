class street:
    start_loc = NULL


    def __init__(self, start_loc, end_loc, name, time):
        self.start_loc = start_loc
        self.end_loc = end_loc
        self.name = name
        self.time = time

    def getStartLoc(self):
        return self.start_loc

    def getEndLoc(self):
        return self.end_loc

    def getName(self):
        return self.name

    def getTime(self):
        return self.time

    def loadStreetData(self, input_string):
        string_list = input_string.split()
        self.start_loc = string_list[0]
        self.end_loc = string_list[1]
        self.name = string_list[2]
        self.time = string_list[3]
