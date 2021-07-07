import sys

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        
    def __str__(self):
        return '[' + str(self.start) + ', ' + str(self.end) + ']'
    def measure():
        return (Interval.b-Interval.a)

def read_intervals(file):
    with open(file,'r') as f:
        n = int(f.readline())
        intervals = []
        for i in range(n):
            s, e = [int(iv) for iv in f.readline().split()]
            intervals.append(Interval(s,e))
    return intervals

def measure( lis ):
    lis.sort(key=lambda x: x.start)
    curr = [ [ lis[0].start,lis[0].end ] ] #initializing curr
    for i in lis:
        if i.start > curr[-1][1]: #if A_i > current intervals, then we want a new one
            curr.append([i.start, i.end])
        elif i.end > curr[-1][1]:
            curr[-1][1] = i.end
    meas=0
    for i in curr:
        meas += (i[1]-i[0])
    return meas

if __name__ == '__main__':
    a = read_intervals(sys.argv[1])
    b = measure(a)
    print(b)