# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
                       정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제 
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''

from pprint import pprint
import sys


'''
      아래의 구문은 input.txt 를 read only 형식으로 연 후,
      앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
      여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
      아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.

      따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
      아래 구문을 사용하기 위해서는 import sys가 필요합니다.

      단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
sys.stdin = open("lots.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    x=[]
    result = {}
    a = input().split()
   
    for i in a:
        
        
        if i not in result: # 만약 result 안에 a의 i가 없다면 추가?
            result[i] = 1
        else:               # 그외의 상황 *있다면? +1? 그럼 딕셔너리?
            result[i] = result[i] + 1 
        
        # *주절주절 : 일단 딕셔너리를 사용해 값을 구하는건 모두 성공한거 같다, 하지만 max 를 사용하면 그저 키값이 나와 곤란한 상황에 values를 사용해 value의 가장 큰값을 뽑아내는것도 성공했다. 그럼 지금 필요한것? 2시간째
        #계속 계속 고민한거 같은데 무언가 하나가 잡히지 않아 글을 쓰고있다 뭐가 필요할까 라고 글을 쓰고 있는 도중에 생각났다. max values의 값이 밸류인 키를 찾으면 되는게 아닐까? 역시 글로 쓰는게 중요한거 같다.
    # if result[i] == max(result.values()):
    #     print(max(result.values()))
        
    for y in result.values():
        if y == max(result.values()):    
            x.append(y)
    print(x)

       