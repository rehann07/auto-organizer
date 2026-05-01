# 🧹 Workspace Auto-Organizer

> *"I treat manual repetition as a bug that needs to be automated out of my day."*

## 📌 Overview
As a backend developer, my workspace—especially the 'Downloads' folder—constantly gets cluttered with `.log` files, `.json` responses, `.jar` builds, and various PDFs while building and testing microservices. 

Instead of manually sorting my workspace every week, I wrote this Python automation script. It scans a target directory and automatically routes files into designated sub-folders based on their extensions, keeping the environment clean and distraction-free.

## ⚙️ How It Works
The script maps file extensions to specific categories and moves them automatically:
*   **Code_and_Logs:** `.log`, `.json`, `.xml`, `.jar`, `.py`, `.js`, `.java`
*   **Documents:** `.pdf`, `.docx`, `.txt`, `.csv`, `.xlsx`
*   **Media:** `.jpg`, `.jpeg`, `.png`, `.mp4`, `.mp3`
*   **Archives:** `.zip`, `.tar`, `.gz`, `.rar`
*   **Others:** Catch-all for undefined file types.

## 🚀 Usage

1. Clone the repository:
   
    ```bash
    git clone 
    ```
2. Navigate to the directory:
   
    ```bash
    cd auto-organizer
    ```
3. Open `auto_organizer.py` and update the `directory_to_clean` variable at the bottom to point to your target folder (e.g., your Downloads folder).
4. Run the script:
   ```bash
   python auto_organizer.py
   ```

## 🛠️ Built With
*   Python 3.x
*   `os` and `shutil` (Built-in libraries, zero external dependencies required)
