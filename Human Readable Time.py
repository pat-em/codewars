import math

def make_readable(seconds):
    hour = math.floor(seconds/3600)
    rest_after_h = seconds % 3600
    minute = math.floor(rest_after_h/60)
    second = rest_after_h % 60
    hour = ("0" + str(hour)) if hour<10 else hour
    minute = ("0" + str(minute)) if minute<10 else minute
    second = ("0" + str(second)) if second<10 else second

    print_time = "{}:{}:{}".format(hour, minute, second)
    return print_time

print(make_readable(0))

##########################33
def make_readable(s):
    return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)