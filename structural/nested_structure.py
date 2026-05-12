#Nested strutures
def analyze_nested_structure(data):

    def count_depth(obj, current_depth=0):
        if isinstance(obj,(list, tuple)):
            if not obj:
                return current_depth
            return max(count_depth(item, current_depth + 1) for item in obj)
        elif isinstance(obj, dict):
            if not obj:
                return current_depth
            return max(count_depth(value, current_depth + 1) for value in obj.values())
        else:
            return current_depth
        
    depth = count_depth(data)
    print(f"Maximum depth of nested structure: {depth}")
    return depth

#test nested structure
nested_data = [3, [6, [3, [4,[ 5,[ 8]]]]]]
analyze_nested_structure(nested_data)
         
