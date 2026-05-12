                            # Example: Fibonacci Sequence
def recognize_fibonacci_pattern():
    
    sequence = [0, 1]
    
    # Generate next 10 numbers by recognizing the pattern
    for i in range(10):
        next_num = sequence[-1] + sequence[-2]
        sequence.append(next_num)
    
    print("Fibonacci Sequence:", sequence)
    return sequence

recognize_fibonacci_pattern()