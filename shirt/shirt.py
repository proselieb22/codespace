import os
import sys
from PIL import Image, ImageOps

def overlay_shirt(input_image, output_image):
    # Check if input and output files have correct extensions
    valid_extensions = ['.jpg', '.jpeg', '.png']
    input_extension = os.path.splitext(input_image)[1].lower()
    output_extension = os.path.splitext(output_image)[1].lower()

    if input_extension not in valid_extensions or output_extension not in valid_extensions:
        sys.exit("Invalid input/output file format")

    # Check if input and output extensions match
    if input_extension != output_extension:
        sys.exit("Input and output have different extensions")

    # Check if input file exists
    if not os.path.exists(input_image):
        sys.exit("Input does not exist")

    # Open input and shirt images
    try:
        input_img = Image.open(input_image)
        shirt = Image.open("shirt.png")  # Replace "shirt.png" with the actual shirt image file name

        # Resize input image to the same size as shirt image
        input_img = ImageOps.fit(input_img, shirt.size, method=0, bleed=0.0, centering=(0.5, 0.5))

        # Overlay shirt on input image
        input_img.paste(shirt, (0, 0), shirt)

        # Save the result
        input_img.save(output_image)
        print(f"Shirt overlay saved as {output_image}")
    except FileNotFoundError:
        sys.exit("Could not open one of the images")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Too few or too many command-line arguments")

    input_image = sys.argv[1]
    output_image = sys.argv[2]

    overlay_shirt(input_image, output_image)
