from collections import Counter

def analyze_frequency_pattern(data):
    """
    Find the most common elements and their patterns
    """
    freq = Counter(data)
    
    print("Frequency Analysis:")
    for item, count in freq.most_common():
        print(f"  {item}: appears {count} times")
    
    # Find if there's a pattern in frequencies
    frequencies = list(freq.values())
    if len(set(frequencies)) == 1:
        print(f"\nPattern found: All elements appear exactly {frequencies[0]} times (uniform distribution)")
    elif frequencies == sorted(frequencies, reverse=True):
        print("\nPattern found: Zipf's law-like distribution (decreasing frequency)")
    
    return freq

# Example: Text analysis
text = "8 5 3 8 5 2 8 5 3 2 1"
words = text.split()
analyze_frequency_pattern(words)