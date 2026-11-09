import json
import os

# 파일 경로 설정
QUIZ_FILE = "quizzes.json"
SCORE_FILE = "scores.json"

# ===== 파일 불러오기/저장 함수 =====

def load_quizzes():
    """JSON 파일에서 퀴즈 불러오기"""
    if os.path.exists(QUIZ_FILE):
        with open(QUIZ_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    # 파일 없으면 기본 퀴즈 5개 반환
    return [
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

def save_quizzes(quizzes):
    """퀴즈를 JSON 파일에 저장"""
    with open(QUIZ_FILE, "w", encoding="utf-8") as f:
        json.dump(quizzes, f, ensure_ascii=False, indent=2)

def load_scores():
    """JSON 파일에서 점수 기록 불러오기"""
    if os.path.exists(SCORE_FILE):
        with open(SCORE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []  # 파일 없으면 빈 리스트

def save_scores(scores):
    """점수 기록을 JSON 파일에 저장"""
    with open(SCORE_FILE, "w", encoding="utf-8") as f:
        json.dump(scores, f, ensure_ascii=False, indent=2)

# ===== 메뉴 기능 함수 =====

def play_quiz(quizzes, scores):
    """퀴즈 풀기"""
    score = 0
    print("\n[퀴즈를 시작합니다!]")

    for q in quizzes:
        print(f"\n질문: {q['question']}")
        for option in q['options']:
            print(option)

        answer = input("정답 번호를 입력하세요: ")

        if answer == q['answer']:
            print("정답입니다! 🎉")
            score += 1
        else:
            print(f"틀렸습니다. 정답은 {q['answer']}번입니다. 😢")

    print(f"\n퀴즈 종료! 당신의 점수는 {score}/{len(quizzes)}입니다.")

    # 점수 저장
    scores.append(score)
    save_scores(scores)
    print("✅ 점수가 저장되었습니다!")

def add_quiz(quizzes):
    """퀴즈 추가"""
    print("\n[새 퀴즈 추가]")
    question = input("질문을 입력하세요: ")

    options = []
    for i in range(1, 5):
        option = input(f"{i}번 보기를 입력하세요: ")
        options.append(f"{i}. {option}")

    answer = input("정답 번호를 입력하세요 (1~4): ")

    new_quiz = {
        "question": question,
        "options": options,
        "answer": answer
    }

    quizzes.append(new_quiz)
    save_quizzes(quizzes)
    print("✅ 퀴즈가 추가되고 저장되었습니다!")

def show_quiz_list(quizzes):
    """퀴즈 목록 보기"""
    print(f"\n[퀴즈 목록] 총 {len(quizzes)}개")
    for i, q in enumerate(quizzes, 1):
        print(f"{i}. {q['question']}")

def show_scores(scores):
    """점수 확인"""
    if not scores:
        print("\n아직 퀴즈를 풀지 않았습니다!")
        return

    print(f"\n[점수 기록] 총 {len(scores)}회 도전")
    for i, s in enumerate(scores, 1):
        print(f"{i}회차: {s}점")
    print(f"🏆 최고 점수: {max(scores)}점")

# ===== 메인 함수 =====

def main():
    quizzes = load_quizzes()   # 시작할 때 퀴즈 불러오기
    scores = load_scores()     # 시작할 때 점수 불러오기

    # 처음 실행이면 기본 퀴즈 저장
    if not os.path.exists(QUIZ_FILE):
        save_quizzes(quizzes)

    while True:
        print("\n=== 파이썬 퀴즈 프로그램 ===")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료하기")

        choice = input("원하는 메뉴 번호를 입력하세요: ")

        if choice == "1":
            play_quiz(quizzes, scores)
        elif choice == "2":
            add_quiz(quizzes)
        elif choice == "3":
            show_quiz_list(quizzes)
        elif choice == "4":
            show_scores(scores)
        elif choice == "5":
            print("\n프로그램을 종료합니다. 수고하셨습니다! 👋")
            break
        else:
            print("\n잘못된 입력입니다. 1~5번 사이를 선택해주세요.")

if __name__ == "__main__":
    main()