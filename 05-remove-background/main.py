from rembg import remove

# Path to the input image file
input_path = "cat.jpg"

# Path where the output image (background removed) will be saved
output_path = "removed.png"

# Open the input image in binary read mode
with open(input_path, 'rb') as i:
    # Open the output file in binary write mode
    with open(output_path, 'wb') as o:
        # Read the input image as bytes
        input_file = i.read()

        # Remove the background from the image
        output_file = remove(input_file)

        # Write the processed image to the output file
        o.write(output_file)
