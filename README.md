### Algorithm 공부 이유 및 목표

- 해외 취업 및 실무 공부를 위해 알고리즘 공부를 시작함
- 실무 업무 중 특정 정렬 및 문제 해결의 위해 알고리즘 공부의 필요성이 느껴짐
- 해외 회사들의 경우 대부분 코딩 테스트와 알고리즘 테스트를 기본으로 요구하기 때문에 공부는 필수

## 스터디 도구 및 자료

- LeetCode(https://leetcode.com)의 Problems를 하루에 1개 이상씩 풀기를 목표로 잡음
- 프로그래밍 언어는 Python3를 사용하기로 함
- iOS 개발에도 응용하기 위해 Swift로도 동일한 코드 작성 예정
- 도서: 파이썬 알고리즘 인터뷰(박상길 지음) 참고하여 공부 예정

## Day1(TwoSum)

- 조건
  - Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
  - You may assume that each input would have exactly one solution, and you may not use the same element twice.
  - You can return the answer in any order.
- [1,2,3,4] 리스트에 두 수의 합이 target 3 인 리스트를 찾아 내는 코드 작성
- Solution_1
  - 단순 반복문 방법
    - 반복문 속에 반복문 이중 반복문을 사용하여 두 수의 합이 target과 동일하면 [i, j] 리턴
- Solution_2
  - dictionary를 활용한 방법
    - target - List[i]의 값이 딕셔너리에 존재하면 [dictionary[target], index] 를 리턴 하는 방법
    - 배열에 diff값이 존재하지 않으면 dictionary에 값추가
      - dictionary[nums[i]] = index

## Day2 (언어 Python)

# Why Python!

- 면접관이 쉽게 이해할 수 있다
  - 문법이 간단하고 수도코드 포멧으로 작성하기도 편하다
- 코딩 플래폼에서의 지원
  - 거의 모든 플랫폼에서 파이썬을 지원하지만, 간혹 과도한 내장 라이브러리 사용을 제한하기 위해 파이썬을 금하는 기업도 있다
- 유연한 언어
  - 파이썬은 정적인 언어인 자바나 C와는 달리 엄격함이 거의 없다
  - 타입힌트는 선택사항이고 유연하게 알고리즘 구현에만 집중할 수 있다
  - 과도한 유연함은 패널티가 될 수 있다, 쓰지않는 변수, 잘못된 변수는 제거하도록 하자
- 언어 레벨에서의 풍부한 기능 지원
  - 코딩 테스트에서는 외부 라이브러리 사용이 제한된다
  - 파이썬의 경우 언어 레벨에서 풍부한 기능을 제공하기 때문에 사용하면 할줄 알면 된다

# Python History

- 1989년 12월 30대 중반 네덜란드 컴퓨터 과하자 귀도 반 로썸(Guido Van Rossum)에 의해 탄생
- 파이썬의 원칙
  - 읽기 쉬워야 한다(인덴트 처리)
  - 사용자가 원하는 모듈 패키지를 만들 수 있어야 한다(easy_install을 걸쳐 pip를 통해 패키지 인덱스 제공)
  - 약간 독특하고 신비한 이름(코미디 그룹 몬티 파이썬(Monty Python)의 이름을 땀)

# 파이썬 인덴트

- PEP 8 공식 가이드에 따라 공백 4칸을 원칙으로 한다
  - PEP: 파이썬의 개발은 파이썬 개발 제안서(Python Enhanchment Proposals) 프로세스를 통해 진행된다.
- PyCharm 커뮤니티 에디션을 활용하면 여러 pyLint을 자동으로 적용해준다

# 네이밍 컨벤션

- 파이썬 변수명 네이밍 컨벤션(Naming Convention)은 밑줄(\_)로 구분하여 스네이크 케이스(Snake Case)를 따른다
- 파이썬은 파이썬다운 방식(Python Way)에 굉장한 자부심이 있다

# 타입 힌트

- PEP 484에 타입 힌트(Type Hint)가 추가됐다
- 이 기능은 파이썬 3.5부터 사용 가능하다
- CPython typing.py에는 선언할 수 있는 타입이 명시 되어 있다
  - a: str = "a"
  - b: int = 1
- 소프트웨어의 규모가 커지고, 협업이 많아지면서 타입 명시의 중요성이 커지고, 코드 가독성이 좋은 코드의 기본이 되기 시작하였다
- 타입 힌트 확인 라이브러리 mypy
  - pip install mypy
- Python Module 실행
  - python3 -m mypy python_file_name.py

# 리스트 컴프리헨션

- 기존 리스트를 기반으로 새로운 리스트를 만들어내는 구문
- 파이썬 2.0부터 지원했음
- 홀수인 경우 2를 곱해 출력하는 리스트 컴프리헨션
  - [n * 2 for n in range(1, 10 + 1) if n % 2 == 1]
  - 리스트 컴프리헨션을 사용하지 않을 경우
    - a = []
      for n in range(1, 10 + 1):
      if n % 2 == 1:
      a.append(n \* 2)
  - 코드 길이도 줄어들고 변수의 양도 줄어들게 된다
- 딕션너리의 경우도 컴프리헨션이 가능하다
  - a = {key, value for key, value in original.items()}
  - a = {}
    for key, value in original.items():
    a[key] = value

# 제너레이터

- 루프의 반복 동작을 제어할 수 있는 루틴 형태를 말한다
- 임의의 숫자 1억개를 생성할 경우 제너레이터가 없으면 1억 개를 메모리 어딘가에 보관해야만 한다
- 제너레이터를 사용하면 단순히 제너레이터만 생성하고 필요할 때 언제든 숫자를 만들 수 있다
- yield 구문을 사용하면 제너레이터를 리턴할 수 있다
- yield는 제너레이터가 여기까지 실행 중이던 값을 내보낸다는 의미이며, 함수는 종료되지 않고 계속해서 맨 끝에 도달할 떄까지 실행된다
- def get_natural_number():
  n = 0
  while True:
  n += 1
  yield n
- g = get_natural_number()
- next(g) // 1, 2, 3 next로 g를 호출할 때마다 1씩 증가된 값을 리턴한다

# Range

- 제너레이터의 방식을 활용하는 대표적임 함수는 range이다
- list(range(5)) // [0, 1, 2, 3, 4]
- range(5) // range(0, 5)
- for i in range(5):
  print(i) // 0, 1, 2, 3, 4 출력
- python3 부터 range() 함수가 리턴하는 값이 제너레이터 역할을 하는 것으로 바뀜
- 숫자 100만개를 생성하는 방법
  - 방법 1
    - a = [n for n in range(1000000)]
    - 이미 생성된 값이 담겨 있다
    - getsizeof(a) // 8448728
  - 방법 2
    - b = range(100000)
    - range 함수로 조건만 담겨 있다
    - getsizeof(b) // 48
    - b[500] // 500 인덱스로 접근도 가능하다

# Enumerate

- 열거하다 라는 뜻의 함수
- 여러가지 자료형(List, Set, Tuple 등)을 인덱스를 포함한 enumerate 객체로 리턴한다.
- a = [1, 2, 3]
  enumerate(a) // 0, 1 1, 2 2, 3 형태로 열거형 반환, 반환한 값을 list(enum) 리스트화 하여 사용
- 출력
  for i, v in enumerate(a):
  print(i, v)

# 나눗셈 연산자 //

- 파이썬 2이하에서는 / 연산자는 타입을 유지하려는 특성 때문에 실수하기가 쉬웠다
- 5 / 3 의 경우 파이썬 3 이상에서는 1.666..이지만 파이썬 2이하 버전에서는 정수형을 유지해 1을 리턴했다
- 파이썬 3에서는 // 연산자가 타입을 유지하는 형태의 나눗셈 연산자로 추가 되었다(몫을 구하는 연산자)

# print

- 파이썬 2에서는 Statement 였으나, 3에서는 print() 함수로 바뀌었다
- print('a', 'b') // a b
- print('a', 'b', sep=',') // a, b
- print()는 항상 줄바꿈을 포함한다 end 파라미터로 줄바꿈을 제거할 수 있다.
- print('a', end=' ')
  print('b') // a b
- 리스트를 출력할떄는 join을 사용한다
- a = ['a', 'b']
  print(' '.join(a)) // a b
- formatting
- idx = 1
  fruit = 'Apple'
  print('{0}: {1}'.format(idx + 1, fruit)) // 2: Apple
- 인덱스는 생략 가능하다
- print('{}: {}'.format(idx + 1, fruit)) // 2: Apple
- f-string(formated string literal)
  print(f'{idx + 1}: {fruit}) // 2: Apple
  - 파이썬 3.6+ 에서만 지원한다

# pass

- 임시 함수, 임시 클래스(즉 미완성) 등을 작성하고 에러를 예외 처리하기 위해서 내용에 pass를 사용하여 처리
- class MyClass(object):
  def method_a(self):

  def method_b(self):
  print('Method B')
  c = MyClass() // IndentationError

- def method_a(self) 함수에 pass를 삽입하여 에러를 방지할 수 있다.
- def method_a(self):
  pass
- 파이썬에서 pass는 널 연산(Null Operation)으로 아무것도 하지 않는 기능
- pass는 목업(mockup) 인터페이스부터 구현한 다음에 추후 구현을 진행할 수 있게 한다.

# locals

- 로컬 심볼 테이블 딕셔너리를 가져오는 메소드
- 선언된 모든 변수를 조회할 수 있는 명령
- import pprint // pprint는 가독성을 위한 줄바꿈 처리를 위해 추가
  pprint.pprint(locals())

# 리스트 컴프리헨션

- 지나치게 남발하면 가독성을 떨어뜨리게 된다
  - 예제 day6
