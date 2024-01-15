def cheak_password(password:str):
    if not password:
        print('password is empty')
        return
    
    with open('password.txt', 'r') as file:
        common_passwords: list[str] = file.read().splitlines()
        
    for i, common_passwords in enumerate(common_passwords,start=1):
        if password == common_passwords:
            print(f'{password} : ❌ Common and among -->> (#{i})')
            return
    print(f'{password} : ✔️ unique password!!!') 

def main():
    while True:
        user_password = input('Enter your password>>>')
        if user_password == 'exit':
            break

        if not user_password:
            print('password is empty')
        else:
            cheak_password(user_password)
    
if __name__ == '__main__':
    main()