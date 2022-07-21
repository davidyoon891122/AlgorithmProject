import re

str1 = 'The World has changed'

strls = [str1[i:i + 2].lower() for i in range(len(str1) - 1) if re.findall('[a-z]{2}', str1[i:i + 2].lower())]

print(strls)