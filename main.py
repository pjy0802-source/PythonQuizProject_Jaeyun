quizzes = [
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
    }
]

def main():
    while True:  # 프로그램이 계속 실행되도록 반복문 추가
        print("\n=== 파이썬 퀴즈 프로그램 ===")
        print("1. 퀴즈 풀기")
        print("2. 점수 확인")
        print("3. 종료하기")
        
        choice = input("원하는 메뉴 번호를 입력하세요: ")
        
        if choice == "1":
            score = 0  # 맞힌 개수를 저장할 변수
            print("\n[퀴즈를 시작합니다!]")
            
            for q in quizzes:  # 리스트에 있는 문제를 하나씩 꺼내옴
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
            
        elif choice == "2":
            print("\n[점수 확인 기능은 아직 개발 중입니다!]")
            
        elif choice == "3":
            print("\n프로그램을 종료합니다. 수고하셨습니다!")
            break  # while 반복문을 빠져나가서 프로그램을 종료함
            
        else:
            print("\n잘못된 입력입니다. 1~3번 사이를 선택해주세요.")

if __name__ == "__main__":
    main()