import time
import random

number_of_questions = 10
questions_correct = 0

for question in range(number_of_questions):
    num_1 = random.randint(0, 10)
    num_2 = random.randint(0, 10)
    time.sleep(1)
    print(f"{num_1} x {num_2} = ")

    attempt = 1
    time_before = time.time()
    while True:
        try:
            answer = int(input("Answer: "))
            time_after = time.time()
        except ValueError:
            # This does not count properly the attempts
            print('Please enter whole a number.')
        else:
            if (time_after - time_before) >= 8:
                print("You took too long! Next question:")
                break
            elif attempt >= 3:
                print("Too many tries! Next question:")
                break
            elif answer == (num_1 * num_2):
                questions_correct += 1
                print('Correct!')
                break
            else:
                attempt += 1
                continue

correct_percent = questions_correct / number_of_questions * 100
print(f"You got {round(correct_percent, 2)}% of the questions correct.")
