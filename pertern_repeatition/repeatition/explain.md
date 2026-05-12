# Understanding the `find_repeating_pattern()` Function

This function checks whether a sequence (list) contains a repeating pattern.

Example:

```python
[1,2,3,1,2,3,1,2,3]
```

The repeating pattern is:

```python
[1,2,3]
```

because it repeats multiple times.

---

# Full Code

```python
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
```

---

# Step-by-Step Explanation

---

## 1. Function Definition

```python
def find_repeating_pattern(sequence):
```

This creates a function named:

```python
find_repeating_pattern
```

The function accepts one parameter:

```python
sequence
```

This parameter represents the list we want to analyze.

Example:

```python
sequence = [1,2,3,1,2,3]
```

---

## 2. Docstring

```python
"""
Find if there's a repeating pattern in a sequence
Example: [1,2,3,1,2,3,1,2,3] has pattern [1,2,3]
"""
```

This is documentation explaining what the function does.

---

## 3. Get the Length of the Sequence

```python
n = len(sequence)
```

`len()` counts the number of items in the list.

Example:

```python
sequence = [1,2,3,1,2,3,1,2,3]
```

Length:

```python
n = 9
```

---

# 4. Try Different Pattern Lengths

```python
for pattern_length in range(1, n // 2 + 1):
```

This loop tries different possible pattern sizes.

---

## Why `n // 2`?

A repeating pattern cannot be larger than half of the sequence.

Example:

```python
[1,2,3,1,2,3]
```

Length = 6

Possible pattern sizes:

- 1
- 2
- 3

---

## Understanding `range(1, n // 2 + 1)`

If:

```python
n = 9
```

Then:

```python
n // 2 = 4
```

So:

```python
range(1,5)
```

means:

```python
1,2,3,4
```

The function will test pattern lengths:

- 1
- 2
- 3
- 4

---

# 5. Extract a Possible Pattern

```python
pattern = sequence[:pattern_length]
```

This slices the beginning of the sequence.

Example:

If:

```python
pattern_length = 3
```

Then:

```python
pattern = sequence[:3]
```

Result:

```python
[1,2,3]
```

---

# 6. Assume the Pattern Works

```python
is_repeating = True
```

Initially, the code assumes the pattern repeats correctly.

If an error is found later, it changes to:

```python
False
```

---

# 7. Check the Remaining Elements

```python
for i in range(pattern_length, n):
```

This loop checks every remaining item in the sequence.

Example:

```python
range(3,9)
```

means:

```python
3,4,5,6,7,8
```

---

# 8. Main Comparison Logic

```python
if sequence[i] != pattern[i % pattern_length]:
```

This is the most important line in the program.

---

# Understanding the `%` Operator

`%` means modulus (remainder).

Example:

```python
7 % 3
```

Result:

```python
1
```

because:

```python
7 ÷ 3 = 2 remainder 1
```

---

# Why Use `%` Here?

It allows the code to cycle through the pattern repeatedly.

Suppose:

```python
pattern = [1,2,3]
```

Indexes:

```python
0 1 2
```

Now look at this:

| i | i % 3 |
|---|---|
| 3 | 0 |
| 4 | 1 |
| 5 | 2 |
| 6 | 0 |
| 7 | 1 |
| 8 | 2 |

Notice how the indexes repeat:

```python
0,1,2,0,1,2...
```

This allows the function to compare the sequence against the repeating pattern.

---

# Real Example

Sequence:

```python
[1,2,3,1,2,3,1,2,3]
```

Pattern:

```python
[1,2,3]
```

Comparisons:

| i | sequence[i] | i % 3 | pattern[i % 3] |
|---|---|---|---|
| 3 | 1 | 0 | 1 |
| 4 | 2 | 1 | 2 |
| 5 | 3 | 2 | 3 |
| 6 | 1 | 0 | 1 |
| 7 | 2 | 1 | 2 |
| 8 | 3 | 2 | 3 |

All values match.

---

# 9. If a Mismatch Occurs

```python
is_repeating = False
break
```

Example:

```python
[1,2,3,1,2,9]
```

Eventually:

```python
9 != 3
```

Then:

```python
is_repeating = False
```

`break` immediately exits the loop.

---

# 10. If the Pattern is Valid

```python
if is_repeating:
```

If no mismatch was found:

---

# 11. Count Repetitions

```python
repetitions = n // pattern_length
```

Example:

```python
9 // 3 = 3
```

The pattern repeats 3 times.

---

# 12. Print the Pattern

```python
print(f"Repeating pattern found: {pattern}")
```

Output:

```python
Repeating pattern found: [1, 2, 3]
```

---

# 13. Print Number of Repetitions

```python
print(f"Pattern repeats {repetitions} times")
```

Output:

```python
Pattern repeats 3 times
```

---

# 14. Return the Pattern

```python
return pattern
```

The function sends the pattern back.

---

# 15. If No Pattern Exists

```python
print("No repeating pattern found")
return None
```

If every possible pattern length fails, the function prints a message and returns `None`.

---

# Test Example

```python
sequence = [1, 2, 3, 1, 2, 3, 1, 2, 3]
find_repeating_pattern(sequence)
```

---

# Final Output

```python
Repeating pattern found: [1, 2, 3]
Pattern repeats 3 times
```

---

# Important Concepts Used

## Functions

```python
def
```

---

## Loops

```python
for
```

---

## List Slicing

```python
sequence[:3]
```

---

## Modulus Operator

```python
%
```

---

## Boolean Values

```python
True / False
```

---

## Conditional Statements

```python
if
```

---

# Simple Visual Summary

```text
Try small patterns
        ↓
Compare against entire sequence
        ↓
If all values match
        ↓
Pattern found
```

---

# Key Idea

The modulus operator `%` is the secret behind the repeating check.

Example:

```python
i % pattern_length
```

This continuously cycles through the pattern indexes:

```python
0,1,2,0,1,2...
```

which allows the program to compare repeating sections correctly.