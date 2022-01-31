class street:
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