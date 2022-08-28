import random
from string import digits,ascii_letters

email_providers = ['gmail','yahoo','orkut']
available_char = digits + ascii_letters

n = 1000
file = 'random_emails.txt'

lst = []
for i in range(n):
    l = random.randint(4,20)
    e = ''
    for j in range(l):
        c = random.randrange(0,62)
        e = e + available_char[c]
    ep = random.randrange(0,3)
    e = e + '@' + email_providers[ep] + '.com'
    lst.append(e)
    
with open(file,'w') as f:
    for e in lst:
        f.write(e+'\n')