import struct
import io
import socket
def int_to_nbyte(n):
    if n < (1 << 8):
        tag = 'B'
    elif n < (1 << 16):
        tag = 'H'
    elif n < (1 << 32):
        tag = 'L'
    else:
        tag = 'Q'
    return tag.encode('utf-8') + struct.pack('!' + tag, n)

def nbyte_to_int(source):
    read_bytes = lambda d, s: (d[:s], d[s:])
    read_file = lambda d, s: (d.read(s), d)
    read_socket = lambda d, s: (d.recv(s), d)
    readers = {
        bytes: read_bytes,
        io.IOBase: read_file,
        socket.socket: read_socket
    }
    size_info = {'B': 1, 'H': 2, 'L': 4, 'Q': 8}

    reader = readers[type(source)]

    btag, source = reader(source, 1)
    tag = btag.decode('utf-8')
    if not tag in size_info:
        raise TypeError("Invalid type: " + type(tag))

    size = size_info[tag]
    bnum, source = reader(source, size)
    return struct.unpack('!' + tag, bnum)[0], source

def str_to_nbyte(s):
    tag, s_byte = ("s", s) if isinstance(s, bytes) else("c", s.encode("utf-8"))
    nbyte = int_to_nbyte(len(s_byte))
    # print(tag)
    # print(s_byte)
    # print(nbyte)
    return tag.encode("utf-8") + nbyte + s_byte

def nbyte_to_str(source):
    read_bytes = lambda d, s: (d[:s], d[s:])
    read_file = lambda d, s: (d.read(s), d)
    read_socket = lambda d, s: (d.recv(s), d)
    readers = {
        bytes: read_bytes,
        io.IOBase: read_file,
        socket.socket: read_socket
    }

    reader = readers[type(source)]

    #取得tag
    btag, source = reader(source, 1)
    tag = btag.decode('utf-8')

    #判斷tag是否正確
    if tag not in ['s', 'c']:
        raise TypeError("Invalid type: " + type(tag))

    #取得長度
    size, source = nbyte_to_int(source)

    #依照長度取得bytes格式字串
    bstr, source = reader(source, size)

    #如果是str就將bytes 轉回成str
    return bstr if tag == 's' else bstr.decode("utf-8")
