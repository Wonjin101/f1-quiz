class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question  # 문제 문자열
        self.choices = choices    # 4개의 선택지 리스트
        self.answer = answer      # 정답 번호 (1~4)

    def display(self, index=None):
        if index is not None:
            print(f"\n[문제 {index}] {self.question}")
        else:
            print(f"\nQ. {self.question}")
        for idx, choice in enumerate(self.choices, start=1):
            print(f"  {idx}) {choice}")

    def check_answer(self, user_answer):
        return self.answer == user_answer

    def to_dict(self):
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            question=data["question"],
            choices=data["choices"],
            answer=data["answer"]
        )


def get_default_quizzes():
    return [
        Quiz(
            "F1에서 앞차와의 간격이 1초 이내일 때 리어 윙을 열어 공기 저항을 줄이는 시스템은?",
            ["ERS", "DRS", "ABS", "KERS"],
            2
        ),
        Quiz(
            "이탈리아를 대표하는 F1 팀 스쿠데리아 페라리(Scuderia Ferrari)의 상징 색상은?",
            ["브리티시 레이싱 그린", "실버 애로우", "로쏘 코르사(레드)", "파파야 오렌지"],
            3
        ),
        Quiz(
            "F1 본선 레이스(그랑프리)에서 1위로 우승한 드라이버가 획득하는 기본 포인트는?",
            ["10점", "15점", "20점", "25점"],
            4
        ),
        Quiz(
            "도심의 일반 도로를 통제하여 달리며, 코스가 좁고 추월이 극도로 어렵기로 유명한 전통의 F1 서킷은?",
            ["모나코 서킷", "실버스톤 서킷", "몬자 서킷", "스파프랑코르샹 서킷"],
            1
        ),
        Quiz(
            "마른 노면에서 사용하는 F1 슬릭 타이어(Slick Tire) 3종 중 가장 부드럽고 접지력이 높은 타이어와 줄무늬 색상은?",
            ["하드(Hard) - 흰색", "미디엄(Medium) - 노란색", "소프트(Soft) - 빨간색", "인터미디엇(Intermediate) - 초록색"],
            3
        )
    ]


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
