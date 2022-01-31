from asyncio.windows_events import NULL


class intersection:
    id = 0
    #a list of order indexes of in_streets
    schedule = []
    #list of streets coming in intersection
    in_streets = []
    curr_street = 0
    curr_time = 0

    def update(self):
        if self.current_time == self.curr_street.robot.time:
            self.curr_street += 1
            self.current_time = 0
            self.in_streets[self.schedule[self.curr_street]].robot.state = True #set next robot in shcedule to green
            self.in_streets[self.schedule[self.curr_street - 1]].robot.state = False #Set previous robot in schedule to red

            if(self.curr_street > len(self.schedule)) :
                self.curr_street = 0

        else :
            self.current_time += 1
            self.in_streets[self.schedule[self.curr_street]].robot.cars_queued.nextCar().moveAcrossIntersection()
