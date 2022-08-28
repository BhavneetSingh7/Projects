import re

pattern = re.compile(r'\w+\@gmail\.com')

with open('random_emails.txt','r',encoding='utf-8') as f:
    contents = f.read()
    matches = pattern.finditer(contents)
    count = 0
    for match in matches:
        count += 1
        # print(match)
    print(count)
