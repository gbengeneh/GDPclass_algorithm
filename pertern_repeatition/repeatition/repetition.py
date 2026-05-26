def find_repeating_pattern(sequence):
    """
    Find if there's a repeating pattern in a sequence
    Example: [1,2,3,1,2,3,1,2,3] has pattern [1,2,3]
    """
    n = len(sequence)
    
    # Try different pattern lengths
    for pattern_length in range(1, n // 2 + 1):
        pattern = sequence[:pattern_length]
        
        # Check if this pattern repeats throughout
        is_repeating = True
        for i in range(pattern_length, n):
            if sequence[i] != pattern[i % pattern_length]:
                is_repeating = False
                break
        
        if is_repeating:
            repetitions = n // pattern_length
            print(f"Repeating pattern found: {pattern}")
            print(f"Pattern repeats {repetitions} times")
            return pattern
    
    print("No repeating pattern found")
    return None

# Test
sequence = [1, 2, 3, 1, 2,3, 1, 2, 3]
find_repeating_pattern(sequence)