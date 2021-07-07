import random
import math
import copy

def first_fit_pack(lst,check=False):
    """
    Place the packs into bins by the first-fit algorithm.

    The algorithm try to place the packs (keeping their order) into
    the bins so that the next item is always placed in the first bin
    where it fits. If the pack does not fit in any of the bins, open 
    a new bin. (Every pack is measured by a number between 0 and 1,
    let us call the weight of it. Packs fit into a bin, if the sum 
    of their weights is not more than 1.)

    :param lst: List of the packs.
    :return:    The number of necessary bins.
    """
    pack = [1]
    item = 0
    for i in lst:
        item+=1
        it = 0
        while it < len(pack):
            if pack[it] >= i:
                pack[it] -= i
                ( print('Item {0} is in box{1}'.format(item,it+1)) ) if check == True else None
                break
            else:
                it += 1
                if it == len(pack):
                    pack.append(1-i)
                    ( print('Item {0} is in box{1}'.format(item,it+1)) ) if check == True else None
                    break
    return len(pack)

def ffd_pack(lst,check=False):
    """
    Place the packs into bins by the first-fit decreasing algorithm.

    The algorithm try to place the packs into the bins like in the
    previous algorithm but first sort them decreasing by weights.

    :param lst: List of the packs.
    :return:    The number of necessary bins.
    """
    items = copy.deepcopy(lst)
    items.sort(reverse=True)
    return first_fit_pack(items,check)

def best_fit_pack(lst,check=False):
    """
    Place the packs into bins by the best-fit algorithm.

    The algorithm try to place the packs (keeping their order) into
    the bins so that the next item is always placed in the bin
    where the omittance is minimal.

    :param lst: List of the packs.
    :return:    The number of necessary bins.
    """
    bins = []
    item = 0
    for pack in lst:
        item += 1
        max_fulness = -1.0
        max_pos = -1
        for i in range(len(bins)):
            if (bins[i] + pack <= 1.0) and (bins[i] > max_fulness):
                max_pos = i
                max_fulness = bins[i]
        if max_pos == -1:
            bins.append(pack)
            ( print('Item {0} is in box{1}'.format(item,len(bins))) ) if check == True else None
        else:
            bins[max_pos] += pack
            ( print('Item {0} is in box{1}'.format(item,max_pos+1)) ) if check == True else None
    return len(bins)

if __name__ == '__main__':
    # TODO Generate a random sequence of 1000 numbers between 0 and 1
    # instead of the next list:
    packs = [0.34, 0.34, 0.33, 0.33, 0.33, 0.33]
    packs2 = [random.random() for i in range(1000)]

    the_sum = math.ceil(sum(packs2)) 
    ff = first_fit_pack(packs2)
    ffd = ffd_pack(packs2)
    bf = best_fit_pack(packs2)

    print(f"OPT: {the_sum}")
    print(f" FF: {ff}")
    print(f"FFD: {ffd}")
    print(f" BF: {bf}")


print('''in general FFD < BF <FF

How BF works:
    - for item k, find all possible boxes where k still fits
    - if there is no such box, than open a new box
    - out of all these boxes, which box would be the fullest if k is packed there
    - pack k into the box that would be the fullest''')
    
