import os
import sys
from tqdm import tqdm

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

# ==============================
# Utility Functions
# ==============================

def clear_terminal():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def ask_folder() -> str:
    """Asks the user for a folder path and validates it."""
    while True:
        path = input('📂  Enter combo folder path: ').strip()
        if os.path.exists(path) and os.path.isdir(path):
            return path
        clear_terminal()
        print('❌ Folder not found. Please try again.\n')


def save_result(result: str):
    """Saves the search results into ./output folder."""
    os.makedirs('./output', exist_ok=True)

    filename = input('\n💾 Output filename: ').strip()
    output_path = os.path.join('./output', filename or 'result.txt')

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(result)

    print(f'\n✅ Result saved at: {os.path.abspath(output_path)}')


# ==============================
# Core Logic
# ==============================

def read_files(path: str, search: str):
    """Reads files from the folder and searches for the given term."""
    files = [
        f for f in os.listdir(path)
        if os.path.isfile(os.path.join(path, f))
    ]

    result_data = ''
    found_count = 0

    print(f'\n🔍 Searching for: "{search}"\n')

    for filename in tqdm(files, desc='Reading files', ncols=80):
        full_path = os.path.join(path, filename)

        try:
            with open(full_path, 'r', encoding='utf-8') as file:
                for line in file:
                    if search in line:
                        found_count += 1
                        result_data += line.strip() + '\n'
        except Exception as e:
            print(f'\n⚠️  Error reading {filename}: {e}')

    clear_terminal()
    print('================ SEARCH RESULTS ================\n')

    if result_data:
        print(result_data)
        print(f'\n🔸 Total matches found: {found_count}\n')
        if input('Save results? [y/N]: ').lower() == 'y':
            save_result(result_data)
    else:
        print('No matches found.\n')


def main():
    clear_terminal()
    print('===============================')
    print('     🔎 COMBO SEARCH TOOL      ')
    print('===============================\n')

    path = ask_folder()
    search = input('🧩  Search term: ').strip()
    clear_terminal()
    read_files(path, search)


if __name__ == '__main__':
    main()