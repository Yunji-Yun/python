# 함수(Functions)
# 재사용으로 효율 up
# 파라미터(매개변수), 인자(인수)

# 'name' => 파라미터 (함수 정의 부분에서 사용)
def print_name(name): # 함수 정의 함수명(명명규칙 따를 것) (넘겨받을 변수)
    print(f'이름은 {name}입니다')

# "윤윤지" => 인자(인수) (함수 실행시 넘겨받은 값)
print_name("윤윤지")
print_name("윤멋사")

def print_ex_string():
    print("예시 문자열입니다.")

print_ex_string()

def print_name_age(name, age):
    print(f'이름은 {name}이고 {age}살 입니다.')

print_name_age("윤윤지", "21")
# print_name_age() -> 인자가 들어오지 않아 에러

# 함수 기본 값 세팅
# 인자를 넘겨받지 않아도 기본 값 넣어 실행

def order_coffee(qty, option='hot'): # 디폴트 지정한 파라미터가 뒤로 와야 함
    print(f'{qty}잔 / {option}')

order_coffee(3, 'iced')
order_coffee(3)
order_coffee(option='iced', qty=5) # 순서 바뀌어도 ㄱㅊ

def get_id(email):

    if email.endswith('@test.com'):
        email_id = email.removesuffix('@test.com')
        print(email_id)
        return email_id # 다른 변수에 값 넣기 가능
    else:
        print("처리할 수 없는 이메일 주소입니다.")

user_id = get_id('user@test.com')
print(user_id)








