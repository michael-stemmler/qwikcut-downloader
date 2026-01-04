# QwikCut Game Downloader

A lightweight Python CLI tool designed for coaches and athletes to batch download game footage clips from QwikCut URL patterns.

It automates the tedious process of downloading clips one by one, organizes them into folders, and ensures they are named correctly for proper sorting (e.g., `clip_001.mp4`).

## 🚀 Features

* **Batch Downloading:** Downloads an entire game (e.g., 100+ clips) automatically based on a URL pattern.
* **Smart Sorting:** Renames files with leading zeros (e.g., `clip_001.mp4` instead of `clip_1.mp4`) so file explorers sort them correctly.
* **Visual Progress Bar:** Shows a real-time progress bar for each file download directly in the terminal.
* **Resume Capability:** Skips files that have already been downloaded to save bandwidth and time.
* **Organized Output:** Automatically creates a sub-folder for each game.

## 📋 Prerequisites

* **Python 3.x** installed on your machine.
* The `requests` library.

## 🛠️ Installation

1.  **Clone the repository** (or just download the ZIP):
    ```bash
    git clone https://github.com/michael-stemmler/qwikcut-downloader.git
    cd qwikcut-downloader
    ```

2.  **Install dependencies:**
    ```bash
    pip install requests
    ```

## 📖 Usage

### 1. Get the Base URL
To use this script, you need the "Base URL" of the video files.
1.  Log in to QwikCut and open your game.
2.  Click on the download icon of the **first clip** (Clip #1) to open the player.
3.  Right-click the video (or look at the browser URL if it opens in a new tab) and copy the link.
    * *Example Link:* `https://d2htis0rx2m2xo.cloudfront.net/uploads/68b48b97f1899/1.mp4`
4.  **Remove the `1.mp4`** at the end.
    * *Base URL:* `https://d2htis0rx2m2xo.cloudfront.net/uploads/68b48b97f1899/`

### 2. Run the Script
Open your terminal and run the script with the following parameters:

* `--url`: The Base URL you found above.
* `--count`: Total number of clips in the game (e.g., 97).
* `--name`: The name of the folder where videos will be saved.

```bash
python qwikcut_downloader.py --url "https://YOUR_BASE_URL_HERE/" --count 97 --name "Wolves_vs_Phonix"
```


### 3. 📂 Output Structure
```
Game_Downloads/
└── Wolves_vs_Phonix/
    ├── clip_001.mp4
    ├── clip_002.mp4
    ├── ...
    └── clip_097.mp4
```

## ⚠️ Disclaimer
This tool is intended for educational purposes and for personal archiving of team footage by authorized coaches and athletes.

Please ensure you comply with the Terms of Service of the hosting platform. Do not use this tool to download content you do not have the rights to access. The authors of this script are not responsible for any misuse.   
Do not share copyrighted material publicly.

## 📄 License
This project is licensed under the MIT License - see the [LICENSE file](LICENSE) for details. You are free to modify and distribute this software.



