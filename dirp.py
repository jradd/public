""" handle bytes io """
from os.path import exists

def bio(fname, data):
    """ copy file without appending to the obj-like buffer"""
    buf = b''
    buf += data
#    if exists(fname):
#      ff = open(fname, 'rb+')
##      ff.write(b'abc')
#    print(ff.read(200))
    if exists(fname):
        print('exists')
        f = open(fname + 'out', 'wb', buffering=200)
    else:
        # file does not exist
        print('doesnt exist')
        f = open(fname, 'wb+', buffering=200)          # create handle
        f.write(data)
    with open(fname, 'rb+') as rio:
        print('rio', rio.seek(0), rio.read(200))
        rio.seek(0)
#        print(len(data), rio.seek(0), rio.read(20000)
        rio.flush()
        f.write(rio.read(200))
        rio.seek(0)
        return rio.read(200)
    f.close()
