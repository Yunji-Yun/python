# greeting이라고 하는 변수 선언
# 이 변수에 문자열 값을 할당
greeting = "안녕하세요:)"
print(greeting)

# 변수는 데이터를 변경해서 할당할 수 있는 공간
greeting = "반갑습니다:)"
print(greeting)

# Naming Convention(명명 규칙)

# 1. 변수 사이 공백 허용 안됨
# my greeting = "안녕하세요"

# 2.단어 사이는 _(언더스코어)를 사용하여 연결
my_greeting = "안녕하세요" 

# 3. 변수를 선언하기 위한 문자열은 숫자/특수문자로 시작이 불가
greeting_1 = "안녕"
# 1_greeting = "안녕"
# !_greeting = "안녕"

# 4. 예약어 변수로 선언 불가
# print = "안녕"

# 5. 가급적 소문자 사용

# 6. 오타 주의

# 문자열 (Strings) = 문자의 나열

city = "seoul" # Seoul, SEOUL, SEOul
print(city)

city.upper()
print(city.upper()) # SEOUL

city = city.upper()
print(city) # SEOUL

city.lower()
print(city) # SEOUL
print(city.lower()) # seoul

city = city.lower()
print(city) # seoul

# 통일된 문자 받을 수 잇음

occupation = "developer   " # != "developer"
occupation.rstrip() # 오른쪽 공백 제거
print(occupation.rstrip())

occupation = "   developer" # != "developer"
occupation.lstrip() # 왼쪽 공백 제거

occupation.strip() # 왼쪽, 오른쪽 모두 공백 제거

print("INFP\nENFP\nISTJ\nESTJ") # 개행 문자
print("INFP\tENFP\tISTJ\tESTJ") # 탭 문자

score = "점수:90"
print(score.removeprefix("점수:")) # 불필요한 부분 지움

score_2 = "75점"
print(score_2.removesuffix("점")) # 불필요한 부분 지움

city = "서울 중구"
print(city.replace("서울", "서울시")) # 데이터 일괄 형식으로 받았을 때 데이터 바꿈

si_1 = "용인"
gu_1 = "기흥"
address_1 = f"{si_1}시 {gu_1}구"
print(address_1)

si_2 = "서울"
gu_2 = "종로"

# 서울시 종로구
# 용인시 기흥구
# (시의 이름)시 (구의 이름)구
print(f"{si_1}시 {gu_1}구")
print(f"{si_2}시 {gu_2}구") # 리스트 등에서 데이터를 가져와 쓸 때 유용

# 숫자(Numbers)

a = 2
b = 3

print(a + b) # 더하기
print(a - b) # 빼기
print(a * b) # 곱하기
print(a / b) # 나누기

print(a ** b) # 제곱

print(a + b * b) # 곱하기 먼저 처리

print(a // b) # 몫
print(a % b) # 나머지

# 실수(Float) - 십진 부동 소수점

x = 10.0
y = 0.3
z = 1

print(x + y)
print(x - y)
print(x * y)
print(x / y) # 실수 간 계산은 근사값

print(x + z)
print(x - z)
print(x * z)
print(x / z) # 실수와 연산하는 수는 그 결과가 모두 실수이다.

price = 12_349_000_000_000 # 큰 숫자 식별 편하게
print(price)

# 상수(Contants) - 한 번 선언하면 변경 X

PI = 3.141592 # 덮어쓰기 불가능
PI = 1.23 # 하지만 파이썬은 가능하므로 대문자로 표현하여 상수임을 나타냄
print(PI)

# 문자열-숫자 간 변환

a = 100
b = "100" # 동일하지 않음
c = "0.453"

a = str(a) # 숫자 형태인 a의 값을 문자형으로 변환
b = int(b) # 문자 형태인 b의 값을 정수형으로 변환
c = float(c) # 문자 형태인 c의 값을 실수형으로 변환

# 논리형(Bool, Boolean)
# 대문자로 시작하는 키워드 - True, False (다른 언어와 차이)

print(3 > 2) # False / 크기 비교
print(3 == 3) # True / 같다는 뜻 
print(3 == 3.0) # True / 같은 값인지
print(3 is 3.0) # False / 타입 고려

# 명령 프롬프트(Prompt)

input() # 사용자의 입력 기다림
input("설치를 계속 진행하시겠습니까? (Y/N): ") # 사용자에게 입력 유도
text = input("출력할 텍스트를 입력해주세요: ") # 사용자 입력값 저장
print(text)

# 주석(Comments)
# 한 줄 주석 / 여러 줄 주석
# 부가 설명

"""
여러 줄 주석입니다.
여러 줄 주석입니다.
여러 줄 주석입니다.
print("text")
"""

'''
여러 줄 주석입니다.
여러 줄 주석입니다.
여러 줄 주석입니다.
'''