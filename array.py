arr = [10, 20, 30, 40]
# insert to the last index
arr.append(50)  
print(arr)  # Output: [10, 20, 30, 40, 50]
# insert in the middle
arr.insert(2, 25)
print(arr)  # Output: [10, 20, 25, 30, 40, 50]

# remove from the end
arr.pop()
print(arr)  # Output: [10, 20, 25, 30, 40]
# remove from the middle
arr.remove(25)
print(arr)  # Output: [10, 20, 30, 40]