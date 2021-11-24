# 문민제 창의적사고와 코딩(SW) 프로젝트
# 프로그램명: 간단한 보드게임 (목표 점수 도달하기)
# IDE: 파이참(PyCharm)

from random import randint

number = 4 # 4명에서 플레이 하는 게임
member = []

for i in range(number):
    name = str(input("사용자의 닉네임을 정하시오: ")) # 이름을 넣은 순서대로 게임을 진행함
    member.append(name)

print("게임에 참여하는 사람", member)

end_point = int(input("게임의 목표 점수를 설정하시오: \n")) # 목표 점수 도달시 게임 종료

dk_map = ["[시작지점]: 죽전치과병원", "사회과학관","제1공학관","제2공학관","제3공학관","종합실험동",
       "노천마당","국제관","석주석기념박물관","곰상","혜당관","법학관","인문관","상경관",
       "사범관","미디어센터","소프트웨어ICT관","범정관"]

print("[맵 배경] <단국대>") # monopoly처럼 하고 싶은 맘에 단국대를 배경으로 함

map_point = []

def random_point():
    for j in range(len(dk_map)): # 맵마다 점수를 -1~3점까지 랜덤하게 배정함
        point = randint(-1,3)
        map_point.append(point)

    print("<각 맵 점수>")

    for a, b in zip(dk_map, map_point):  # zip()함수 이용하여 리스트 2개를 병렬로 묶음
            print(a, "[", b, "]\n")      # 책 <데이터 과학을 위한 파이썬 프로그래밍> 에서 공부한 부분

random_point()

member_point = []

for k in range(number): # 각 플레이어 점수 0점으로 초기화 시키기
    member_point.append(0)

def roll_dice():
    input("주사위를 굴리실거면 아무거나 입력하시오 >>")  # 자동 실행하니 게임의 느낌이 없어서 입력 방법으로 바꿈

# 플레이어의 이동을 체크하기 위한 변수
fir = 0
sec = 0
third = 0
four = 0

n = 1# 턴 수 구하기 위한 변수
print("게임을 시작합니다.") # 여기서부터 게임 시작

while(True):
    print(n,"번째 턴 시작합니다.\n")

    print("[첫번째 플레이어]")
    roll_dice()
    dice = randint(1, 6)
    print("숫자", dice,"나왔습니다.")
    fir += dice
    if fir > 17:
        fir = fir % 18
    member_point[0] += map_point[fir]
    print("[",dk_map[fir],"]에 도착했습니다.",map_point[fir],"만큼의 점수를 획득합니다.\n")

    print("[두번째 플레이어]")
    roll_dice()
    dice = randint(1, 6)
    print("숫자", dice,"나왔습니다.")
    sec += dice
    if sec > 17:
        sec = sec % 18
    member_point[1] += map_point[sec]
    print("[", dk_map[sec], "]에 도착했습니다.", map_point[sec], "만큼의 점수를 획득합니다.\n")

    print("[세번째 플레이어]")
    roll_dice()
    dice = randint(1, 6)
    print("숫자", dice,"나왔습니다.")
    third += dice
    if third > 17:
        third = third % 18
    member_point[2] += map_point[third]
    print("[", dk_map[third], "]에 도착했습니다.", map_point[third], "만큼의 점수를 획득합니다.\n")

    print("[네번째 플레이어]")
    roll_dice()
    dice = randint(1, 6)
    print("숫자", dice,"나왔습니다.")
    four += dice
    if four > 17:
        four = four % 18
    member_point[3] += map_point[four]
    print("[", dk_map[four], "]에 도착했습니다.", map_point[four], "만큼의 점수를 획득합니다.\n")

    print("-현재 게임의 점수:", member_point,"\n")

    n += 1

    if member_point[0] > end_point-1: # 가장 먼저 목표 점수를 달성한 사람이 이김
        print(n,"번째 턴에서 게임 종료@@")
        print(member[0],"님이 이겼습니다!!")
        break

    elif member_point[1] > end_point-1:
        print(n, "번째 턴에서 게임 종료@@")
        print(member[1],"님이 이겼습니다!!")
        break

    elif member_point[2] > end_point-1:
        print(n, "번째 턴에서 게임 종료@@")
        print(member[2],"님이 이겼습니다!!")
        break

    elif member_point[3] > end_point-1:
        print(n, "번째 턴에서 게임 종료@@")
        print(member[3],"님이 이겼습니다!!")
        break

print("< 게 임 종 료 >")