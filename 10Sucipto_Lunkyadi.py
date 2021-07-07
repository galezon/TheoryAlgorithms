from operator import itemgetter
import sys

class Acrobat:
    """
    A class containing the data of an acrobat
    """

    def __init__(self, identifier, height, weight):
        """
        Initialize a new Acrobat object.

        :param identifier: identification number of acrobat
        :param height: height of acrobat
        :param weight: weight of acrobat
        """
        self.id = identifier
        self.height = height
        self.weight = weight

    def may_stand_on(self, other):
        """
        Desides if the acrobat may stand on the other acrobat.

        :param other: another acrobat the actual acrobat wants to stand on.
        :returns: True, if the acrobat may stand on the other, otherwise False.
        """
        return self.weight < other.weight and self.height < other.height

    def __str__(self):
        """
        Convert the acrobat into string

        :returns: the string representation of the acrobat
        """
        return 'Acrobat ' + str(self.id) + ': height = ' + str(self.height) + ', weight = ' + str(self.weight)

def read_acrobats(file):
    with open(file,'r') as f:
        n = int(f.readline())
        acrobats = []
        for i in range(n):
            m, s = [int(a) for a in f.readline().split()]
            acrobats.append(Acrobat(i+1, m, s))
    return acrobats

def tryy3(file):
    a = read_acrobats(file)
    a.sort(key=lambda x: x.weight) #acrobats sorted by increasing weight
    mem_tab = [0]*len(a)
    for i in range( len(a) ):
        j = i-1
        max_stand = 0
        while j>=0  and j >= max_stand :
            if  a[j].may_stand_on(a[i]) and mem_tab[j] > max_stand  :
                max_stand = mem_tab[j]
            j-=1
        mem_tab[i] = max_stand + 1
    return max(mem_tab)

def main():
    a = tryy3(sys.argv[1])
    print(a)    


if __name__ == '__main__':
    main()

