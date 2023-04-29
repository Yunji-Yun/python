# 조건문

if True: # 조건식이 참일때 종속된 식이 실행
    print("True") # 들여쓰기 해야 이프문에 종속
else:
    print("False")

if 4 > 3 :
    print("a")
else:
    print("b")

# 입력 값을 string 타입으로 처리
value = input("값을 입력해주세요: ") # input은 받은 값이 모두 str 임 -> 실수 혹은 정수 형태로 바꿔야 숫자 비교에 사용 가능

if int(value) > 10:
    print("a")
else:
    print("b")

# 특정 값에 대한 조건을 만들 때 예외를 없애기 위해 로퍼 함수 이용!
value = value.upper()
if value == "ENFJ":
    print("ENFJ")
else:
    print("nothing")

# 다중조건
day = input("요일을 입력해주세요(0~6): ")

if day == '0':
    print("휴무")
elif day == '6':
    print("단축영업")
elif day == '1':
    print("연장영업")
else :
    print("정상영업")


# 반복문(loops)

i = 0 # 변수 초기화 (사용할 변수는 초기화하는 것이 좋음)
text = ""
sum = 0

for i in range(1, 101): # (시작값, 끝값+1)
    print(i)

for i in range(1, 101):
    sum = sum + i

print(sum)

'''
while True:
    print("while loop") # 무한 반복 -> 종료 조건, 범위 설정 중요
'''
progress = 0

while progress < 100:
    progress = progress + 1
    print(f"{progress}% completed")

