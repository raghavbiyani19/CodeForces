zx = input()
zx = zx.lower()
s = ''
for letter in zx:
    if letter not in 'aeiouy':
        s = s+"."+letter
print(s)