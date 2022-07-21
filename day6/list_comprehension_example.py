import re

# 2 문자열로 나누어 lower_case 리스트로 반환 하는 구문 

str1 = 'The World has changed'
# 가독성이 좋은 않은 형태
strls = [str1[i:i + 2].lower() for i in range(len(str1) - 1) if re.findall('[a-z]{2}', str1[i:i + 2].lower())]

print(strls)

# 가독성을 위해 역할별로 줄을 나눈다
strls_nice_case = [
    str1[i:i + 2].lower() for i in range(len(str1) - 1) 
    if re.findall('[a-z]{2}', str1[i:i + 2].lower())
]
print(strls_nice_case)

# 풀어쓰는 경우
strls_normal_case = []
for i in range(len(str1) - 1):
    if re.findall('[a-z]{2}', str1[i:i + 2].lower()):
        strls_normal_case.append(str1[i:i + 2].lower())

print(strls_normal_case)
