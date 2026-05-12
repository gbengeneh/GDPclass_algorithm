# Each function is a sub-problem, a small, manageable part of the larger task.

def get_ingredients():
    """Represents gathering ingredients from the pantry and fridge."""
    print("1. Gathering ingredients: Tofu, Bell Peppers, Onions, Soy Sauce, Ginger.")
    ingredients = ['Tofu', 'Bell Peppers', 'Onions', 'Soy Sauce', 'Ginger']
    return ingredients

def chop_vegetables(ingredients):
    """Represents the pre-preparation (mise en place) step."""
    print("\n2. Chopping vegetables and protein.")
    # In a real program, this would involve more complex logic.
    chopped_ingredients = {
        'protein': 'Chopped Tofu',
        'vegetables': ['Sliced Bell Peppers', 'Diced Onions']
    }
    print("   - Tofu, Bell Peppers, and Onions are now chopped.")
    return chopped_ingredients

def cook_stir_fry(components):
    """Represents the cooking process."""
    print("\n3. Cooking the stir-fry.")
    print(f"   - Sautéing {components['vegetables'][1]} and {components['protein']}.")
    print(f"   - Adding {components['vegetables'][0]} and cooking until tender.")
    print(f"   - Adding Soy Sauce and Ginger for flavor.")
    print("   - Stir-fry is ready!")
    return "Delicious Vegetable Stir-fry"

def serve_dish(final_dish):
    """Represents plating and serving the meal."""
    print("\n4. Serving the meal.")
    print(f"   - Plating the {final_dish}.")
    print("   - Enjoy your meal!")

# --- Main Program: The Master Chef ---
# The main part of the program now reads like a high-level recipe,
# combining the solutions from all the sub-problems.

def make_vegetable_stir_fry():
    """
    Main function that orchestrates the entire process by calling
    the decomposed functions in the correct order.
    """
    print("--- Starting to Make Vegetable Stir-fry ---")
    
    # Each function call solves one part of the problem.
    all_ingredients = get_ingredients()
    prepared_components = chop_vegetables(all_ingredients)
    cooked_dish = cook_stir_fry(prepared_components)
    serve_dish(cooked_dish)

    print("\n--- Meal preparation complete! ---")

# Run the main program
if __name__ == "__main__":
    make_vegetable_stir_fry()