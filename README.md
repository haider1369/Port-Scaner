# 🔍 Python Port Scanner

A fast, multithreaded **Port Scanner** built using Python.  
Perfect for cybersecurity students, ethical hacking practice, and GitHub portfolio projects.

---

## 🚀 Features

✔ Scan a single port  
✔ Scan a range of ports  
✔ Full 1–65535 port scan  
✔ Banner grabbing  
✔ Service detection  
✔ Multithreaded (FAST)  
✔ Works on Windows, Linux, macOS  

---

## 🛠️ How It Works

The scanner uses:
- `socket.connect_ex()` to check if a port is open  
- Multithreading to increase speed  
- Timeout control for efficiency  
- Banner grabbing using simple socket messages  

---
## ▶️ Usage

Run the script:

```bash
python port_scanner.py
```
Example interaction:
```
Enter target: scanme.nmap.org
Scan Types:
1. Single Port
2. Port Range
3. Full Scan (1–65535)

Select option: 2
Start: 20
End: 100
```
---

## 📜 License
MIT License.

---

## 👤 Author
Created by **Haider Sultan**  
Cybersecurity Student & Python Learner



