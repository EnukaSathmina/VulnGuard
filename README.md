# 🛡️ VulnGuard

VulnGuard is a web vulnerability scanner designed to detect common security issues in web applications such as SQL Injection, Cross-Site Scripting (XSS), missing security headers, and other basic web security flaws.

> ⚠️ Disclaimer: This tool is intended for educational and authorized security testing purposes only. Do NOT use it on websites you do not own or do not have permission to test.

---

## 🚀 Features

- 🌐 Scan websites using a target URL
- 🔍 Detect common vulnerabilities:
  - SQL Injection (SQLi)
  - Cross-Site Scripting (XSS)
  - Missing Security Headers
  - Basic endpoint exposure checks
- ⚡ Fast Python-based scanning engine
- 🧾 Structured JSON output for results
- 🖥️ Simple launcher script support

---

## 🏗️ Tech Stack

- Python 🐍
- FastAPI ⚡
- Requests library
- BeautifulSoup (if used for parsing)
- HTTP analysis modules

---

## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/VulnGuard.git
cd VulnGuard
```

### 2. Create virtual environment (recommended)
```bash
python -m venv venv
venv\Scripts\activate   # Windows
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```

## ▶️ Running VulnGuard
### 1. Start the backend server
```bash
uvicorn main:app --reload
```

### 2. Run the frontend
Open the file manually:
```
frontend/index.html
```
👉 Just double-click it or open it in your browser.

OR (Recommended) Use launcher script
```
python launcher.py
```

# 🔐 Legal & Ethical Use

VulnGuard is strictly for:

- Educational purposes
- Security testing with permission
- Personal or lab environments

# 🚫 Do NOT use on:

- Unauthorized websites
- Government or financial systems
- Any system you do not own or have permission to test
---
💡 Future Improvements
- Expanded vulnerability detection rules
- Full website crawling support
- Advanced reporting system (PDF/HTML export)
- Plugin-based scanner modules
- Performance optimizations

<h2 align="center">👨‍💻 Author</h2>

<p align="center">
  Made by <b>Enuka Sathmina</b>
</p>
