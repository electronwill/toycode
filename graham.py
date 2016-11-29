'''
github.com/electronwill 2016-11-29
https://en.wikipedia.org/wiki/Graham%27s_number
These functions are only designed and tested to work for integers a >= 0 and b >= 0 .
They are only feasible to execute for a few very small integer values.
'''

def successor(a):
    return a + 1

def sum(a, b):
    c = a
    for _ in range(b):
        c = successor(c)
    return c

def sum_fast(a,b): return a+b

def product(a, b): #a*b
    c = 0
    for _ in range(b):
        c = sum_fast(a, c)
    return c

def product_fast(a,b): return a*b

def exponent(a, b): #a^b
    c = 1
    for _ in range(b):
        c = product_fast(a, c)
    return c

def exponent_fast(a,b): return a**b

def tetration(a, b): #a^^b
    c = 1
    for _ in range(b):
        c = exponent_fast(a, c)
    return c

def pentation(a, b): #a^^^b
    c = 1
    for _ in range(b):
        c = tetration(a, c)
    return c

def hyperoperation(a, b, n):
    if n==0: return b+1
    if n>2:
        result=1
    else:
        result=[0,a,0][n]
    for _ in range(b):
        result = hyperoperation(a,result,n-1)
    return result

def hyperoperation_fast(a,b,n):
    if n==0: return b+1
    if n==1: return a+b
    if n==2: return a*b
    if n==3: return a**b
    result=1
    for _ in range(b):
        result = hyperoperation_fast(a,result,n-1)
    return result

def h(a,b,n): return hyperoperation_fast(a,b,n)

def g(): #Graham's number; it is not feasible to execute this code
    g = h(3,3,6)
    for _ in range(63):
        g = h(3,3,g)
    return g

def test(f):
    for a in range(4):
        for b in range(4):
            print(f(a,b),' ',end='')
        print()
    print()

def testing():
    print('successor sum product exponent tetration pentation')
    for a in range(4): print(successor(a),' ',end='')
    print()
    print()

    test(sum)
    test(product)
    test(exponent)
    test(tetration)

    for a in range(3):
        for b in range(4):
            print(pentation(a,b),' ',end='')
        print()
    for b in range(3):
        print(pentation(3,b),' ',end='')
    print()
    print()

    print('hyperoperation')
    for n in range(4):
        for a in range(4):
            for b in range(4):
                print(hyperoperation(a,b,n),' ',end='')
            print()
        print()
    
    print('hyperoperation_fast')
    for n in range(5):
        for a in range(4):
            for b in range(4):
                print(h(a,b,n),' ',end='')
            print()
        print()
    for a in range(3):
        for b in range(4):
            print(h(a,b,5),' ',end='')
        print()
    for b in range(3):
        print(h(3,b,5),' ',end='')
    print()

testing()

'''
successor sum product exponent tetration pentation
1  2  3  4

0  1  2  3
1  2  3  4
2  3  4  5
3  4  5  6

0  0  0  0
0  1  2  3
0  2  4  6
0  3  6  9

1  0  0  0
1  1  1  1
1  2  4  8
1  3  9  27

1  0  1  0
1  1  1  1
1  2  4  16
1  3  27  7625597484987

1  0  1  0
1  1  1  1
1  2  4  65536
1  3  7625597484987

hyperoperation
1  2  3  4
1  2  3  4
1  2  3  4
1  2  3  4

0  1  2  3
1  2  3  4
2  3  4  5
3  4  5  6

0  0  0  0
0  1  2  3
0  2  4  6
0  3  6  9

1  0  0  0
1  1  1  1
1  2  4  8
1  3  9  27

hyperoperation_fast
1  2  3  4
1  2  3  4
1  2  3  4
1  2  3  4

0  1  2  3
1  2  3  4
2  3  4  5
3  4  5  6

0  0  0  0
0  1  2  3
0  2  4  6
0  3  6  9

1  0  0  0
1  1  1  1
1  2  4  8
1  3  9  27

1  0  1  0
1  1  1  1
1  2  4  16
1  3  27  7625597484987

1  0  1  0
1  1  1  1
1  2  4  65536
1  3  7625597484987
'''
