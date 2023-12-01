import os

def rename_images_with_prefix(input_folder):
    # List all files in the input folder
    files = os.listdir(input_folder)

    # Filter out only PNG images
    png_files = [file for file in files if file.lower().endswith('.png')]

    # Rename each PNG image
    for png_file in png_files:
        # Construct full paths
        current_path = os.path.join(input_folder, png_file)
        new_name = f"180_{png_file}"
        new_path = os.path.join(input_folder, new_name)

        # Rename the file
        os.rename(current_path, new_path)

if __name__ == "__main__":
    # Specify input folder
    input_folder = "path/to/input_folder"

    # Rename images with prefix
    rename_images_with_prefix(input_folder)
