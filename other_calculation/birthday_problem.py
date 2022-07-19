import random

TRIALS = 100000    # Number of trials
same_birthday = 0  # Number of trials with same birthday

# 100,000 trials
for _ in range(TRIALS):
    birthdays = []

    # If 23 people have the same birthday, increase same_birthday by 1.
    for _ in range(23):
        birthday = random.randint(1, 365)
        if birthday in birthdays:
            same_birthday += 1
            print(same_birthday)
            break
        birthdays.append(birthday)

    # Probability of experiments with the same birthday among all 100,000 trial
    print(f'{same_birthday / TRIALS * 100}%')
