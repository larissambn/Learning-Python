import math

# Initialize the current position to the original point (0, 0)
x, y = 0, 0

# Iterate through the movements
while True:
    try:
        # Get the movement and steps as input
        movement, steps = input().split()
        
        # Convert steps to an integer
        steps = int(steps)
        
        # Update the current position based on the movement
        if movement == 'UP':
            y += steps
        elif movement == 'DOWN':
            y -= steps
        elif movement == 'LEFT':
            x -= steps
        elif movement == 'RIGHT':
            x += steps
        else:
            # Invalid input, skip this line
            continue
    except ValueError:
        # Invalid input, skip this line
        continue
    except EOFError:
        # End of input
        break

# Calculate the Euclidean distance from the original point
distance = math.sqrt(x**2 + y**2)

# Round the distance to the nearest integer
rounded_distance = round(distance)

# Print the result
print(rounded_distance)
