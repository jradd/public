""" simple number functions """

def get_even(number):
    """ return 0 padded list followed by odd integer
    working
    """
    even = [int(x) for x in range(0, number, 2)]
    odds = [[0] * (number)]
    for i in range(1, number):
        if i in even:
            odds.insert(i-1, i-1)
    if number-2 in even:
        odds.append(number - 1)

    return odds

def get_some(number):
    """ do something with odds """
    odds = get_even(number)
    count = len(odds)
    for i in range(1, count):
        print(odds[i])



def permute(list):
    if not list:                           # shuffle a sequence
        return [list]                        # empty sequence
    else:
        res = []
        for i in range(len(list)):
            rest = list[:i] + list[i+1:]       # delete current node
            for x in permute(rest):            # permute the others
              res.append(list[i:i+i] + x)      # add node at front
        return res

def subset(list, size):
    if size == 0 or not list:             # order matters here
        return [list[:0]]
    else:
        result = []

    for i in range(len(list)):
        pick = list[i:i+1:]                 # sequence slice
        rest = list[:i] + list[i+1:]        # keep [:i] part
    for x in subset(rest, size-1):
        result.append(pick + x)
    return result


def combo(list, size):
    if size == 0 or not list:             # order doesn't matter
        return [list[:0]]                   # xyz == yzx
    else:
        result = []
        for i in range(0, (len(list) - size) + 1):
            pick = list[i:i+1]
            rest = list[i+1:]                 # drop [:i] part
        for x in combo(rest, size - 1):
            result.append(pick + x)
        return result

def inc_slice(step, stop):
    start = 0
#    s0 = ""
    s1 = []
#    s0 +- str(step)
    for i in range(start, stop, step):
        s1.insert(i, (start+i, i+step))
    s1.insert(len(s1)+1, (stop-step, stop))
#    for i, j in s1:
#        s0 += '{}:{}, '.format(i, j)
    return s1

def get_stride(stop, ndim=5):
    if stop % 2 == 0:
        stop = stop - 1
    for i in range(1, stop):
        if stop % i == 0:
            if stop /i <= stop:
                if stop / i == ndim*2:
                    print(i)
                if stop / i == ndim:
                    return i


if __name__ == '__main__':
    try:
        from gif3 import handler
    except ImportError:
        raise Exception
    INFILE = './pascal.gif'
    OUTFILE = './tmp.gif'
    ooh = handler(INFILE, OUTFILE)
    nohead = ooh.getbuffer()[6:]
    stop = nohead.nbytes
    slices = inc_slice(get_stride(stop), stop)
    view = []
    for i, j in slices:
        view.append(nohead[i:j])
    print(view[-1].tolist())




