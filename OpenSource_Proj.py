import os

# 연락처 클래스 정의: 연락처 정보를 저장하고 출력하는 기능을 제공
class Contact:
    def __init__(self, name, phone_number, e_mail, addr):
        self.name = name  # 이름
        self.phone_number = phone_number  # 전화번호
        self.e_mail = e_mail  # 이메일 주소
        self.addr = addr  # 주소

    def print_info(self):
        # 저장된 연락처 정보를 출력
        print("Name : ", self.name)
        print("Phone Number : ", self.phone_number)
        print("E-mail : ", self.e_mail)
        print("Address : ", self.addr)

# 로그인 및 회원가입 처리 함수: 사용자 인증 및 회원가입 기능 제공
def login():
    users = load_users()  # 저장된 사용자 정보 로드
    print("로그인 또는 회원가입")
    print("1. 로그인")
    print("2. 회원가입")
    choice = input("선택: ")

    if choice == "1":
        # 로그인 절차
        username = input("Username: ")
        password = input("Password: ")
        if username in users and users[username] == password:
            print(f"환영합니다, {username}!")
            return username  # 로그인 성공 시 사용자 이름 반환
        else:
            print("잘못된 사용자 이름 또는 비밀번호입니다.")
            return login()  # 재시도
    elif choice == "2":
        # 회원가입 절차
        username = input("새로운 사용자 이름: ")
        if username in users:
            print("이미 존재하는 사용자 이름입니다.")
            return login()
        password = input("새로운 비밀번호: ")
        users[username] = password  # 새로운 사용자 추가
        save_users(users)  # 사용자 정보 저장
        print(f"회원가입 완료! {username}님 환영합니다.")
        return username
    else:
        print("잘못된 입력입니다.")
        return login()

# 저장된 사용자 정보를 로드
def load_users():
    if not os.path.exists("users.txt"):
        return {}  # 파일이 없을 경우 빈 딕셔너리 반환
    with open("users.txt", "rt") as f:
        lines = f.readlines()
        return {line.split(":")[0]: line.split(":")[1].strip() for line in lines}

# 사용자 정보를 파일에 저장
def save_users(users):
    with open("users.txt", "wt") as f:
        for username, password in users.items():
            f.write(f"{username}:{password}\n")

# 새로운 연락처 생성 함수
def set_contact():
    name = input("Name : ")
    phone_number = input("Phone Number : ")
    e_mail = input("E-mail : ")
    addr = input("Address : ")
    return Contact(name, phone_number, e_mail, addr)  # Contact 객체 반환

# 연락처 목록 출력
def print_contact(contact_list):
    for contact in contact_list:
        contact.print_info()

# 연락처 삭제 함수
def delete_contact(contact_list, name):
    for i, contact in enumerate(contact_list):
        if contact.name == name:
            del contact_list[i]  # 이름이 일치하는 연락처 삭제
            print(f"{name} 연락처가 삭제되었습니다.")
            return
    print(f"{name} 이름의 연락처를 찾을 수 없습니다.")

# 연락처 수정 함수
def update_contact(contact_list, name):
    for contact in contact_list:
        if contact.name == name:
            print("현재 정보:")
            contact.print_info()
            print("새로운 정보를 입력하세요 (수정하지 않으려면 Enter를 누르세요).")
            new_name = input(f"Name ({contact.name}): ")
            new_phone = input(f"Phone Number ({contact.phone_number}): ")
            new_email = input(f"E-mail ({contact.e_mail}): ")
            new_addr = input(f"Address ({contact.addr}): ")

            # 입력값이 비어있지 않은 경우에만 업데이트
            if new_name.strip():
                contact.name = new_name
            if new_phone.strip():
                contact.phone_number = new_phone
            if new_email.strip():
                contact.e_mail = new_email
            if new_addr.strip():
                contact.addr = new_addr

            print("연락처가 수정되었습니다.")
            return
    print(f"{name} 이름의 연락처를 찾을 수 없습니다.")

# 연락처 검색 함수
def search_contact(contact_list, name):
    for contact in contact_list:
        if contact.name.lower() == name.lower():
            print("검색 결과:")
            contact.print_info()
            return
    print(f"{name} 이름의 연락처를 찾을 수 없습니다.")

# 메뉴 출력 및 입력 처리 함수
def print_menu():
    while True:
        print("1. 연락처 입력")
        print("2. 연락처 출력")
        print("3. 연락처 삭제")
        print("4. 연락처 수정")
        print("5. 연락처 검색")
        print("6. 관리자 메뉴")
        print("7. 종료")
        menu = input("메뉴 선택 : ")
        try:
            return int(menu)  # 정수 변환 시도
        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력해주세요.")

# 연락처 데이터를 파일에 저장
def store_contact(contact_list, username):
    with open(f"{username}_contacts.txt", "wt") as f:
        for contact in contact_list:
            f.write(contact.name + "\n")
            f.write(contact.phone_number + "\n")
            f.write(contact.e_mail + "\n")
            f.write(contact.addr + "\n")

# 파일에서 연락처 데이터를 로드
def load_contact(contact_list, username):
    if not os.path.exists(f"{username}_contacts.txt"):
        return

    with open(f"{username}_contacts.txt", "rt") as f:
        lines = f.readlines()
        num = len(lines) // 4  # 연락처는 4줄로 구성됨
        for i in range(num):
            name = lines[4 * i].rstrip('\n')
            phone_number = lines[4 * i + 1].rstrip('\n')
            e_mail = lines[4 * i + 2].rstrip('\n')
            addr = lines[4 * i + 3].rstrip('\n')
            contact = Contact(name, phone_number, e_mail, addr)
            contact_list.append(contact)

# 관리자 메뉴: 모든 사용자와 연락처 정보를 출력
def admin_menu():
    print("\n==== 관리자 메뉴 ====")
    users = load_users()  # 사용자 정보 로드
    if not users:
        print("저장된 사용자가 없습니다.")
        return

    print("등록된 사용자 목록:")
    for username in users.keys():
        print(f"- {username}")

    print("\n사용자별 연락처 정보:")
    for username in users.keys():
        contact_list = []
        load_contact(contact_list, username)  # 사용자 연락처 로드
        print(f"\n{username}님의 연락처:")
        if not contact_list:
            print("  저장된 연락처가 없습니다.")
        else:
            print_contact(contact_list)

# 메인 프로그램 실행 함수
def run():
    username = login()  # 로그인 또는 회원가입
    contact_list = []
    load_contact(contact_list, username)  # 사용자 연락처 로드

    while True:
        menu = print_menu()

        if menu == 1:
            contact = set_contact()
            contact_list.append(contact)  # 연락처 추가

        elif menu == 2:
            print_contact(contact_list)  # 연락처 출력

        elif menu == 3:
            name = input("삭제할 이름 입력: ")
            delete_contact(contact_list, name)  # 연락처 삭제

        elif menu == 4:
            name = input("수정할 이름 입력: ")
            update_contact(contact_list, name)  # 연락처 수정

        elif menu == 5:
            name = input("검색할 이름 입력: ")
            search_contact(contact_list, name)  # 연락처 검색

        elif menu == 6:  # 관리자 메뉴
            admin_menu()

        elif menu == 7:
            store_contact(contact_list, username)  # 연락처 저장
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 입력입니다. 다시 선택하세요.")

# 스크립트가 직접 실행될 때만 run 함수 호출
if __name__ == '__main__':
    run()
