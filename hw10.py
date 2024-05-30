import os
import pickle

def save_scores(scores, filename='score.bin'):
    with open(filename, 'wb') as file:
        pickle.dump(scores, file)

def load_scores(filename='score.bin'):
    if os.path.exists(filename):
        with open(filename, 'rb') as file:
            scores = pickle.load(file)
        return scores
    return []

def input_scores():
    scores = []
    print("[점수 입력]")
    while True:
        score = int(input(f'#{len(scores) + 1}? '))
        if score < 0:
            break
        scores.append(score)
    return scores

def display_scores(scores):
    if scores:
        print("[점수 출력]")
        print(f'개인점수: {" ".join(map(str, scores))}')
        average = sum(scores) / len(scores)
        print(f'평균: {average:.1f}')
    else:
        print("저장된 점수가 없습니다.")

scores = load_scores()

if scores:
    display_scores(scores)
else:
    scores = input_scores()
    save_scores(scores)
