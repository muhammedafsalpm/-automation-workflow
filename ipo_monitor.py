import os
import requests
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
import pytz
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# ---------------- CONFIG ----------------

FINNHUB_API_KEY = os.getenv("FINNHUB_API_KEY")
SMTP_EMAIL = os.getenv("SMTP_EMAIL")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
TO_EMAIL = os.getenv("TO_EMAIL")

# Validate environment variables
if not all([FINNHUB_API_KEY, SMTP_EMAIL, SMTP_PASSWORD, TO_EMAIL]):
    raise ValueError("Missing environment variables. Check your .env file.")

# Dubai timezone
dubai_tz = pytz.timezone("Asia/Dubai")
today = datetime.now(dubai_tz).strftime("%Y-%m-%d")

# Finnhub IPO API — SAME DAY ONLY
url = (
    f"https://finnhub.io/api/v1/calendar/ipo"
    f"?from={today}&to={today}&token={FINNHUB_API_KEY}"
)

response = requests.get(url, timeout=30)
data = response.json()

qualified_ipos = []

for ipo in data.get("ipoCalendar", []):

    symbol = ipo.get("symbol")
    price = ipo.get("price")
    shares = ipo.get("numberOfShares")

    if not symbol or not price or not shares:
        continue

    offer_amount = float(price) * float(shares)

    if offer_amount >= 200_000_000:
        qualified_ipos.append(
            f"{symbol} — ${offer_amount:,.0f}"
        )

# ---------------- EMAIL ----------------

if qualified_ipos:
    ipo_text = "\n".join(qualified_ipos)
else:
    ipo_text = "No same-day U.S. IPOs exceeded the USD 200 million offer size threshold."

email_body = f"""
Hello,

This is an automated daily IPO monitoring report generated at 9:00 AM Dubai time.

Workflow Summary:
• Market: United States
• IPO scope: Same-day IPOs only (today’s IPOs)
• Filter condition: Offer amount greater than USD 200 million
• Offer amount calculation: IPO price × number of shares
• Data source: Finnhub IPO calendar
• Execution: Fully automated scheduled workflow

------------------------------------------------------------

Qualified IPOs for Today:

{ipo_text}

------------------------------------------------------------

If no IPOs meet the above criteria, this indicates that no same-day U.S. IPOs exceeded the USD 200 million offer threshold at the time of execution.

This workflow runs automatically every day and sends an updated report without manual intervention.

Regards,
Automated IPO Monitoring System
(Generated programmatically)
"""

msg = MIMEText(email_body)
msg["Subject"] = f"Daily U.S. IPO Monitor – Same-Day IPOs Above $200M ({today})"
msg["From"] = SMTP_EMAIL
msg["To"] = TO_EMAIL


with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(SMTP_EMAIL, SMTP_PASSWORD)
    server.send_message(msg)

print("✅ IPO automation executed successfully.")
