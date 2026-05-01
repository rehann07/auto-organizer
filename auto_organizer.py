import os
import shutil

def organize_directory(target_dir):
    """
    Automates the cleanup of a cluttered directory by sorting files into 
    subfolders based on their extensions.
    """
    # Dictionary mapping folder names to their file extensions
    file_types = {
        "Code_and_Logs": ['.log', '.json', '.xml', '.jar', '.py', '.js', '.java'],
        "Documents": ['.pdf', '.docx', '.txt', '.csv', '.xlsx'],
        "Media": ['.jpg', '.jpeg', '.png', '.mp4', '.mp3'],
        "Archives": ['.zip', '.tar', '.gz', '.rar']
    }

    # Ensure the target directory exists
    if not os.path.exists(target_dir):
        print(f"Directory {target_dir} does not exist.")
        return

    # Scan through files in the target directory
    for filename in os.listdir(target_dir):
        file_path = os.path.join(target_dir, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        file_ext = os.path.splitext(filename)[1].lower()
        moved = False

        # Match file extension to a category and move it
        for folder, extensions in file_types.items():
            if file_ext in extensions:
                folder_path = os.path.join(target_dir, folder)
                os.makedirs(folder_path, exist_ok=True)
                
                shutil.move(file_path, os.path.join(folder_path, filename))
                print(f"Moved: {filename} -> {folder}/")
                moved = True
                break
        
        # Catch-all for other files
        if not moved:
            others_path = os.path.join(target_dir, "Others")
            os.makedirs(others_path, exist_ok=True)
            shutil.move(file_path, os.path.join(others_path, filename))
            print(f"Moved: {filename} -> Others/")

if __name__ == "__main__":
    # Point this to your Downloads folder or any cluttered directory
    directory_to_clean = "./downloads_test" # Change this to your actual path if testing
    organize_directory(directory_to_clean)
    print("Workspace optimized! 🚀")