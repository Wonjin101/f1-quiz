def get_number_input(prompt, min_val, max_val):
    while True:
        raw_input = input(prompt).strip()
        if not raw_input:
            print("⚠️ 입력이 비어 있습니다. 숫자를 입력해 주세요.")
            continue
        try:
            number = int(raw_input)
        except ValueError:
            print("⚠️ 잘못된 입력입니다. 숫자만 입력해 주세요.")
            continue
        if number < min_val or number > max_val:
            print(f"⚠️ {min_val}부터 {max_val} 사이의 번호를 선택해 주세요.")
            continue
        return number

def show_menu():
    print("\n" + "=" * 35)
    print("   🏎️  F1(포뮬러 1) 상식 퀴즈 게임  🏁")
    print("=" * 35)
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")
    print("=" * 35)

def main():
    try:
        while True:
            show_menu()
            choice = get_number_input("메뉴 번호를 선택하세요 (1-5): ", 1, 5)
            if choice == 1:
                print("\n👉 [퀴즈 풀기] 화면입니다. (구현 예정)")
            elif choice == 2:
                print("\n👉 [퀴즈 추가] 화면입니다. (구현 예정)")
            elif choice == 3:
                print("\n👉 [퀴즈 목록] 화면입니다. (구현 예정)")
            elif choice == 4:
                print("\n👉 [점수 확인] 화면입니다. (구현 예정)")
            elif choice == 5:
                print("\n🏁 F1 퀴즈 게임을 종료합니다. 감사합니다!")
                break
    except (KeyboardInterrupt, EOFError):
        print("\n\n⚠️ 프로그램 강제 종료가 감지되었습니다. 안전하게 종료합니다.")

if __name__ == "__main__":
    main()
