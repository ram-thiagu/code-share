from PIL import Image
import os

def rotate_and_save_images(input_folder, output_folder):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all files in the input folder
    files = os.listdir(input_folder)

    # Filter out only PNG images
    png_files = [file for file in files if file.lower().endswith('.png')]

    # Process each PNG image
    for png_file in png_files:
        # Construct full paths
        input_path = os.path.join(input_folder, png_file)
        output_path = os.path.join(output_folder, png_file)

        # Open the image
        image = Image.open(input_path)

        # Rotate the image by 180 degrees
        rotated_image = image.rotate(180)

        # Save the rotated image to the output folder
        rotated_image.save(output_path)

if __name__ == "__main__":
    # Specify input and output folders
    input_folder = "path/to/input_folder"
    output_folder = "path/to/output_folder"

    # Rotate and save images
    rotate_and_save_images(input_folder, output_folder)
