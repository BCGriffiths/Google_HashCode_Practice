class robot:
    #Robot has two states: true- "green" and false- "red"
    def __init__(self, state, time_enabled):
        self.state = state
        self.time_enabled = time_enabled
        self.cars_queued = []

    def getState(self):
        return self.state

    def getTimeEnabled(self):
        return self.time_enabled

    def setState(self, state_change):
        self.state = state_change

    def setTimeEnabled(self, time_change):
        self.time_enabled = time_change

    def addCarQueued(self, add_car):
        self.cars_queued.append(add_car)

    #returns next car in queue and removes it
    def nextCar(self):
        next_car = self.cars_queued[0]
        self.cars_queued.pop(0)
        return next_car