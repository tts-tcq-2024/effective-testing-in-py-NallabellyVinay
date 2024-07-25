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

color_map = generate_color_map()
print_color_map(color_map)

# Test the generated color map
assert(len(color_map) == 25)  # Ensure there are 25 entries
assert(color_map[0] == ' 0 | White  | Blue  ')  # Check the format of the first entry
assert(color_map[24] == '24 | Violet | Slate ')  # Check the format of the last entry
