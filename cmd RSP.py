from random import*
import time

print('가위, 바위, 보에 오신걸 환영합니다./ 끝내고 싶으면 ㅈㅈ 를 치시오.')
print('이기면 3점, 지면 -1점, 비기면 0점, ')
score = 0 ; win = 0 ; draw = 0 ; lose = 0
S = '가위' ; R = '바위' ; P = '보' ; ai = 'PYTHON'
while True:
    if score <= 0:
        score == 0



    print('-'*25)
    rsp = input('PYTHON: 가위 , 바위 , 보  VS  ')
    if rsp == S or rsp == R or rsp == P or rsp == 'ㅈㅈ':
        score += 0 

    else: 
        print('안냈으니 졌다!')
        score -= 1
        lose += 1


    rsp2 = randint(1, 3)
    
    if rsp2 == 1:
        print(ai, ': 가위')
        if rsp == S:
            print('DRAW')
            draw += 1
        if rsp == R:
            print('WIN')
            win += 1
            score += 3
        if rsp == P:
            print('LOSE')
            lose += 1
            score -= 1
    if rsp2 == 2:
        print(ai, ': 바위')
        if rsp == S:
            print('LOSE')
            score -= 1
            lose += 1
        if rsp == R:
            print('DRAW')
            draw += 1
        if rsp == P:
            print('WIN')
            win += 1
            score += 3
    if rsp2 == 3:
        print(ai, ': 보')
        if rsp == S:
            print('WIN')
            win += 1
            score += 3
        if rsp == R:
            print('LOSE')
            score -= 1
            lose += 1
        if rsp == P:
            print('DRAW')
            draw += 1
    print('-'*25)
    if rsp == 'ㅈㅈ':
        print(score,'점')
        print(f'''\n이긴 횟수: {win}회
        \n비긴 횟수: {draw}회
        \n진 횟수: {lose}회
        \n승률: {win/(win+draw+lose)*100, 2}%''')
        save = open("save.txt","w", encoding="UTF-8")
        save.write(win)
        save.close()

        break
time.sleep(5)
time.sleep(5)