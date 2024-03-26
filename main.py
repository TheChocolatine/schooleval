from PIL import Image

# Create a new image with a white background
image = Image.new("RGB", (100, 100), "white")
pixels = image.load()

# Define the colors for tree and trunk
tree_color = (34, 139, 34)  # Green color for the tree
trunk_color = (139, 69, 19)  # Brown color for the trunk

# Define the coordinates for the tree top
tree_top_x = 50
tree_top_y = 30

# Draw the tree top
for y in range(tree_top_y - 10, tree_top_y + 11):
    for x in range(tree_top_x - 10, tree_top_x + 11):
        if (x - tree_top_x) ** 2 + (y - tree_top_y) ** 2 <= 100:
            pixels[x, y] = tree_color

# Draw the trunk with a loop
trunk_width = 10
trunk_height = 30
trunk_left = tree_top_x - trunk_width // 2
trunk_right = tree_top_x + trunk_width // 2
trunk_top = tree_top_y + 10
trunk_bottom = trunk_top + trunk_height

for y in range(trunk_top, trunk_bottom):
    for x in range(trunk_left, trunk_right):
        pixels[x, y] = trunk_color

# Draw some branches using additional loops
for i in range(5):
    branch_length = 10 - i * 2
    branch_start_x = tree_top_x + 2 * i
    branch_start_y = tree_top_y - 3 * i

    for j in range(branch_length):
        pixels[branch_start_x + j, branch_start_y - j] = tree_color

# Save the image
image.save("tree_image.png")

# Show the image
image.show()
