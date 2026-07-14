import random


def generate_sequence(n):
    sequence = []
    for _ in range(1, n + 1):
        sequence.append(random.randint(0, 1))
    return sequence


def clustered_sequence_generator(length, p=0.7):
    sequence = []
    sequence.append(random.randint(0, 1))
    for i in range(1, length):
        last = sequence[-1]
        if random.random() < p:
            sequence.append(last)
        else:
            sequence.append(1 - last)
    return sequence
