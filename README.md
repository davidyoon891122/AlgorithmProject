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
  - 리스트 컴프리헨션은 대체로 표현식이 2개를 넘지 않아야 한다
  - 지나치게 복잡한 표현식일 경우에는 풀어 쓰는것이 좋다
  - 역할별로 나누어 2줄로 표현하는 것도 방법이다

# 구글 파이썬 스타일 가이드

- PEF8에서 제공하는 규칙 외에 구글에서 제공하는 가이드라인
- 가독성을 높이기 위한 지침들이 많다
- 함수의 기본 값으로 가변 객체(Mutable Object)를 사용하지 않아야 한다
  - 함수가 객체를 수정하면(리스트에 아이템 추가 등) 기본값이 변경되기 떄문
  - No: def foo(a, b=[]):
  - No: def foo(a, b: Mapping = {}):
  - 다음과 같이 불변 객체(Immutable Object)를 사용, None을 명시적으로 할당하는 것도 좋은 방법
  - Yes: def foo(a, b=None):
    if b is None:
    b = []
  - Yes: def foo(a, b: Optional[Sequence] = None):
    if b is None:
    b = []
- True, False를 판별할 때는 암시적(Implicit)인 방법을 시도하는 편이 간결하고 가독성이 좋다
  - 굳이 False임을 if foo != []: 같은 형태로 판별할 필요가 없다
  - if foo:로 충분하다
- 이외에도 몇 가지 더 정리
  - Yes: if not users:
    print('no users')
  - Yes: if foo == 0:
    self.handle_zero()
  - Yes: if % 10 == 0:
    self.handle_mutilple_of_ten()
  - No: if len(users) == 0:
    print('no users')
  - No: if foo is not None and not foo:
    self.handle_zero()
  - No: if not i % 10:
    self.handle_mutiple_of_ten()

## 빅오, 자료형

- 빅오 big-O는 입력값이 커질 때 알고리즘의 실행 시간(시간 복잡도)과 함께 공간 요구사항(공간 복잡도)이 어떻게 증가하는지를 뷴류하는 데 사용되며, 알고리즘의 효율성을 분석하는 데에도 매우 유용하게 활용된다

# 빅오

- 빅오란 입력값이 무한대로 향할때 함수의 상한을 설명하는 수학적 표기 방법
- 점근적 실행 시간(Asymptotic Running Test)를 표기할 때 가장 널리 쓰이는 수학적 표기법 중 하나이다
- 점진적 실행 시간은 달리 말하면 시간 복잡도라 할 수 있다
- 시간 복잡도(Time Complexity)의 사전적 정의는 어떤 알고리즘을 수행하는 데 걸리는 시간을 설명하는 계산 복잡도(Computational Complexity)를 의미
- 빅오로 시간 복잡도를 표현할 때는 최고차항만을 표기하며, 계수는 무시한다
- 4n^2 + 3n + 4 가 있으면 최고 차항 4n^2의 값만 고려하여 O(n^2)가 된다
- 빅오 크기의 종류
- O(1)
  - 입력값이 아무리 커도 실행 시간은 일정
  - 최고의 알고리즘이라 할 수 있다
  - 해시 테이블의 조회 및 삽입이 이에 해당한다
- O(log n)
  - 실행 시간이 입력값에 영향을 받는다
  - 이진 검색이
- O(n)
  - 입력값만큼 실행 시간에 영향을 받으며, 알고리즘을 수행하는 데 걸리는 시간은 입력값에 비례한다
  - 선형 시간(Linear-Time) 알고리즘이라고 한다
  - 정렬되지 않은 리스트에서 최댓값 또는 최솟값을 찾는 경우
- O(n log n)
  - 병합정렬을 비롯한 효율 좋은 정렬 알고리즘이 이에 해당한다
  - 적어도 모든 수에 대해 한 번 이상은 비교해야 하는 비교 기반 정렬 알고리즘은 아무리 좋은 알고리즘도 O(n log n)보다 빠를 수 없다
  - 물론 입력값이 최선인 경우, 비교를 건너뛰어 O(n)이 될 수 있으며 팀소드(Timsort)가 이런 로직을 갖고 있다
- O(n^2)
  - 버블 정렬 같은 비효율적인 정렬 알고리즘이 이에 해당
- O(2^n)
  - 피보나치 수를 재귀로 계산하는 알고리즘이 이에 해당
  - 간혹 n^2와 혼동하는 경우가 있는데 후반으로 갈 수록 2^n이 훨씬 크다
- O(n!)
  - 각 도시를 방문하고 돌아오는 가장 짧은 경로를 찾는 외판원 문제(Traveling Salesman Problme TSP)를 브루트 포스로 풀이할 떄가 이에 해당
  - 가장 느린 알고리즘
- 공간 복잡도
  - 시간과 공간이 트레이드오프(Space-Time TradeOff) 관계다
  - 빠른 알고리즘은 공간을 많이 사용하고, 공간을 적게 차지하는 알고리즘은 실행 시간이 느리다는 애기다

# 상한과 최악

- 빅오(O)는 상한(Upper Bound)를 의미한다
- 하한(Lower Bound)를 나타내는 빅오메가, 평균을 의미하는 빅세타가 있다
- 상한이 최악과 정확하게 같은 의미는 아니다
- 최악의 경우/평균적인 경우의 시간 복잡도와 아무런 관계가 없는 개념이다(상한)
- 빅오 표기법은 주어진(최선/최악/평균) 경우의 수행 시간의 상항을 나타낸다

# 분할 상황 분석

