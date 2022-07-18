# 일반적인 형태
print(1,2,3)

# sep example 구분자 넣어서 출력
print('a', 'b', sep=',') # a,b 

# end example 뒤에 추가하여 출력
print('a', 'b', end=' ') # a b
print('c')

# list 출력할때에는 join 사용 Int형은 타입 에러 뜸 string과 합쳐져서
a = ['1', '2', '3']
print(' '.join(a)) # 1, 2, 3

# print formatting
idx = 1
fruit = 'Apple'
print('{0}: {1}'.format(idx + 1, fruit)) # 2: Apple
print('{}: {}'.format(idx + 1, fruit)) # 2: Apple
print(f'{idx +1}: {fruit}') # 2: Apple



