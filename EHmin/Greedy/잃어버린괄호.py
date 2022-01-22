import sys

sentence = sys.stdin.readline().strip().split('-') # -를 기준으로 문자열을 분할한다.
#ex)10-5+5+3+5-6+5-4-5 > 10, 5+5+3+5, 6+5, 4, 5
temp = []

for sub in sentence:
    temp.append(sum(list(map(int, sub.split('+'))))) 
    # -를 기준으로 분할한 식에는 숫자와 +만 남는다 >>> +를 기준으로 문자열을 재분할 >>> map을 이용하여 정수로 바꾸어서 새로운 list에 저장, sum을 사용해서 동시에 각 계산식의 합을 도출
    # [10, 5+5+3+5, 6+5, 4, 5] > [10, 18, 11, 4, 5]
sys.stdout.write(str((sum(temp)*-1) + 2*temp[0]))
# 첫번째 식 말고는 모두 -로 연결 된 것이므로, 첫번째 것에서 나머지 인덱스에 있는값을 모두 빼주면 된다.
# sum을 사용하고 -1 곱하고, 0번째를 2번 더했음.(sum()함수를 사용하기 위해서 이다.
