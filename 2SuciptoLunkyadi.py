#!/usr/bin/env python
"""
The original program recognizes the alphabets \sigma = {'a','b','c'}, the language of the original program is
	any word of length >=1 consisting of only alphabets inside of \sigma. The reason is, the only unaccepted
	state is if qs = [0]. However, delta(q,a) = 0 iff delta(q=2,a='c'). In the same time, there is another
	computation, delta(q=2,a='c') = 1. Thus, it accepts word using alphabets from \sigma of any length.
"""
# the description of the automaton starts here

q0 = 0

f = set([0, 2, 6, 10])

def delta(q, a):
    if q == 0:
        if a == 'a':
            return set([1])
        else:
            return set([0])
    elif q == 1:
        if a == 'l':
            return set([3])
        elif a == 'a':
            return set([2])
        else:
            return set([1])
    elif q == 2:
        if a == 'l':
            return set([7])
        elif a == 'a':
            return set([1])
        else:
            return set([2])
    elif q == 3:
        if a == 'g':
            return set([4])
        elif a == 'a':
            return set([2])
        else:
            return set([1])
    elif q == 4:
        if a == 'p':
            return set([5])
        elif a == 'a':
            return set([2])
        else:
            return set([1])
    elif q == 5:
        if a == 'r':
            return set([6])
        elif a == 'a':
            return set([2])
        else:
            return set([1])
    elif q == 6:
        return set([6])
    elif q == 7:
        if a == 'g':
            return set([8])
        elif a == 'a':
            return set([1])
        else:
            return set([2])
    elif q == 8:
        if a == 'p':
            return set([9])
        elif a == 'a':
            return set([1])
        else:
            return set([2])
    elif q == 9:
        if a == 'r':
            return set([10])
        elif a == 'a':
            return set([1])
        else:
            return set([2])
    elif q == 10:
        return set([10])


# the description of the automaton ends here

def recognize(word):
    qs = set([q0])
    for a in word:
        qs_prime = set()
        for q in qs:
            qs_prime.update(delta(q, a))
        qs = qs_prime
    print(qs)
    return f.intersection(qs)

def main(args):
    word = args[1]
    if recognize(word):
        print('word accepted')
    else:
        print('word NOT accepted')
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
