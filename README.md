# 🔍 TCP Port Scanner

A simple and powerful **TCP port scanner** built with Python. It allows you to scan open TCP ports on a target IP with customizable port ranges, timeout settings, and output saving.  
Perfect for ethical hackers, network admins, or anyone curious about network services.

![banner](https://img.shields.io/badge/Built%20With-Python-blue?style=flat-square)
![license](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

## 🚀 Features

- Scan **specific ports** or a **range** of ports (e.g., `20-80` or `22,80,443`)
- Detect open ports with **service names** if available
- Supports **custom timeout**
- Save scan results to a file
- Clean and **colorful CLI interface**
- Graceful **keyboard interrupt handling**

---

## 📦 Requirements

Ensure you have Python 3 installed. Install the required modules:

```bash
pip install termcolor pyfiglet
```

---

## 🛠️ Usage

```bash
python tcp_scanner.py -t <target_ip> -p <ports> [-T <timeout>] [-o <output_file>]
```

---

## 🧾 Arguments

| Flag               | Description                                                   | Required | Default                   |
|--------------------|---------------------------------------------------------------|----------|----------------------------|
| `-t`, `--target`   | Target IP address or domain to scan                           | ✅ Yes   | –                          |
| `-p`, `--ports`    | Port range or list (e.g., `22,80,443` or `1-1024`)            | ❌ No    | `1-1024`                   |
| `-T`, `--timeout`  | Timeout in seconds for each connection attempt                | ❌ No    | `1`                        |
| `-o`, `--output`   | Output file to save the scan results                          | ❌ No    | `results_tcp_scanner.txt` |

---

## 📂 Example

```bash
python tcp_scanner.py -t 192.168.1.1 -p 20-100 -T 2 -o scan_results.txt
```

---

## ⚠️ Disclaimer

- This project is for educational purposes only. Do not use these implementations in production or real-world security systems. They lack the security protections of real cryptographic libraries.

---

## 📜 License

This project is licensed under the MIT License.

---

## 📧 Contact

- Made with ❤️ by 7ima-SR
- Website:https://ibrahim-elsaied.netlify.app/

