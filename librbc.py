def splitter(num, bytesize):# source bytesize is 3 for hexa, 4 for octal, 12 for binary
    d = [v for v in num.split('.')[0]]
    f = [v for v in num.split('.')[1]]
    while len(d)%bytesize != 0:
        d.insert(0, '0')
    while len(f)%bytesize != 0:
        f.append('0')
    return [d,f]

def binModifier(num, bytesize):# destination bytesize is 3 for octal 4 for hexa
    x = len(num[0])/bytesize
    d = [''.join(num[0][bytesize*i:bytesize*(i+1)]) for i in range(int(x))]
    y = len(num[1])/bytesize
    f = [''.join(num[1][bytesize*i:bytesize*(i+1)]) for i in range(int(y))]
    return [d,f]

hexa = {'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111','8':'1000','9':'1001','a':'1010','b':'1011','c':'1100','d':'1101','e':'1110','f':'1111'}
octa = {k:v[1:] for k,v in hexa.items()}
octa = dict(list(octa.items())[:8])
invOcta = {v:k for k,v in octa.items()}
invHexa = {v:k for k,v in hexa.items()}
def splitConverter(num, sample):
    d = [sample[v] for v in num[0]]
    f = [sample[v] for v in num[1]]
    return [''.join(d),''.join(f)]

def beautiful(num):
    while num[0][0] == '0' and len(num[0]) > 1:
        num[0] = num[0][1:]
    while num[1][-1] == '0' and len(num[1]) > 1:
        num[1] = num[1][:-1]
    return num

def converter(num,c):
    if c in ['h','H']:
        hexad = splitter(num, 3)
        binary = splitConverter(hexad,hexa)
        bonum = binModifier(binary,3)
        octal = splitConverter(bonum, invOcta)
    if c in ['o','O']:
        octal = splitter(num, 4)
        binary = splitConverter(octal,octa)
        bhnum = binModifier(binary,4)
        hexad = splitConverter(bhnum, invHexa)
    if c in ['b','B']:
        binary = splitter(num, 12)
        bonum = binModifier(binary,3)
        octal = splitConverter(bonum, invOcta)
        bhnum = binModifier(binary,4)
        hexad = splitConverter(bhnum, invHexa)
    binary = beautiful(binary)
    octal = beautiful(octal)
    hexad = beautiful(hexad)
    return {'b' : ''.join(binary[0]) + '.' + ''.join(binary[1]),
            'o' : ''.join(octal[0]) + '.' + ''.join(octal[1]),
            'h' : ''.join(hexad[0]) + '.' + ''.join(hexad[1])}
