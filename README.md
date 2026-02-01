# Daily U.S. IPO Monitoring Automation

---

## **Overview**

This project implements an automated workflow that monitors **same-day U.S. IPOs** and sends an email notification when IPOs meet a defined offer-size threshold.

The automation runs **daily at 9:00 AM Dubai time (UTC+4)**.

---

## **Automation Logic**

- Monitor **U.S. stock market IPOs**
- Consider **only today’s IPOs** (not future listings)
- Calculate offer amount:

IPO Price × Number of Shares


- Filter IPOs with **offer size > USD 200 million**
- Send automated email notification with qualifying ticker symbols

---

## **Technologies Used**

### **Language**
- Python 3.10+

### **Market Data**
- Finnhub IPO Calendar API

### **Automation & Scheduling**
- GitHub Actions (cron-based scheduler)

### **Email Service**
- Gmail SMTP (SSL with App Password)

### **Libraries**
- requests  
- pytz  
- python-dotenv  

---

## **Project Structure**

automation-workflow/
│
├── ipo_monitor.py
├── requirements.txt
├── .gitignore
└── .github/
└── workflows/
└── ipo.yml


---

## **Environment Variables**

Stored securely using environment variables.

FINNHUB_API_KEY=xxxxxxxxxxxx

SMTP_EMAIL=yourgmail@gmail.com
SMTP_PASSWORD=gmail_app_password
TO_EMAIL=yourgmail@gmail.com


---

## **Schedule**

- Runs daily at **9:00 AM Dubai time**
- Cron expression:

0 5 * * *


---

## **Email Output**

**Subject**
Daily U.S. IPO Monitor – Same-Day IPOs Above $200M


**Email includes:**
- Execution date
- Filter criteria
- Qualified IPO ticker symbols
- Calculated offer amounts

If no IPO qualifies, a confirmation email is still sent.

---

## **Why Finnhub**

- Reliable U.S. IPO calendar data  
- Provides IPO price and share count  
- Clean and stable REST API  
- Covers NASDAQ and NYSE listings  

---

## **Verification**

- GitHub Actions execution logs  
- Manual workflow trigger  
- Email delivery confirmation  
- Screen recording for review  

---

## **Summary**

This automation demonstrates:

- Timezone-aware scheduling  
- Market-data integration  
- Deterministic filtering logic  
- Secure credential handling  
- Fully automated daily workflow  

---

**Author:**  
**Muhammed Afsal P M**