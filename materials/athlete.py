def get_coach_data(filename):
    with open(filename) as f:
        line = f.readline()
    return line.strip().split(',')

class Athlete:
    def __init__(self,a_name,a_dob=None,a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times
    def top3(self):
        return sorted(set([self.sanitize(t) for t in self.times]))[0:3]
    def sanitize(self,time_string):
        if '-' in time_string:
            splitter = '-'
        elif ':' in time_string:
            splitter = ':'
        else:
            return (time_string)
        (mins,secs) = time_string.split(splitter)
        return (mins+'.'+secs)


class Rugby(Athlete):
    def __init__(self,a_name,a_bod,a_squat,a_times):

        Athlete.__init__(self,a_name,a_bod,a_times)

        self.squat = a_squat
    def top3(self):
        return sorted([self.sanitize(t) for t in self.times])[-3:]


class OtherAthlete(Athlete):
    def __init__(self,a_name,a_bod,a_squat,a_times):

        Athlete.__init__(self,a_name,a_bod,a_times)

        self.squat = a_squat
    def top3(self):
        return sorted([self.sanitize(t) for t in self.times])[0:3]
