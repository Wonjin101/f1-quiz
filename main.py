import json
import os

STATE_FILE = "state.json"


class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

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
        if not isinstance(data, dict):
            raise ValueError("퀴즈 데이터가 딕셔너리 형식이 아닙니다.")
        question = str(data["question"]).strip()
        choices = data["choices"]
        answer = int(data["answer"])
        if not question or not isinstance(choices, list) or len(choices) != 4 or not (1 <= answer <= 4):
            raise ValueError("퀴즈 데이터 필드 형식이 올바르지 않습니다.")
        return cls(question=question, choices=[str(c) for c in choices], answer=answer)


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


class QuizGame:
    def __init__(self, state_file=STATE_FILE):
        self.state_file = state_file
        self.quizzes = []
        self.best_score = None
        self.load_state()

    def load_state(self):
        """state.json 파일에서 퀴즈 목록과 최고 점수를 불러옵니다."""
        if not os.path.exists(self.state_file):
            self.quizzes = get_default_quizzes()
            self.best_score = None
            self.save_state()
            return

        try:
            with open(self.state_file, "r", encoding="utf-8") as f:
                data = json.load(f)

            if not isinstance(data, dict) or "quizzes" not in data:
                raise ValueError("state.json 필수 키(quizzes)가 누락되었습니다.")

            loaded_quizzes = [Quiz.from_dict(q) for q in data["quizzes"]]
            best_score = data.get("best_score", None)
            if best_score is not None and not isinstance(best_score, int):
                best_score = int(best_score)

            self.quizzes = loaded_quizzes if loaded_quizzes else get_default_quizzes()
            self.best_score = best_score
        except (json.JSONDecodeError, KeyError, ValueError, TypeError, OSError) as e:
            print(f"\n⚠️ 데이터 파일({self.state_file})이 손상되었거나 읽을 수 없습니다: {e}")
            print("👉 기본 F1 퀴즈 데이터로 초기화하여 복구합니다.")
            self.quizzes = get_default_quizzes()
            self.best_score = None
            self.save_state()

    def save_state(self):
        """현재 퀴즈 목록과 최고 점수를 state.json 파일에 UTF-8로 저장합니다."""
        data = {
            "quizzes": [q.to_dict() for q in self.quizzes],
            "best_score": self.best_score
        }
        try:
            with open(self.state_file, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except OSError as e:
            print(f"\n⚠️ 데이터 저장 중 오류가 발생했습니다: {e}")

    def get_number_input(self, prompt, min_val, max_val):
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

    def get_text_input(self, prompt):
        while True:
            text = input(prompt).strip()
            if not text:
                print("⚠️ 내용이 비어 있습니다. 다시 입력해 주세요.")
                continue
            return text

    def show_menu(self):
        print("\n" + "=" * 35)
        print("   🏎️  F1(포뮬러 1) 상식 퀴즈 게임  🏁")
        print("=" * 35)
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("=" * 35)

    def play_quiz(self):
        if not self.quizzes:
            print("\n⚠️ 등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가해 주세요.")
            return

        print("\n" + "-" * 35)
        print(f"🏎️ 퀴즈를 시작합니다! (총 {len(self.quizzes)}문제)")
        print("-" * 35)

        correct_count = 0
        for idx, quiz in enumerate(self.quizzes, start=1):
            quiz.display(idx)
            user_answer = self.get_number_input("정답 번호를 입력하세요 (1-4): ", 1, 4)

            if quiz.check_answer(user_answer):
                print("✅ 정답입니다!")
                correct_count += 1
            else:
                correct_choice = quiz.choices[quiz.answer - 1]
                print(f"❌ 오답입니다! (정답: {quiz.answer}번 - {correct_choice})")

        score = int((correct_count / len(self.quizzes)) * 100)
        print("\n" + "=" * 35)
        print("🏁 [퀴즈 결과]")
        print(f"총 {len(self.quizzes)}문제 중 {correct_count}문제 정답! (점수: {score}점)")
        print("=" * 35)

        if self.best_score is None or score > self.best_score:
            self.best_score = score
            print(f"🏆 최고 점수가 {self.best_score}점으로 갱신되었습니다!")
            self.save_state()

    def add_quiz(self):
        print("\n" + "-" * 35)
        print("➕ [새로운 F1 퀴즈 추가]")
        print("-" * 35)

        question = self.get_text_input("문제 내용을 입력하세요: ")
        choices = []
        for i in range(1, 5):
            choice = self.get_text_input(f"선택지 {i}번을 입력하세요: ")
            choices.append(choice)

        answer = self.get_number_input("정답 번호를 입력하세요 (1-4): ", 1, 4)

        new_quiz = Quiz(question, choices, answer)
        self.quizzes.append(new_quiz)
        self.save_state()
        print(f"\n✅ 새로운 퀴즈가 등록 및 저장되었습니다! (현재 총 {len(self.quizzes)}문제)")

    def list_quizzes(self):
        print("\n" + "-" * 35)
        print(f"📋 [저장된 F1 퀴즈 목록] (총 {len(self.quizzes)}문제)")
        print("-" * 35)

        if not self.quizzes:
            print("⚠️ 등록된 퀴즈가 없습니다.")
            return

        for idx, quiz in enumerate(self.quizzes, start=1):
            print(f"{idx}. {quiz.question}")
            for c_idx, choice in enumerate(quiz.choices, start=1):
                print(f"   {c_idx}) {choice}")
            print(f"   👉 정답: {quiz.answer}번 ({quiz.choices[quiz.answer - 1]})\n")

        input("확인하셨으면 엔터(Enter)를 눌러 메뉴로 돌아가세요...")

    def show_best_score(self):
        print("\n" + "-" * 35)
        print("🏆 [최고 점수 확인]")
        print("-" * 35)
        if self.best_score is None:
            print("아직 퀴즈를 풀지 않았습니다. 먼저 퀴즈 풀기에 도전해 보세요!")
        else:
            print(f"현재 최고 점수는 {self.best_score}점입니다! 🎉")
        input("\n확인하셨으면 엔터(Enter)를 눌러 메뉴로 돌아가세요...")

    def run(self):
        try:
            while True:
                self.show_menu()
                choice = self.get_number_input("메뉴 번호를 선택하세요 (1-5): ", 1, 5)
                if choice == 1:
                    self.play_quiz()
                elif choice == 2:
                    self.add_quiz()
                elif choice == 3:
                    self.list_quizzes()
                elif choice == 4:
                    self.show_best_score()
                elif choice == 5:
                    self.save_state()
                    print("\n🏁 데이터를 저장하고 F1 퀴즈 게임을 종료합니다. 감사합니다!")
                    break
        except (KeyboardInterrupt, EOFError):
            print("\n\n⚠️ 프로그램 강제 종료가 감지되었습니다. 현재 상태를 저장하고 안전하게 종료합니다.")
            self.save_state()


def main():
    game = QuizGame()
    game.run()


if __name__ == "__main__":
    main()
