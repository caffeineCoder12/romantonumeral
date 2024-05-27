d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

s = input()

num = 0
num += d[s[0].upper()]
for i in range(1,len(s)):
    if num < d[s[i].upper()]:
        num -= d[s[i].upper()]
    else:
        num += d[s[i].upper()]

print(abs(num))