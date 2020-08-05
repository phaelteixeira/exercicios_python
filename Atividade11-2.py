def invert_dict(d):
    inverse = {}
    for key in d:
        val = d[key]
        inverse.setdefault(val,[]).append(key)
    return inverse

if __name__ == '__main__':
    hist = dict(p=1,a=2,r=2,o=5,t=2)
    inverse = invert_dict(hist)
    for i in inverse:
        keys = inverse[i]
        print(i,keys)
