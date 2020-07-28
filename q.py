"""Attemp to use heap"""

BUFFER = b'47494638396101000100800000000000ffffff21f90401000000002c000000000100010000020144003b'
task = {}
priority = []
priorities = ()

#class ImageSequence:
#  def __init__(self, im):
#    self.im = im
#
#  def __getitem__(self, ix):
#    try:
#      if ix:
#        self.im.seek(ix)
#      return self.im
#    except EOFError:
#      raise IndexError   # end of sequence
#

def _chunk_bs(bs, step=2):
    """chunk by step count"""
    stop = len(bs)
    start = 0
    bs_to_list = []
    for bstep in range(0, stop, step):
        bs_to_list.insert(bstep, bs[start:bstep+step])
        start = start + step
    return bs_to_list



class Mapping:
    """sub classed object for transitive updates"""
    def __init__(self, iterable):
        self.entries = []
        self.__update(iterable)

    def update(self, iterable):
        """instance class object"""
        for entry in iterable:
            self.entries.append(entry)

    __update = update


class MappingSubclass(Mapping):
    """Instance class override"""
    def update(self, keys, values):
      # provides new signature for update()
      # but does not break __init__()
        for entry in zip(keys, values):
            self.entires.append(entry)


class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.count = 0
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.count = self.count + 1
        self.index = self.index - 1
        return self.data[self.index]



def heappush(heap, item):
    """Push the item onto the heap, maintaining the heap invariant."""
    heap.append(item)
    _siftdown(heap, 0, len(heap)-1)

def heappop(heap):
    """Pop the smallest item off the heap, maintaining the heap invariant."""
    lastelt = heap.pop()
    if heap:
        returnitem = heap[0]
        heap[0] = lastelt
        _siftup(heap, 0)
        return returnitem
    return lastelt


def heapify(x):
    """ O(len(x)) linear time """
    n = len(x)
    for i in reversed(range(n//2)):
        _siftup(x, i)



def _siftdown(heap, startpos, pos):
    newitem = heap[pos]
    # follow the path to the root, moving parents down until finding a place
    # newitem fits.
    while pos > startpos:
        parentpos = (pos -1) >> 1
        parent = heap[parentpos]
        if newitem < heap[pos]:
            heap[pos] = parent
            pos = parentpos
            continue
        break

    heap[pos] = newitem

def _siftup(heap, pos):
    endpos = len(heap)
    # assuming length is counting literal
    # types?
    startpos = pos
    newitem = heap[pos]
    # Bubble up the smaller child until hitting a leaf.
    childpos = 2*pos + 1
    while childpos < endpos:
        # Set childpos to index of previous index
        rightpos = childpos + 1
        # avoid IndexError
        if rightpos < endpos and not heap[childpos] < heap[rightpos]:
            childpos = rightpos
       # increment index
        heap[pos] = heap[childpos]
        pos = childpos
       # Blow another Bubble
        childpos = 2*pos + 1
    # The leaf at pos is empty now.
    # Sift the parents down.
    heap[pos] = newitem
    _siftdown(heap, startpos, pos)


#if __name__ == "__main__":
#    from heapq import heappush, heappop
#    heapq = []
#    data = [1, 3, 5, 7, 11, 13, 1, 7, 2, 0]
#    for item in data:
#        heappush(heapq, item)
#    sort = []
#    while heapq:
#        sort.append(heappop(heapq))
#    print(sort)
