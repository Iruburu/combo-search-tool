# 🔍 Combo Search Tool

A simple and efficient terminal-based tool for searching specific text patterns across multiple files.  
Built in **Python**, it uses `tqdm` for progress visualization and handles directories, user input, and file management smoothly.

---

## ⚙️ Features
- ✅ Reads all files in a given folder  
- 🔎 Searches for specific keywords or patterns inside each file  
- 💾 Option to save the matching lines into an output file  
- 🧹 Clears the terminal for a clean interface  
- 📊 Displays progress with a loading bar (`tqdm`)

---

## 🚀 Usage

### 1. Install dependencies
```bash
pip install tqdm
```

### 2. Run the script
```bash
python combo_search.py
```

### 3. Follow the prompts
- Enter the path of your folder containing text files  
- Type the word or phrase you want to search for  
- Wait for the scan to finish  
- Optionally, save results into an output file  

---

## 🧠 Example
```
Path combos: ./combos
Search terms: gmail.com

Lendo os combos: 100%|██████████████████████████████████████| 50/50 [00:02<00:00, 24.78it/s]

Results found:
email1@gmail.com:password123
email2@gmail.com:qwerty

Save result? [y or N]: y
Result filename: gmail_hits.txt
```

---

## 📂 Output
All saved results are stored inside the `./output/` folder automatically.

Example:
```
/output/gmail_hits.txt
```

---

## 📘 Notes
This project is designed for **educational and ethical use only**.  
Do **not** use it to process or distribute unauthorized, leaked, or sensitive data.

You can safely test this tool using your **own files** or **dummy data**, for example:
```
test_user@example.com:12345
demo_user@gmail.com:qwerty
```

---

## 🛠️ Technologies
- Python 3.8+
- tqdm
- os, sys, and built-in modules

---

## 💡 Future Improvements
- Add regex-based search  
- Support for `.zip` or large dataset reading  
- Option to ignore case sensitivity  

---

## 👨‍💻 Author
**Iruburu Viturino**  
Dev Web | Ethical Hacker  
📍 [GitHub Profile](https://github.com/yourusername)

---
