

# Example: Arithmetic Progression
def recognize_arithmetic_pattern(data):
    """
    Recognize if a sequence follows an arithmetic pattern
    Example: 2, 5, 8, 11, 14 (difference of 3)
    """
    if len(data) < 2:
        return None
    
    differences = [data[i+1] - data[i] for i in range(len(data)-1)]
    
    # Check if all differences are the same
    if len(set(differences)) == 1:
        common_diff = differences[0]
        print(f"Arithmetic pattern found! Common difference: {common_diff}")
        
        # Predict next 5 numbers
        predictions = []
        last_num = data[-1]
        for i in range(1, 6):
            predictions.append(last_num + (common_diff * i))
        
        print(f"Next 5 numbers will be: {predictions}")
        return common_diff, predictions
    else:
        print("No arithmetic pattern found")
        return None

# Test it
data = [2, 4, 6, 8, 10, 12]
recognize_arithmetic_pattern(data)