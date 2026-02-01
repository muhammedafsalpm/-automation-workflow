📈 Daily U.S. IPO Monitoring Automation
Overview

This project implements an automated workflow that monitors same-day U.S. IPOs and sends an email notification when IPOs meet a defined offer-size threshold.

The automation runs daily at 9:00 AM Dubai time (UTC+4) and performs the following checks:

Monitors only today’s IPOs (not future IPOs)

Calculates IPO offer amount:

Offer Amount = IPO Price × Number of Shares


Filters IPOs with offer size greater than USD 200 million

Sends an automated email listing qualifying ticker symbols

Produces execution logs for verification

✅ Functional Requirements Covered

✔ Runs automatically every day at 9:00 AM Dubai time
✔ U.S. stock market IPOs only
✔ Same-day IPOs only (today’s IPOs)
✔ Filters offer amount above USD 200 million
✔ Automated email notification
✔ Fully verifiable execution

🛠️ Technologies Used
Programming Language

Python 3.10+

Data Source

Finnhub API

Provides official U.S. IPO calendar data

Includes IPO price and number of shares offered

Automation & Scheduling

GitHub Actions

Cron-based scheduler

Executes daily at 9:00 AM Dubai time

Email Notification

Gmail SMTP (SSL)

Secure email delivery using App Password authentication

Libraries

requests — API communication

pytz — timezone handling (Dubai)

python-dotenv — environment variable management

📁 Project Structure
automation-workflow/
│
├── ipo_monitor.py
├── requirements.txt
├── .gitignore
└── .github/
    └── workflows/
        └── ipo.yml

🔐 Environment Variables

All sensitive values are stored securely using environment variables.

.env (for local testing only)
FINNHUB_API_KEY=your_finnhub_api_key

SMTP_EMAIL=yourgmail@gmail.com
SMTP_PASSWORD=your_gmail_app_password
TO_EMAIL=yourgmail@gmail.com


⚠️ .env is excluded from version control.

📦 Installation (Local Test)
pip install -r requirements.txt


Run the automation:

python ipo_monitor.py


Successful execution prints:

✅ IPO automation executed successfully.


An email notification will be delivered to the configured inbox.

⏰ Automation Schedule

The workflow runs daily via GitHub Actions:

9:00 AM Dubai time (UTC +4)


GitHub cron configuration:

0 5 * * *

📧 Sample Email Output

Subject:

Daily U.S. IPO Monitor – Same-Day IPOs Above $200M (YYYY-MM-DD)


Email Content:

• Market: United States
• IPO scope: Same-day IPOs only
• Offer threshold: USD 200 million

Qualified IPOs:
ARM — $4,870,000,000
RDDT — $748,000,000


If no IPO meets the criteria:

No same-day U.S. IPOs exceeded the USD 200 million offer threshold.

🔍 Why Finnhub API?

Finnhub was selected because it provides:

Reliable U.S. IPO calendar data

IPO price and share count in a single API

Clean JSON responses suitable for automation

Free tier for testing and evaluation

Coverage of NASDAQ and NYSE listings

🧪 Verification

The workflow can be verified by:

GitHub Actions execution logs

Manual workflow trigger (workflow_dispatch)

Email notification delivery

Screen recording of successful run

🚀 Possible Enhancements

Slack / Microsoft Teams alerts

Twilio SMS notifications

Retry and fallback market-data APIs

Database logging

Dashboard monitoring

✅ Summary

This automation demonstrates:

Reliable scheduled execution

Market-data integration

Deterministic filtering logic

Secure credential handling

Production-style automation workflow

Clear audit and verification path

Author:
Muhammed Afsal P M