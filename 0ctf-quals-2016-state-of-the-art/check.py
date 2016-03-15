#!/usr/bin/env python

'''
MAPPINGS:

0x72a061f9 ~> 0x1b171f8 ~> void java.lang.String.<init>(byte[])
0x72a0ad91 ~> 0x1b1bd90 ~> void java.lang.StringBuffer.<init>(java.lang.String)
0x72a0e5d9 ~> 0x1b1f5d8 ~> java.lang.StringBuilder java.lang.StringBuilder.reverse()
0x72a0e809 ~> 0x1b1f808 ~> java.lang.String java.lang.StringBuilder.toString()
0x72a061f9 ~> 0x1b171f8 ~> void java.lang.String.<init>(byte[])
0x72a09f11 ~> 0x1b1af10 ~> java.lang.String java.lang.String.replace(char, char)
0x72a0a781 ~> 0x1b1b780 ~> java.lang.String java.lang.String.substring(int, int)
0x72a0d919 ~> 0x1b1e918 ~> java.lang.StringBuilder java.lang.StringBuilder.append(java.lang.String)
0x72a0ac71 ~> 0x1b1bc70 ~> void java.lang.StringBuffer.<init>()
0x72a0ab49 ~> 0x1b1bb48 ~> java.lang.String java.lang.String.trim()
0x72a08971 ~> 0x1b19970 ~> boolean java.lang.String.equals(java.lang.Object)
'''


a1 = [0x78,0x45,0x78,0x32,0x57,0x37] #r10
a2 = [0x22,0x29,0x44,0x55,0x60,0x33] #r7
a3 = [0x17,0x94,0x35,0x03,0x90] #var_48
a4 = [0x45,0x64,0x5f,0x41,0x52,0x54,0x7d] #var_44
a5 = [0x58,0x75,0x1b,0xf0,0x0f,0x4c] #r11
a6 = [0x69,0x0c,0x1b,0xbe,0xf2,0x49] #var_4c

i = 0
while i < len(a2):
    a2[i] = (a2[i] + 0x36) ^ a6[i]
    i += 1

i = 0
while i < len(a1):
    if a1[i] == ord('W'):
        a1[i] = ord('i')
    if a1[i] == ord('2'):
        a1[i] = 0x84
    a1[i] ^= a5[i]
    i += 1

an = a1 + a2 #var_58

a3[4] = a3[4] - ord('1')
a3[3] = a3[3] + 0x2f
a3[2] = a3[2] + ord('*')
a3[1] = a3[1] - 0x22
a3[0] = a3[0] + 0x2e

sb1 = "".join(map(chr,a3))[::-1]

an_replaced = []
for x in an:
    if x == ord("d"):
        an_replaced.append(ord("n"))
    elif x == ord("S"):
        an_replaced.append(ord("e"))
    else:
        an_replaced.append(x)

an_replaced = "".join(map(chr, an_replaced))
an_replaced = an_replaced.strip()

z = an_replaced + sb1

a4_str = "".join(map(chr,a4))
z = z + a4_str[2:7]

print 'FLAG: %s' % z
