# 일반적인 열거형 예제
a = [1, 2, 3, 2, 45, 2, 5]

print(list(enumerate(a)))

# 열거형을 쓰기전 index와 함께 리스트 출력 방법 1
b = ['a1', 'a2', 'a3']

for i in range(len(b)):
    print(i, b[i])

# 열거형을 쓰기전 index와 함께 리스트 출력 방법 2
i = 0

for v in b:
    print(i, v)
    i += 1

# 열거형을 써서 리스트 출력
for i, v in enumerate(b):
    print(i, v)
