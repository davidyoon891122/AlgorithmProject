### Algorithm 공부 이유 및 목표
+ 해외 취업 및 실무 공부를 위해 알고리즘 공부를 시작함
+ 실무 업무 중 특정 정렬 및 문제 해결의 위해 알고리즘 공부의 필요성이 느껴짐
+ 해외 회사들의 경우 대부분 코딩 테스트와 알고리즘 테스트를 기본으로 요구하기 때문에 공부는 필수

## 스터디 도구 및 자료
+ LeetCode(https://leetcode.com)의 Problems를 하루에 1개 이상씩 풀기를 목표로 잡음
+ 프로그래밍 언어는 Python3를 사용하기로 함
+ iOS 개발에도 응용하기 위해 Swift로도 동일한 코드 작성 예정
+ 도서: 파이썬 알고리즘 인터뷰(박상길 지음) 참고하여 공부 예정
## Day1(TwoSum)
+ 조건
    + Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    + You may assume that each input would have exactly one solution, and you may not use the same element twice.
    + You can return the answer in any order.
+ [1,2,3,4] 리스트에 두 수의 합이 target 3 인 리스트를 찾아 내는 코드 작성
+ Solution_1
    + 단순 반복문 방법
        + 반복문 속에 반복문 이중 반복문을 사용하여 두 수의 합이 target과 동일하면 [i, j] 리턴
+ Solution_2
    + dictionary를 활용한 방법 
        + target - List[i]의 값이 딕셔너리에 존재하면 [dictionary[target], index] 를 리턴 하는 방법
        + 배열에 diff값이 존재하지 않으면 dictionary에 값추가
            + dictionary[nums[i]] = index
