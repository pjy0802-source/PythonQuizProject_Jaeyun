import json
import os

STATE_FILE = "state.json"  # ← 파일 하나로 통합!

# ===== Quiz 클래스 =====
class Quiz:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

    def to_dict(self):
        """저장용 딕셔너리로 변환"""
        return {
            "question": self.question,
            "options": self.options,
            "answer": self.answer
        }

# ===== QuizGame 클래스 =====
class QuizGame:
    def __init__(self):
        self.quizzes = []
        self.scores = []
        self.load_state()  # 시작할 때 불러오기

    # ===== 저장/불러오기 =====
    def load_state(self):
        """state.json에서 데이터 불러오기"""
        if os.path.exists(STATE_FILE):
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.quizzes = data.get("quizzes", [])
                self.scores = data.get("scores", [])
        else:
            # 파일 없으면 기본 퀴즈 설정
            self.quizzes = [
                {
                    "question": "파이썬에서 리스트에 요소를 추가하는 함수는?",
                    "options": ["1. append()", "2. pop()", "3. remove()", "4. sort()"],
                    "answer": "1"
                },
                {
                    "question": "파이썬의 창시자는?",
                    "options": ["1. 빌 게이츠", "2. 스티브 잡스", "3. 귀도 반 로섬", "4. 일론 머스크"],
                    "answer": "3"
                },
                {
                    "question": "다음 중 파이썬의 특징이 아닌 것은?",
                    "options": ["1. 배우기 쉽다", "2. 오픈 소스이다", "3. 느리지만 강력하다", "4. 컴파일이 필수다"],
                    "answer": "4"
                },
                {
                    "question": "파이썬에서 주석을 작성할 때 사용하는 기호는?",
                    "options": ["1. //", "2. #", "3. /*", "4. --"],
                    "answer": "2"
                },
                {
                    "question": "파이썬에서 딕셔너리를 만들 때 사용하는 괄호는?",
                    "options": ["1. []", "2. ()", "3. {}", "4. <>"],
                    "answer": "3"
                }
            ]
            self.scores = []
            self.save_state()  # 기본 퀴즈 저장

    def save_state(self):
        """state.json에 데이터 저장"""
        data = {
            "quizzes": self.quizzes,
            "scores": self.scores
        }
        with open(STATE_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    # ===== 기능 메서드 =====
    def read_number(self, prompt, minimum, maximum):
        while True:
            value = input(prompt).strip()

            if not value:
                print("숫자를 입력해 주세요.")
                continue

            try:
                number = int(value)
            except ValueError:
                print("정수를 입력해 주세요.")
                continue

            if minimum <= number <= maximum:
                return number

            print(f"{minimum}~{maximum} 사이의 숫자를 입력해 주세요.")
    def play_quiz(self):
        """퀴즈 풀기"""
        score = 0
        print("\n[퀴즈를 시작합니다!]")

        for q in self.quizzes:
            print(f"\n질문: {q['question']}")
            for option in q['options']:
                print(option)

            answer = str(self.read_number("정답 번호를 입력하세요: ", 1, 4))
            if answer == q['answer']:
                print("정답입니다! 🎉")
                score += 1
            else:
                print(f"틀렸습니다. 정답은 {q['answer']}번입니다. 😢")

        print(f"\n퀴즈 종료! 당신의 점수는 {score}/{len(self.quizzes)}입니다.")
        self.scores.append(score)
        self.save_state()
        print("✅ 점수가 저장되었습니다!")

    def add_quiz(self):
        """퀴즈 추가"""
        print("\n[새 퀴즈 추가]")
        question = input("질문을 입력하세요: ")

        options = []
        for i in range(1, 5):
            option = input(f"{i}번 보기를 입력하세요: ")
            options.append(f"{i}. {option}")

        answer = str(self.read_number("정답 번호를 입력하세요: ", 1, 4))

        new_quiz = {
            "question": question,
            "options": options,
            "answer": answer
        }

        self.quizzes.append(new_quiz)
        self.save_state()
        print("✅ 퀴즈가 추가되고 저장되었습니다!")

    def show_quiz_list(self):
        """퀴즈 목록 보기"""
        print(f"\n[퀴즈 목록] 총 {len(self.quizzes)}개")
        for i, q in enumerate(self.quizzes, 1):
            print(f"{i}. {q['question']}")

    def show_scores(self):
        """점수 확인"""
        if not self.scores:
            print("\n아직 퀴즈를 풀지 않았습니다!")
            return

        print(f"\n[점수 기록] 총 {len(self.scores)}회 도전")
        for i, s in enumerate(self.scores, 1):
            print(f"{i}회차: {s}점")
        print(f"🏆 최고 점수: {max(self.scores)}점")

    # ===== 메인 루프 =====
    def run(self):
        """프로그램 실행"""
        while True:
            print("\n=== 파이썬 퀴즈 프로그램 ===")
            print("1. 퀴즈 풀기")
            print("2. 퀴즈 추가")
            print("3. 퀴즈 목록")
            print("4. 점수 확인")
            print("5. 종료하기")

            choice = input("원하는 메뉴 번호를 입력하세요: ")

            if choice == "1":
                self.play_quiz()
            elif choice == "2":
                self.add_quiz()
            elif choice == "3":
                self.show_quiz_list()
            elif choice == "4":
                self.show_scores()
            elif choice == "5":
                print("\n프로그램을 종료합니다. 수고하셨습니다! 👋")
                break
            else:
                print("\n잘못된 입력입니다. 1~5번 사이를 선택해주세요.")

# ===== 실행 =====
if __name__ == "__main__":
    game = QuizGame()
    game.run()