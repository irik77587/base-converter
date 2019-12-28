import librbc as sh
def dbf(n):
    s = 0
    for v in range(len(n)):
        s = s + (float(n[v])/(2**(v+1)))
    return str(s)[1:]
def frc(n, size = 20):
    fb = []
    while not len(fb) == size or not n == 0.0:
        n = n * 2
        fb.append(str(int(n)))
        n = n - int(n)
        c = ''.join(fb)
    return c
def generate(num):
    number = {k:v for k,v in num.items() if not k in 'd'}
    if not num['d'] == '0.0':
        number['b'] = bin(int(num['d'].split('.')[0])).split('0b')[1] + '.' + frc(float('0.' + num['d'].split('.')[1]))
    base = list(number.keys())
    for i in base:
        if not number[i] == '0.0':
            number = sh.converter(number[i],i)
    if num['d'] == '0.0':
        num['d'] = str(int(number['b'].split('.')[0],2)) + dbf(number['b'].split('.')[1])
    #Beautify decimal START
    while num['d'][-1] == '0' and len(num['d']) > 1:
        num['d'] = num['d'][:-1]
    num['d'] = num['d'] + ('0' if num['d'][-1] in '.' else '.0' if not '.' in num['d'] else '')
    #Beautify decimal END
    number.update({'d' : num['d']})
    return number

