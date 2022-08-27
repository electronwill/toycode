'''
Suppose a and b are integers, and 0 < a < 2**n, and 0 < b < 2**n, for some known value n.
What's the fastest way to find a and b such that a/b is the closest possible approximation of some irrational number like pi, or e, or the square root of 2?
Here I just brute force it for some low values of n and the irrational number of pi to see if any obvious patterns emerge.
Reddit post: https://www.reddit.com/r/AskProgramming/comments/wswm4g/approximating_an_irrational_with_limited_size_ints/

approximating an irrational as a ratio of limited size integers

Computers typically store non-integer numbers by approximating them in a form similar to a * (2 ** b), or sometimes a * (10 ** b).

I've been curious about how it could work to store them in a form like a/b instead, and playing around with that a bit for fun.

Suppose a and b are integers, and 0 < a < 2 ** n, and 0 < b < 2 ** n, for some known value n.

What's the fastest way to find a and b such that a/b is the closest possible approximation of some irrational number like pi, or e, or the square root of 2?

Is there any feasibly fast way to do this for a large value of n such as 64?

I wrote this tiny Python program to brute force it for n < 24 and the irrational number of pi, just to give some idea of what I'm talking about.
'''

'''
import math

pi = math.pi
besta = 1
bestb = 1
for n in range(1, 24):
    maxa = 2 ** n - 1 # max value of a that is in the required range
    for b in range(1, math.ceil(maxa / pi) + 1):
        a = math.floor(b * pi)
        if a + 1 < 2 ** n and abs(pi - (a + 1) / b) < abs(pi - a / b):
            a = a + 1
        if a < 2 ** n and abs(pi - a / b) < abs(pi - besta / bestb):
            besta = a
            bestb = b
    print(n, '\t', abs(pi - besta / bestb), '\t\t', besta, '/', bestb)
'''

'''
Output (reformatted):

1   2.141592653589793       1 / 1
2   0.14159265358979312     3 / 1
3   0.14159265358979312     3 / 1
4   0.10840734641020688     13 / 4
5   0.0012644892673496777   22 / 7
6   0.0012644892673496777   22 / 7
7   0.0012644892673496777   22 / 7
8   0.0005670125641521473   245 / 78
9   2.667641894049666e-07   355 / 113
10  2.667641894049666e-07   355 / 113
11  2.667641894049666e-07   355 / 113
12  2.667641894049666e-07   355 / 113
13  2.667641894049666e-07   355 / 113
14  2.667641894049666e-07   355 / 113
15  2.667641894049666e-07   355 / 113
16  1.5900235039723043e-07  65298 / 20785
17  3.3162805834763276e-10  104348 / 33215
18  1.2235634727630895e-10  208341 / 66317
19  2.914335439641036e-11   312689 / 99532
20  8.715250743307479e-12   833719 / 265381
21  1.6107115641261771e-12  1146408 / 364913
22  1.1426415369442111e-12  3126535 / 995207
23  2.220446049250313e-14   5419351 / 1725033
'''

'''
Based on Reddit replies:
https://en.wikipedia.org/wiki/Continued_fraction
https://en.wikipedia.org/wiki/Continued_fraction#Continued_fraction_expansion_of_%CF%80_and_its_convergents
https://oeis.org/A001203
This little program uses these first 98 terms to print the first 98 rational approximations of pi, the error of each, and the number of bits in each. Then if necessary, I would generate enough more terms to exceed the 64-bit 2s complement restriction on a and b. Not done in this project: Generalize from pi to all other irrational numbers as long as you have a function that generates successive approximations of the irrational number in the form a * (2 ** b).
'''

import math
x=[3,7,15,1,292,1,1,1,2,1,3,1,14,2,1,1,2,2,2,2,1,84,
 2,1,1,15,3,13,1,4,2,6,6,99,1,2,2,6,3,5,1,1,6,8,1,
 7,1,2,3,7,1,2,1,1,12,1,1,1,3,1,1,8,1,1,2,1,6,1,1,
 5,2,2,3,1,2,4,4,16,1,161,45,1,22,1,2,2,1,4,1,2,24,
 1,2,1,3,1,2,1]
a=[3,22]
b=[1,7]
c=5
for n in range(2,len(x)):
    a=a+[a[-1]*x[n]+a[-2]]
    b=b+[b[-1]*x[n]+b[-2]]
    print(a[-1],b[-1],abs(math.pi - a[-1] / b[-1]))
    while((1<<c) < a[-1]):
        print(c)
        c=c+1

'''
9223372036854775807 is the max 64 bit 2's complement integer
The best approximation in this sequence with numerator and denominator less than that is: 2646693125139304345 / 842468587426513207
1st 100 digits of pi: 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
= 31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679 / 10**100
Using Python's automatic arbitrary precision integer math to estimate errors:
a/b-c/d = (a*d)/(b*d)-(c*b)/(b*d) = (a*d-b*c)/(b*d)
a = 2646693125139304345
b = 842468587426513207
c = 31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
d = 10**100
d = 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
a*d = e = 26466931251393043450000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
e//b = f =                        31415926535897932384626433832795028841830621840162837701327737089604028993736402938143619911858081000
math.floor(math.pi*10**100) = g = 31415926535897931435667303171173228699167550981710022285650709387251316616699277811329625584350265344
c =                               31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
c - g =                                            948959130661621800142804143012041035924098736535826847446162812174950722669070905335
c - f =                                                                 141072153588220508421708833474135069125687048136728341563089679
So, the error of 2646693125139304345 / 842468587426513207 is smaller than the error of Python's math.pi.
(Unsurprising; math.pi and other Python math constants are just a wrapper around the standard floating point approximation used in C, so they're consistent with very old standards.)
'''
