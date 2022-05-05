import math
import json
import random
# https://opentdb.com/api.php?amount=50
import requests
url = "https://opentdb.com/api.php?amount=50"
response = requests.get(url)
quiz_json = response.json()
pretty_object = json.dumps(quiz_json['results'], indent=4)

cnt_correct = 0
cnt_incorrect = 0
game_pass = False

for eachQuiz in quiz_json['results']:
    if cnt_correct > 0:
        game_pass = True
        print("\You Won\n")
        break
    print(eachQuiz["question"])
    correct_ans = eachQuiz["correct_answer"]
    correct_answer_arr = [eachQuiz["correct_answer"]]
    incorrect_answers_arr = eachQuiz["incorrect_answers"]
    answers = correct_answer_arr + incorrect_answers_arr
    
    shuffled_answers = random.sample(answers, len(answers))
    correct_idx = shuffled_answers.index(correct_ans)
    for i in range(len(shuffled_answers)):
        print(i+1, ": ", shuffled_answers[i])
    
    user_answer = int(input('What is answer? : '))
    if (user_answer-1) == correct_idx:
        cnt_correct += 1
        print("\nCorrect\n")

    else:
        cnt_incorrect += 1
        print("\nIncorrect\n")


    