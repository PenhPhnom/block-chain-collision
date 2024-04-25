import random
def mHash():
    metax = []
    for i in range(64):
        bx = str(random.choice('0123456789abcdef'))
        metax.append(bx)
    hashstring = ''.join(metax)
    return hashstring

def mhex128():
    letgt = []
    for i in range(128):
        let = str(random.choice('0123456789abcdef'))
        letgt.append(let)
    hashstring = ''.join(letgt)
    return hashstring
    


