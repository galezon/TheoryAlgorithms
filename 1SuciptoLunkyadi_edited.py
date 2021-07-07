import sys

"""
  I encoded this program myself, did not copy or rewrite the code of others,
  and did not give or send it to anyone else.  

  Lunkyadi Sucipto
"""
def prepare(text):
    with open(text,'r') as f:
        x = f.read()
    x.strip()
    return x 

def simple_search(text,pattern):
    shift = 0
    current = 0
    comparisons = 0
    while shift <= len(text) - len(pattern) :
        if current == len(pattern):
            return (comparisons,shift + 1)
        elif text[shift + current] == pattern[current]:
            current += 1
        else:
            current = 0
            shift += 1
        comparisons += 1
    return [comparisons]

def preprocess(pattern):
    res = {}
    temp = []
    for i in pattern:
        temp.insert(0,i)
    a = ''.join(temp)
    counter = 1
    for i in a:
        res.setdefault(i,counter)
        counter += 1
    return res
        

def quick_search(text,pattern):
    prep = preprocess(pattern)
    current,shift,comparisons = 0,0,0
    while shift <= len(text) - len(pattern):
        comparisons += 1
        if text[current + shift] == pattern[current]:
            current += 1
            if current == len(pattern):
                return (comparisons, shift + 1)
        else:
            current = 0
            try:
                shift += prep.get( text[shift + len(pattern)], len(pattern) + 1)
            except IndexError:
                return [comparisons]
    return [comparisons]

def main():
    a = prepare(sys.argv[1])
    simple = simple_search(a,sys.argv[2])
    quick = quick_search(a,sys.argv[2])
    if len(simple) == 2:
        print('Simple Matching: {:5} comparisons, the pattern starts at {:4}'.format(simple[0],simple[1]))
        print('Quick Matching: {:5} comparisons, the pattern starts at {:4}'.format(quick[0],quick[1]))
    else:
        print('Simple Matching: {:5} comparisons, no pattern'.format(simple[0]))
        print('Quick Matching: {:5} comparisons, no pattern'.format(quick[0]))





if __name__ == '__main__':
    main()