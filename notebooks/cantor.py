# cantor.py

# // converted to js/gee from repository below.
# // https://github.com/perrygeo/pairing
# // cantor pairing
# // http://en.wikipedia.org/wiki/Pairing_function

# // cantor paring js
# // limit are values up to ~2^27
# // can't be negative
# // can't be float
import math
import ee
ee.Initialize()

def pair(a, b):
    return 0.5 * (a + b) * (a + b + 1) + b

def depair(z):
    '''Inverse of Cantor pairing function
    http://en.wikipedia.org/wiki/Pairing_function#Inverting_the_Cantor_pairing_function'''
    w = math.floor((math.sqrt(8 * z + 1) - 1) / 2)
    t = (math.pow(w, 2) + w) / 2
    y = z - t
    x = w - y

    return x, y



def eePair(img1, img2):
    pairImg = ee.Image(0).expression(
        "0.5 * (a + b) * (a + b + 1) + b", {
            'a': img1,
            'b': img2
        })
    return pairImg


def eeDepair(img):
    z = ee.Image(img)
    w = (z.multiply(8).add(1)).sqrt().subtract(1).divide(2).floor()
    
    t = w.pow(2).add(w).divide(2)
    y = z.subtract(t)
    x = w.subtract(y)
    return [x, y]


if __name__ == '__main__':
    a = 67108864
    b = 67108865
    pairValue = 0.5 * (a + b) * (a + b + 1) + b
    print(f'input values a:{a} b:{b}')
    print(f'paired value: {pairValue}')
    a, b = depair(0.5 * (a + b) * (a + b + 1) + b)
    print('depaired values a:{a}, b:{b}') 
    
    # //depair a list of values
    a = [1984,2112,3444,3612,4217,4227,5100,5221,5323,6286,6296,6398,6408,7320,7461,7583,11395,11405,12960]
    print(list(map(depair, a)))

    # // cantor paring ee images
    map1 = ee.Image('USGS/NLCD_RELEASES/2019_REL/NLCD/2016')
    map2 = ee.Image('USGS/NLCD_RELEASES/2019_REL/NLCD/2019')

    t1 = eePair(map1, map2)
    t2 = eeDepair(t1)

