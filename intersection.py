from asyncio.windows_events import NULL


class intersection:
    id = 0
    schedule = []
    in_streets = []
    curr_street = 0
    curr_time = 0

    def update(self):
        if self.current_time == self.curr_street.robot.time:
            self.curr_street += 1
            self.current_time = 0
            self.in_streets[self.schedule[self.curr_street]].robot.state = True
            self.in_streets[self.schedule[self.curr_street - 1]].robot.state = False
        else :
            self.current_time += 1
            self.in_streets[self.schedule[self.curr_street]].robot.queue.top.moveAcrossIntersection()
