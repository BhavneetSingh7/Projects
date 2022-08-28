import random
from string import digits

n = 1000
lst = []
country_codes = ['+91','+61']

for i in range(n):
    c = random.randrange(0,len(country_codes))
    num = country_codes[c]+ ' ' + str(random.randrange(7000000000,9999999999)) + '\n'
    lst.append(num)

with open('random_numbers.txt','w',encoding='utf-8') as f:
    for n in lst:
        f.write(n)