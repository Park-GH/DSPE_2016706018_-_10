import random
import time
#단어 리스트 (추가 가능)
w = ["cat", "dog", "fox", "monkey", "mouse", "panda", "frog", "snake", "wolf"]
#문제 번호
n=1

print("[타자 게임] 준비되면 엔터!")
#엔터 대기
input()
#시작시간
start = time.time()
#단어 랜덤선택
q=random.choice(w)
#5번반복
while n <= 5:
    print("*문제", n)
    #문제보여줌
    print(q)
    #입력받음
    x = input()
    #문제와입력이같을때 통과! 출력
    if q == x:
        print("통과!")
        n = n+1
        q = random.choice(w)
    else:
        print("오타! 다시 도전!")
#끝난시간
end=time.time()
#걸린시간
et = end - start
#소수점둘째자리
et = format(et, ".2f")
#출력
print("타자 시간 :", et, "초")