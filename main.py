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


def get_text_input(prompt):
    while True:
        text = input(prompt).strip()
        if not text:
            print("⚠️ 내용이 비어 있습니다. 다시 입력해 주세요.")
            continue
        return text


def play_quiz(quizzes):
    if not quizzes:
        print("\n⚠️ 등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가해 주세요.")
        return 0

    print("\n" + "-" * 35)
    print(f"🏎️ 퀴즈를 시작합니다! (총 {len(quizzes)}문제)")
    print("-" * 35)

    correct_count = 0
    for idx, quiz in enumerate(quizzes, start=1):
        quiz.display(idx)
        user_answer = get_number_input("정답 번호를 입력하세요 (1-4): ", 1, 4)

        if quiz.check_answer(user_answer):
            print("✅ 정답입니다!")
            correct_count += 1
        else:
            correct_choice = quiz.choices[quiz.answer - 1]
            print(f"❌ 오답입니다! (정답: {quiz.answer}번 - {correct_choice})")

    score = int((correct_count / len(quizzes)) * 100)
    print("\n" + "=" * 35)
    print("🏁 [퀴즈 결과]")
    print(f"총 {len(quizzes)}문제 중 {correct_count}문제 정답! (점수: {score}점)")
    print("=" * 35)
    return score


def add_quiz(quizzes):
    print("\n" + "-" * 35)
    print("➕ [새로운 F1 퀴즈 추가]")
    print("-" * 35)

    question = get_text_input("문제 내용을 입력하세요: ")
    choices = []
    for i in range(1, 5):
        choice = get_text_input(f"선택지 {i}번을 입력하세요: ")
        choices.append(choice)

    answer = get_number_input("정답 번호를 입력하세요 (1-4): ", 1, 4)

    new_quiz = Quiz(question, choices, answer)
    quizzes.append(new_quiz)
    print(f"\n✅ 새로운 퀴즈가 등록되었습니다! (현재 총 {len(quizzes)}문제)")


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
    quizzes = get_default_quizzes()
    try:
        while True:
            show_menu()
            choice = get_number_input("메뉴 번호를 선택하세요 (1-5): ", 1, 5)
            if choice == 1:
                play_quiz(quizzes)
            elif choice == 2:
                add_quiz(quizzes)
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
