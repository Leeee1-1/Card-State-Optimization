def local_fix(sequence):
    operation_times = 0
    for idx, state in enumerate(sequence):
        if state == 0:
            sequence[idx] = 1
            operation_times += 1
    return sequence, operation_times


def Suffix_flip(sequence):
    operation_times = 0
    for idx, state in enumerate(sequence):
        if state == 0:
            for state_idx in range(idx, len(sequence)):
                sequence[state_idx] = 1 - sequence[state_idx]
            operation_times += 1
    return sequence, operation_times
