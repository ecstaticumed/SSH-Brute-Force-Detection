# 🔐 SSH Brute Force Attack Detection and Automatic Prevention System

## 📌 Overview
This project implements a **real-time SSH brute-force attack detection and prevention system**.  
It monitors SSH authentication logs, detects repeated failed login attempts from malicious IP addresses, and automatically blocks those IPs using a firewall.

The project is designed for **Information Security / Cyber Security coursework** and demonstrates a practical **Intrusion Detection and Prevention System (IDPS)** concept.

---

## 🎯 Objectives
- Detect SSH brute-force login attempts
- Monitor authentication logs in real time
- Automatically block malicious IP addresses
- Reduce the risk of unauthorized system access
- Demonstrate real-world defensive security techniques

---

## 🛠️ Tools & Technologies
- **Operating System:** Kali Linux / Ubuntu  
- **Programming Language:** Python 3  
- **Firewall:** UFW (Uncomplicated Firewall)  
- **SSH Service:** OpenSSH  
- **Log Source:** systemd journal (`journalctl`)  

---

## 🧠 How It Works
1. An attacker attempts multiple SSH logins using incorrect credentials  
2. Failed login attempts are recorded in system authentication logs  
3. The Python script monitors SSH logs in real time  
4. Failed attempts per IP address are counted  
5. If attempts exceed a defined threshold:
   - The IP is marked as malicious
   - The firewall blocks the IP automatically
   - A security alert is generated

---

## ⚙️ Installation & Setup

### 1️⃣ Install and Enable SSH
```bash
sudo apt update
sudo apt install openssh-server -y
sudo systemctl start ssh
sudo systemctl enable ssh
```
## 2️⃣ Enable Firewall (UFW)
```bash
sudo apt install ufw -y
sudo ufw allow ssh
sudo ufw enable
sudo ufw status
```
## 3️⃣ Run the Detection Script
```bash
sudo python3 ssh_bruteforce_realtime.py
```
## 📊 Sample Output
```bash
[ALERT] Blocking SSH brute-force IP: 192.168.1.105
```
## 🛡️ Security Features
```bash
- Real-time SSH log monitoring
- Automatic intrusion prevention
- Threshold-based attack detection
- Firewall-level IP blocking
```
## 👤 Author

Umed Ali
BS Cyber Security
SMI University Karachi
