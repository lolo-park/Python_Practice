"""
매개변수 : hp(사냥감의 체력)
출력: 최소한의 병력을 위해 필요한 개미 수
<공격력>
장군개미 5
병정개미 3
일개미 1
예)체력 23의 여치 공격을 위해서는 장군개미 4마리, 병정개미 1마리가 최적
- 그리디 알고리즘 문제같다. 우선순위를 먼저 생각해서 구해야하는 !
- 제일 먼저 장군개미를 통해 구해야한다. hp // 5 뭐 이런식으로..
  for문 두개를 돌리면 될까.. ?
"""
def solution(hp):

