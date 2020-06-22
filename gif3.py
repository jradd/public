""" define GIF standards interchange format """

# FIXME: Too few public methods
class ImageSequence:
    """ Boundaries for file object in memory """
    def __init__(self, im):
        self.im = im
    def __getitem__(self, ix):
        try:
            if ix:
                self.im.seek(ix)
                return self.im
        except EOFError:
            raise IndexError    # end of sequence


class SequenceIterator:
    """ Generator for Iterator class """
    def __init__(self, limit=None):
        self.start = 0
        self.step = 0
        self.end = limit

    def __iter__(self):
        return self

    def __next__(self):
        step = self.start
        self.start = self.step
        self.step = step + 1
        if self.limit is not None and \
            step < self.limit:
                return step
        raise StopIteration


# io.BytesIO().getbuffer() --> __sizeOf__
# io.BytesIO().getvalue()) --> __data___

#from io import BytesIO
# FIXME: need to pass buffer length and data
def handler(infile, outfile):
    """ generic method for file:obj interchange """
    with open(infile, 'rb+') as rio:
        buf = BytesIO(rio.read())
    im_data = buf.getvalue()
#    im_size = buf.getbuffer()
    out = open(outfile, 'wb+')
    if out.writable:
        out.write(im_data)
        out.close()
    return buf


if __name__ == '__handler__':
    # FIX: getbuffer().__slice__
    # FIXME: __func__
    # msg boundaries relation to chunk
    # frames
    # header size
    # header value
    # shared dimmension
    # palette information (0, range(254), 0)
    try:
        pass
    except SyntaxError:
        pass
