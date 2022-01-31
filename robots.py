class robot:
    def __init__(self, state, time_enabled):
        self.state = state
        self.time_enabled = time_enabled

    def getState(self):
        return self.state

    def getTimeEnabled(self):
        return self.time_enabled

    def setState(self, state_change):
        self.state = state_change

    def setTimeEnabled(self, time_change):
        self.time_enabled = time_change