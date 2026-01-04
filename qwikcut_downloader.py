import os
import requests
import argparse
import sys
import time

def print_progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=50, fill='█'):
    """
    Call in a loop to create terminal progress bar
    """
    if total == 0:
        return
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
    sys.stdout.flush()
    if iteration == total: 
        print()

def download_videos(base_url, video_count, game_name):
    # --- 1. Setup Directories ---
    main_folder = "Game_Downloads"
    target_folder = os.path.join(main_folder, game_name)

    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
        print(f"[INFO] Created directory: {target_folder}")
    else:
        print(f"[INFO] Saving to existing directory: {target_folder}")

    # --- 2. Validate and Clean URL ---
    if not base_url.endswith('/'):
        base_url += '/'

    print(f"[INFO] Starting download for '{game_name}' ({video_count} clips)...")
    print("-" * 60)


    padding_width = len(str(video_count))
    if padding_width < 3:
        padding_width = 3

    # --- 3. Download Loop ---
    for i in range(1, video_count + 1):

        url = f"{base_url}{i}.mp4"
        filename = f"clip_{str(i).zfill(padding_width)}.mp4"
        
        file_path = os.path.join(target_folder, filename)

        if os.path.exists(file_path):
            print(f"[SKIP] {filename} already exists.")
            continue

        print(f"Downloading {filename}...")

        try:
            response = requests.get(url, stream=True)
            total_size = int(response.headers.get('content-length', 0))
            block_size = 1024 
            wrote = 0
            
            if response.status_code == 200:
                with open(file_path, 'wb') as f:
                    for data in response.iter_content(block_size):
                        wrote += len(data)
                        f.write(data)
                        print_progress_bar(wrote, total_size, prefix='Progress:', suffix='Complete', length=40)
            else:
                print(f"[FAILED] Status Code: {response.status_code}")

        except Exception as e:
            print(f"\n[ERROR] Failed to download Clip {i}: {e}")

    print("-" * 60)
    print(f"[SUCCESS] All tasks finished for '{game_name}'.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Download QwikCut game videos automatically with progress bar.",
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument("--url", type=str, required=True, help="Base URL")
    parser.add_argument("--count", type=int, required=True, help="Total number of videos")
    parser.add_argument("--name", type=str, required=True, help="Name of the game")

    if len(sys.argv) == 1:
        print("\n[ERROR] No parameters provided.")
        sys.exit(1)

    args = parser.parse_args()
    download_videos(args.url, args.count, args.name)