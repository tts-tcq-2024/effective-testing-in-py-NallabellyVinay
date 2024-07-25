def generate_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    color_map = []

    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            # Ensure proper alignment
            color_map.append(f'{i * 5 + j:2} | {major:<6} | {minor:<6}')

    return color_map

def print_color_map(color_map):
    for entry in color_map:
        print(entry)

# Generate the color map
color_map = generate_color_map()

# Print the color map
print_color_map(color_map)

# Debug print to check actual generated values
for i, entry in enumerate(color_map):
    print(f"Entry {i}: '{entry}'")

# Test the generated color map
expected_first_entry = ' 0 | White  | Blue  '
expected_last_entry = '24 | Violet | Slate '

# Check the number of entries
assert(len(color_map) == 25), f"Expected 25 entries, but got {len(color_map)}"

# Check the format of the first entry
assert(color_map[0] == expected_first_entry), f"First entry mismatch: Expected '{expected_first_entry}', but got '{color_map[0]}'"

# Check the format of the last entry
assert(color_map[24] == expected_last_entry), f"Last entry mismatch: Expected '{expected_last_entry}', but got '{color_map[24]}'"

print("All is well (maybe!)\n")
