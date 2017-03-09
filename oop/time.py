class Time:
    "save time object as a three digit number in base 60"
    def __init__(self, hours=0, minutes=0, seconds=0):
        # normalize againt user input: 20:70:90 => 21:11:30
        time = hours*3600 + minutes*60 + seconds
        self.hours, minutesAndSec = divmod(time, 3600)
        self.minutes, self.seconds = divmod(minutesAndSec, 60)

    def ToInt(self):
        # TODO change the definition to private ToInt
        return self.hours*3600 + self.minutes*60 + self.seconds

    def __str__(self):
        return "{0}:{1}:{2}".format(self.hours, self.minutes, self.seconds)

    def __add__(self, other):
        "return a new Time object"
        addResult = self.ToInt() + other.ToInt()
        return Time(0,0,addResult) #XXX so clever

        # XXX or if you want to use self.time as the data
        # addition = self.time + other.time
        # newTime = Time()
        # newTime.time = addition
        # return newTime

    def increment(self, secs):
        hours, minutesPlusSecs = divmod(secs,3600)
        minutes, seconds = divmod(minutesPlusSecs,60)
        # convert to base 60, then perform addition with carries
        self.seconds += seconds
        self.minutes += minutes
        self.hours += hours
        if self.seconds >= 60:
            self.seconds -= 60
            self.minutes += 1
        if self.minutes >= 60:
            self.minutes -= 60
            self.hours += 1

        #XXX better to use time(one integer to store, let computer do arithmetics)
        # __str__ is where we convert decimal to base 60

    def after(t, t1):
        return t.ToInt() > t1.ToInt()

def after(t1,t2):
    return t1.time > t2.time

if __name__ == "__main__":
    # add unit tests here
    current = Time(20,13,59)
    print(current)
    print(current.after(Time(21,10,11)))
    current.increment(500)
    print(current)
    print(current + Time(1,11,11))
