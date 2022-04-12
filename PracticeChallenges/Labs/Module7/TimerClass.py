class Timer:
    def __init__(self, hrs=0, min=0, sec=0 ):
        self.hrs = hrs
        self.min = min
        self.sec = sec
        if sec >= 60 | min >= 60 | hrs >= 24:
            raise IndexError

    def __str__(self):
        hh = str(self.hrs).ljust(2, '0')
        mm = str(self.min).ljust(2, '0')
        ss = str(self.sec).ljust(2, '0')
        return f"{hh}:{mm}:{ss}"

    def next_second(self): #increments second
        self.sec +=1 # add second
        if self.sec == 60: #check for time overflow
            self.sec = 0 #reset and repeat with next value
            self.min += 1
            if self.min == 60:
                self.min = 0
                self.hrs += 1
                if self.hrs == 24:
                    self.hrs = 0

    def prev_second(self):
        self.sec -=1 #subtract second
        if self.sec == -1: #check for time underflow
            self.sec = 59 #reset and repeat with next value
            self.min -= 1
            if self.min == -1:
                self.min = 59
                self.hrs -= 1
                if self.hrs == -1:
                    self.hrs = 23


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
