from Crypto.Util.number import *
p = (1<<448) - (1<<224) - 1
d = [132156247253163728496320586201074, 1469495262398780123809, 167773885276849215533569, 596242599987116128415063, 37414057161322375957408148834323969]

test = 2727436
for test in range(2727436, 1<<25):
    for i in d:
        if pow(test, (p-1)//i, p) == 1:
            print(test, i)
    if test == 1<<40:
        break
# 0 mod 2
