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
