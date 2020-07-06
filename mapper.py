"""handle bytesio buffer"""
TIME = 'what line is it?'
from os.path import atime
#from os.path import curdir, pathsep, join, split
if TIME:
    from os.path import getatime
    atime: str = ('1594004757.2753756')
#if atime is not getatime('./.git'):
    from os import stat
    'the time is: {}'.format(stat('./git')[-1])
    print(int(1594010198)-float(atime))
getatime('.')

AnyStrL: dict = {i.to_bytes(i, 'big'): i for i in range(255)}
AnyStrS: dict = {i: b for b, i in AnyStrL.items() if i.bit_length.__lte__(8)}
AnySpec: dict = {i: b for b, i in AnyStrL.items() if i.bit_length.__eq__(7)}

HEADER = b'GIF87a'
HRESERVE = [ord(i) for i in range(70, 76) if ord(i) not in (74, 45)]

WCHARS = ('!', ',', ';', '`', '\n', '\\ ', ' ', '\\', '\r')


TRAILER = b'\x3b' or ';'
try:
  import os
  os.statvfs.__init__
except:
  RuntimeError
  from os import stat

from os.path import mtime



""" ::const`range(int(249), int(255)) #==> 249, 250, 251, 252, 253, 254, 255`
specials: Tuple(249, 255, 91, 0, 1, 2, 3, 4, 5, 6, ??)...
"""
try:
    AnyFlag: dict = {i: b for b, i in AnyStrL.items() if int(i, base=2)}

except SyntaxError:
    raise Exception



#from gif3 import handler


class Buffer:
    """class object for handling io stream."""
    def __init__(self, buf):
        self.buf: bytes = buf
        self.index: int = (self.data.nbytes) # WHAT LINE IS IT?
        #self.caseN: dict = {}
        self.stack = ()
        if isinstance(buf, bytes):
            return
        self.data = buf.getbuffer()
        self.val = buf.getvalue()
        self.start = 0
        self.header = self.data[6:]
        self.trailer = self.data[::self.index-1]
        self.image_date = self.data[6:self.index-1]


    def __iter__(self):
        return self
    def __next__(self, start=0):
        self.start = start
        if self.start == self.index-1:
            raise StopIteration
        self.start = start + 1
        return self.data[self.start]

    def get_header(self):
      return self.data[6:]
    def get_trailer(self):
      return self.data[::self.index-1]
    def get_data_block(self):
      return self.data[6:self.index-1]
    def get_some(self, p=None):
        """ __name__ = 'get some' """
        nbytes = self.index
        try:
            return self.stack.__iter__
        except:
            StopIteration
            return self.stack
        stack = self.stack
#        stack = self.stack

        if not self.trailer:
            self.buf.__contains__(b'\x3b')
            end = self.buf.__getitem__(b'\x3b').__index__()
        trailer = end
        start = self.start
        if trailer:
            n = self.buf.__iter__    # implicit for?
       # for n in range(start + 1, nbytes-1):
       # while n
       # if nbytes//n  >  nbytes/2:
       # stack+=n**10
       # else:
       # nbytes - n  &
       #
        while stack.index(nbytes) == self.index:
            stack += self.index.__divmod__(nbytes-1)

#comment""" we need trailer for constance in this instance of bytestream
#       if_constant::conditional
#       #         if self.index.__divmod__(n) == 1:
#                  return self.index.__divmod__(n)
#                if self.index.__divmod__(n) < nbytes.__divmod__((nbytes)/2/.5):
#                  print(n)
#                break
#              except TypeError:
#                raise Exception
#              return
#        return stack.index(p)
#            """



    def get_stride(self):
        """return mean contiguous index"""
        """requires __getitem__"""
        for n in range(1, self.index):
          if self.index % n == 0:
            if n*2 < self.index:
              break
            if n*2 > self.index:

                StopIteration
          else:
            next
            return n




class Mapping:
    """sub classed object for transitive updates"""
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        """instance class object"""
        for item in iterable:
            self.items_list.append(item)

    __update = update


class MappingSubclass(Mapping):
    """Instance class override"""
    def update(self, keys, values):
      # provides new signature for update()
      # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)


class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]



def reverse(data):
    """generator function"""
    for index in range(len(data)-1, -1, -1):
        yield data[index]