- 시간 또는 메모리를 분석하는 알고리즘의 복잡도를 계산할 때, 알고리즘 전체를 보지 않고 최악의 경우만을 살펴보는 것은 지나치게 비관적이라는 이유로 분할 상환 분석 방법이 등장하는 계기가 됐다
- 최악의 경우를 여러 번에 걸쳐 골고루 나눠주는 형태로 알고리즘의 시간 복잡도를 계산할 수 있다
- 동적 배열의 경우 아이템 삽입시 더블링이 일어나는 일이 어쩌다 한 번 뿐이지만 이로 인해 시간 복잡도는 O(n)이 된다
- 분할 상환 분석을 사용하면 O(1)이 된다

# 병렬화

- 일부 알고리즘들은 병렬화로 실행 속도를 높일 수 있다
- GPU 처럼 일의 병렬처리에 우수한 장비를 활용하여 병렬 연산으로 전체 실행시간을 줄일 수 있다

# 자료형

- 숫자
- 파이썬은 숫자 정수형으로 int만을 제공한다
- 파이썬 2에서는 int long을 각각 별도로 제공했다
- int는 C 스타일의 고정 정밀도(Fixed-Precision) 정수형이었고, long은 임의 정밀도(Arbitrary-Precision) 정수형이었다
- python 2.4부터 int형으로 충분하지 않으면 자동으로 long타입으로 변경되어 오버플로우가 발생하는 일은 사라졌다
- 파이써에서는 더 이상 고정 정밀도 정수형은 지원하지 않는다
- bool은 엄밀히 따지면 논리 자료형이지만, 파이썬 내부에서는 1(True), 0(False)로 처리되는 int의 서브 클래스이다
- int는 object의 하위 클래스여서 결국 object > int > bool 형태이다

- 매핑
- 매핑(Mapping) 타입은 키와 자료형으로 구성된 복합 자료형이다
- 파이썬에 내장된 유일한 자료형은 바로 딕셔너리이다
- 집합
  - 집합 자료형 set은 중복된 값을 갖지 않는 자료형이다
  - 빈 집합
    - a = set()
  - 값이 포함 된 집합
    - a = {1, 2, 3}
    - dictionary와 비슷하지만 key: value 형태가 아니다
    - set은 입력 순서가 유지되지 않으며, 중복된 값이 있을 경우 하나의 값만 유지한다
- 스퀸스
- 수열(순서 있는 나열) 같은 의미이다
- str은 문자의 순서 있는 나열로 문자열을 이루는 자료형이며, list는 다양한 값들을 배열 형태의 순서 있는 나열로 구성하는 자료형이다
- list라는 시퀸스 타입이 사실상 배열의 역할을 수행한다
- 스퀸스는 불면(Immutable)과 가변(Mutable)으로 구분한다
- 불변은 str, tuple, bytes가 해당된다
- a = 'abc' , a = 'def'
- a는 다른 객체를 참조할 뿐 'abc', 'def'는 변경되지 않았다
- a = 'abc' , a[1] = d # error 발생
- List는 가변이다
- 원시 타입
- C나 자바 같은 프로그래밍 언어들은 기본적으로 원시 타입(Primitive Type)을 제공한다
- 특히 C 언어는 동일한 정수형이라도 크기나 부호에 따라 매우 다양한 원시 타입을 제공한다
- 원시 타입은 메모리에 정확하게 타입 크기만큼의 공간을 할당하고 그 공간을 오로지 값으로 채워넣는다
- 만약 배열이라면 물리 메모리(Physical Memory)에 자료형의 크기만큼 공간을 갖는 요소가 연속된 순서로 배치되는 형태가 된다
- 원시 형타을 제공하면 매우 빠른 연산이 가능하다
- 파이썬은 원시타입을 제공하지 않는다
- 객체
- 파이썬은 모든 것이 객체이다
- 불변객체(Immutable), 가변객체(Mutable)로 구분할 수 있다
- list, set, dict 만 가변 객체이다
- 불변 객체
- a = 10, b = a
- id(a), id(10), id(b) 모두 동일한 주소
- list는 가변 객체이기 때문에 dict의 키로 정하고 set의 값으로 추가할 수 없다
- 가변 객체
- 다른 변수가 참조하고 있을 때 그 변수의 값 또한 변경된다는 의미
- a = [1, 2, 3, 4, 5]
- b = a, a[2] = 4
- a # [1, 2, 4, 4, 5]
- b # [1, 2, 4, 4, 5]
- 파이썬의 참조와 C++ 참조는 다르다
- int a = 10;
  int &b = a;
  b = 7 // a 도 7
- a = 10
  b = a
  b = 7 // a는 10 b는 7
- 파이썬에서 b에 다른 값을 넣는 순간 b는 다른 객체를 참조한다
- 리스트의 경우
- a = [0, 1, 2]
  b = a
  a[0] = 1 # a,b 모두 동일한 id
  b = [1, 1, 2] # a,b가 서로 다른 객체가 된다

# is 와 ==

- is 는 id() 값을 비교한는 함수이다
- None은 널(null)로서 값 자체가 정의되어 있지 않으므로 ==로 비교가 불가능하다
- 따라서 is로만 비교가 가능하다
- if a is None:
  pass
- == 는 비교연산자이다
- a = [1, 2, 3]
- a == a // True
- a == list(a) // True
- a is a // True
- a is list(a) // False
  - 값은 동일하지만 list()로 한 번 더 묶어주면, 별도의 객체로 복사가 되고 다른 ID를 갖게 된다
- a == copy.deepcopy(a) // True
- a is copy.deepcopy(a) // False
  - copy.deepcopy()로 복사한 결과 또는 값은 같지만 ID는 다르기 때문에, ==로 비교하면 True, is로 비교하면 False가 된다
