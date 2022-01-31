class Car:
    route = []
    current_street_index = 0
    pos_along_street = 0
    at_intersection = False
    complete = False

    def update(self):
        if self.complete :
            return 

        if not(self.at_intersection) :
            self.pos_along_street += 1

        if self.pos_along_street >= self.route[self.current_street_index].time :
            self.route[self.current_street_index].add_to_queue(self)
            self.at_intersection = True

            if self.current_street_index == len(self.route) :
                self.complete = True


    def moveAcrossIntersection(self):
        self.at_intersection = False
        self.current_street_index += 1

    def loadRouteData(self, route_data_string, all_streets):
        route_data = route_data_string.split()
                    
        for i in range(len(route_data) - 1):
            for s in all_streets:
                if s.name == route_data[i + 1]:
                    route.append(s)
                    break


        