# a.Create a docstring constant with 3 sentence strings
docstring = ('''The rain in #Spain in 2019, rained "mainly' on the plain.
                I bought an hamburger from 'KFC'.
                My friend named Jerry who was a boy.''')
# b.Convert the docstring to a LIST with one element
s = [x for x in docstring.split('.')]
s.pop()
print(s)
import string

# c.Using a loop calculate the number
a = 0
b = 0
c = 0
d = 0
digits = string.digits
puncs = string.punctuation
count = 0
for i in s:
    for j in i:
        if j.isupper():
            a += 1
            count+=1
        if j.islower():
            b += 1
            count += 1
        if j in digits:
            c += 1
            count += 1
        if j in puncs:
            d += 1
            count += 1
# d. Output the results
print('# #Upper #Lower #Digits #Punct.')
print('------------------------------')
print("asd{:^5}da{}s".format(1,"asd"))
for i in range(count):
    print('{:^} {:^} {:^} {:^}'.format(count + 1, a, b, c, d))
    count += 1