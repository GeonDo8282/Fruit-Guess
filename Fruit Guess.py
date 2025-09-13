import random

print("단어 맞추기 게임에 오신 것을 환영합니다!")
words = ["사과", "바나나", "딸기", "포도", "복숭아"]

# 랜덤 단어 선택
word = random.choice(words)
tries = 0

while True:
    guess = input("어떤 과일일까요? 입력하세요: ")
    tries += 1
    
    if guess == word:
        print(f"정답! {tries}번 만에 맞추셨네요!")
        break
    else:
        print("틀렸어요! 다시 시도해보세요.")
