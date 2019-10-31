def bignum_to_bytes(n):
    result = b''
    while n > 0:
        b = n % 128
        n >>= 7
        if n:
            b+=128
        result += bytes([b])
    return result

def bytes_to_bignum(bs):
    result = 0
    exp = 0
    for b in bs:
        print("b:",b)
      
        n = b % 128
        print("n:",n)
        result += n << exp
        print("result:",result)
        exp += 7
        if b & (1 << 7) == 0:
            break
    return result
