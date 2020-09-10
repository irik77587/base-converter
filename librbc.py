def splitter(num, bytesize):# source bytesize is 3 for hexa, 4 for octal, 12 for binary
    zero = '000000000000'
    array = num.split('.')
    unaligned = len(array[0])%bytesize
    d = zero[:(bytesize-unaligned)] if unaligned else '' + array[0]
    try:
	    unaligned = len(array[1])%bytesize
	    f = array[1] + (zero[:(bytesize-unaligned)] if unaligned else '')
    except IndexError:
	    f = zero[:bytesize]
    return [d,f]

def binModifier(num, bytesize):# destination bytesize is 3 for octal 4 for hexa
    zero = '00000'
    d = [ num[0][(0+x):(bytesize+x)] for x in range(0,int(len(num[0])),bytesize) ]
    f = [ num[1][(0+x):(bytesize+x)] for x in range(0,int(len(num[1])),bytesize) ]
    if d[0] in zero[:bytesize]:
        del d[0]
    if f[-1] in zero[:bytesize]:
        del f[-1]
    return [d,f]

hexa = {'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111','8':'1000','9':'1001','a':'1010','b':'1011','c':'1100','d':'1101','e':'1110','f':'1111'}
octa = {k:v[1:] for k,v in dict(list(hexa.items())[:8]).items()}
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
    return { 'b' : binary[0] + '.' + binary[1], 'o' : octal[0] + '.' + octal[1], 'h' : hexad[0] + '.' + hexad[1] }
