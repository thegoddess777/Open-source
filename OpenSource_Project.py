import os

# 연락처 클래스 정의: 연락처 정보를 저장하고 출력하는 기능을 제공
class Contact:
    def __init__(self, name, phone_number, e_mail, addr):
        # Contact 객체 초기화 (이름, 전화번호, 이메일, 주소)
        self.name = name
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.addr = addr

    def print_info(self):
        # 연락처 정보를 출력하는 메서드
        print("======================================")
        print("Name          :", self.name)
        print("Phone Number  :", self.phone_number)
        print("E-mail        :", self.e_mail)
        print("Address       :", self.addr)
        print("======================================")

# 로그인 및 회원가입 처리 함수: 사용자 인증 및 회원가입 기능 제공
def login():
    # 사용자 목록 로드
    users = load_users()
    print("로그인 또는 회원가입")
    print("1. 로그인")
    print("2. 회원가입")
    choice = input("선택: ")

    if choice == "1":
        # 로그인 처리
        username = input("Username: ")
        password = input("Password: ")
        if username in users and users[username] == password:
            print(f"환영합니다, {username}!")
            return username  # 로그인 성공 시 사용자 이름 반환
        else:
            print("잘못된 사용자 이름 또는 비밀번호입니다.")
            return login()  # 재시도
    elif choice == "2":
        # 회원가입 처리
        username = input("새로운 사용자 이름: ")
        if username in users:
            print("이미 존재하는 사용자 이름입니다.")
            return login()
        password = input("새로운 비밀번호: ")
        users[username] = password  # 새로운 사용자 추가
        save_users(users)  # 사용자 정보를 파일에 저장
        print(f"회원가입 완료! {username}님 환영합니다.")
        return username
    else:
        print("잘못된 입력입니다.")
        return login()

def load_users():
    # 사용자 정보를 파일에서 로드
    if not os.path.exists("users.txt"):
        return {}  # 파일이 없을 경우 빈 딕셔너리 반환
    with open("users.txt", "rt") as f:
        lines = f.readlines()
        return {line.split(":")[0]: line.split(":")[1].strip() for line in lines}

def save_users(users):
    # 사용자 정보를 파일에 저장
    with open("users.txt", "wt") as f:
        for username, password in users.items():
            f.write(f"{username}:{password}\n")

def set_contact():
    # 새 연락처를 생성하는 함수
    name = input("Name : ")
    phone_number = input("Phone Number : ")
    e_mail = input("E-mail : ")
    addr = input("Address : ")
    return Contact(name, phone_number, e_mail, addr)  # Contact 객체 반환

def print_contact(contact_list):
    # 모든 연락처를 출력하는 함수
    for contact in contact_list:
        contact.print_info()

def delete_contact(contact_list, name):
    # 이름으로 연락처를 삭제하는 함수
    for i, contact in enumerate(contact_list):
        if contact.name == name:
            del contact_list[i]  # 이름이 일치하는 연락처 삭제
            print(f"{name} 연락처가 삭제되었습니다.")
            return
    print(f"{name} 이름의 연락처를 찾을 수 없습니다.")

def update_contact(contact_list, name):
    # 이름으로 연락처를 수정하는 함수
    for contact in contact_list:
        if contact.name == name:
            print("현재 정보:")
            contact.print_info()
            print("새로운 정보를 입력하세요 (수정하지 않으려면 Enter를 누르세요).")
            new_name = input(f"Name ({contact.name}): ")
            new_phone = input(f"Phone Number ({contact.phone_number}): ")
            new_email = input(f"E-mail ({contact.e_mail}): ")
            new_addr = input(f"Address ({contact.addr}): ")

            # 입력값이 있을 경우만 수정
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

def search_contact(contact_list, name):
    # 이름으로 연락처를 검색하는 함수
    for contact in contact_list:
        if contact.name.lower() == name.lower():
            print("검색 결과:")
            contact.print_info()
            return
    print(f"{name} 이름의 연락처를 찾을 수 없습니다.")

def print_menu():
    # 사용자 메뉴를 출력하고 선택 값을 반환
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

def store_contact(contact_list, username):
    # 사용자별 연락처 정보를 파일에 저장
    with open(f"{username}_contacts.txt", "wt") as f:
        for contact in contact_list:
            f.write("======================================\n")
            f.write(f"Name          : {contact.name}\n")
            f.write(f"Phone Number  : {contact.phone_number}\n")
            f.write(f"E-mail        : {contact.e_mail}\n")
            f.write(f"Address       : {contact.addr}\n")
            f.write("======================================\n")

def load_contact(contact_list, username):
    # 사용자별 연락처 정보를 파일에서 로드
    if not os.path.exists(f"{username}_contacts.txt"):
        return

    with open(f"{username}_contacts.txt", "rt") as f:
        lines = f.readlines()
        if len(lines) % 6 != 0:
            print("파일 형식이 올바르지 않습니다. 연락처를 불러올 수 없습니다.")
            return

        num = len(lines) // 6
        for i in range(num):
            try:
                name = lines[6 * i + 1].split(":", 1)[1].strip()
                phone_number = lines[6 * i + 2].split(":", 1)[1].strip()
                e_mail = lines[6 * i + 3].split(":", 1)[1].strip()
                addr = lines[6 * i + 4].split(":", 1)[1].strip()
                contact = Contact(name, phone_number, e_mail, addr)
                contact_list.append(contact)
            except (IndexError, ValueError):
                print("파일에 잘못된 데이터가 있습니다. 해당 항목을 건너뜁니다.")

# 관리자 메뉴: 모든 사용자 정보와 연락처 출력
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
    # 프로그램 실행 흐름 제어
    username = login()  # 로그인 또는 회원가입
    contact_list = []
    load_contact(contact_list, username)  # 사용자별 연락처 로드

    while True:
        menu = print_menu()

        if menu == 1:
            # 연락처 입력
            contact = set_contact()
            contact_list.append(contact)

        elif menu == 2:
            # 연락처 출력
            print_contact(contact_list)

        elif menu == 3:
            # 연락처 삭제
            name = input("삭제할 이름 입력: ")
            delete_contact(contact_list, name)

        elif menu == 4:
            # 연락처 수정
            name = input("수정할 이름 입력: ")
            update_contact(contact_list, name)

        elif menu == 5:
            # 연락처 검색
            name = input("검색할 이름 입력: ")
            search_contact(contact_list, name)

        elif menu == 6:  # 관리자 메뉴
            admin_menu()

        elif menu == 7:
            # 프로그램 종료
            store_contact(contact_list, username)
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 입력입니다. 다시 선택하세요.")

# 스크립트가 직접 실행될 때만 run 함수 호출
if __name__ == '__main__':
    run()
