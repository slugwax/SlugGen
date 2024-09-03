import random
import xml.etree.ElementTree as ET
import os
import sys

def generate_random_color():
    """Generate a random hex color code."""
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

def update_background_color(svg_content, new_color):
    """Update the background color in the SVG content."""
    root = ET.fromstring(svg_content)

    # Define the SVG namespace
    namespace = {'svg': 'http://www.w3.org/2000/svg'}

    # Find the rectangle element with the background color
    for rect in root.findall(".//svg:rect", namespace):
        rect.set("fill", new_color)

    # Convert the updated XML tree to a string
    return ET.tostring(root, encoding='utf-8', method='xml')

def create_svg_with_random_color(input_file, output_file):
    """Create a new SVG file with a random background color."""
    # Read the content of the input SVG file
    with open(input_file, 'r') as file:
        svg_content = file.read()

    # Generate a new random color
    new_color = generate_random_color()

    # Update the SVG content with the new background color
    updated_svg_content = update_background_color(svg_content, new_color)

    # Write the updated SVG content to the new file
    with open(output_file, 'wb') as file:
        file.write(updated_svg_content)

    print(f"Created new SVG file with background color {new_color}: {output_file}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python slugGen.py <number_of_repetitions>")
        sys.exit(1)

    try:
        num_repetitions = int(sys.argv[1])
        if num_repetitions <= 0:
            raise ValueError("Number of repetitions must be a positive integer.")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    input_file = 'input.svg'
    
    # Check if the input file exists
    if not os.path.isfile(input_file):
        print(f"Error: The file '{input_file}' does not exist.")
        sys.exit(1)

    # Repeat the process `num_repetitions` times
    for i in range(num_repetitions):
        # Generate a new output file name with the iteration number
        new_color = generate_random_color()
        output_file = f"{new_color[1:]}_{i}.svg"
        
        # Create a new SVG file with a random background color
        create_svg_with_random_color(input_file, output_file)

if __name__ == "__main__":
    main()