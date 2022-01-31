from asyncio.windows_events import NULL


class intersection:
    id = 0
    schedule_street_indices = []
    in_streets = []
    curr_street = 0
    curr_time = 0

    def update(self):
        if self.current_time == self.curr_street.robot.time:
            self.curr_street += 1
            self.current_time = 0
            self.in_streets[self.curr_street].robot.enabled = True
            self.in_streets[self.curr_street - 1].robot.enabled = False
        else :
            self.current_time += 1
            self.in_streets[self.curr_street].queue.top.moveAcrossIntersection()
