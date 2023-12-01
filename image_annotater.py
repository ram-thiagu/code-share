import os

def create_txt_file(input_folder, output_file):
    # List all files in the input folder
    files = os.listdir(input_folder)

    # Filter out only image files
    image_files = [file for file in files if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]

    # Create and write to the output text file
    with open(output_file, 'w') as f:
        for image_file in image_files:
            image_path = os.path.join(input_folder, image_file)
            label = image_file[0]  # Get the first character of the image name
            f.write(f"{image_path} {label}\n")

if __name__ == "__main__":
    # Specify input folder and output text file
    input_folder = "path/to/input_folder"
    output_file = "path/to/output.txt"

    # Create the text file
    create_txt_file(input_folder, output_file)
