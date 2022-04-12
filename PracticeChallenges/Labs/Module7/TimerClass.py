class Timer:
    def __init__(self, hrs=0, min=0, sec=0 ):
        self.hrs = hrs
        self.min = min
        self.sec = sec
        if sec >= 60 | min >= 60 | hrs >= 24:
            raise IndexError

    def __str__(self):
        return f"{self.hrs}, {self.min}, {self.sec}"

    def next_second(self):
        self.sec +=1
        if self.sec == 60:
            self.sec = 0
            self.min += 1
            if self.min == 60:
                self.min = 0
                self.hrs += 1
                if self.hrs == 24:
                    self.hrs = 0

    def prev_second(self):
        self.sec -=1
        if self.sec == -1:
            self.sec = 59
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


#There is a module for this