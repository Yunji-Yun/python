def get_id(email):

    if email.endswith('@test.com'):
        email_id = email.removesuffix('@test.com')
        print(email_id)
        return email_id # 다른 변수에 값 넣기 가능
    else:
        print("처리할 수 없는 이메일 주소입니다.")