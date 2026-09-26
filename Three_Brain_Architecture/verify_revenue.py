import json
import os

print("--- REVENUE VERIFICATION CHECK ---")
stripe_file = "Logs/stripe_balance.json"

if os.path.exists(stripe_file):
    with open(stripe_file, 'r') as f:
        data = json.load(f)
    print(f"Verified Balance: ${data.get('balance', 0.00)}")
    print(f"Last Transaction: {data.get('last_transaction', 'None')}")
else:
    print("WARNING: No live Stripe connection log found. Current verified balance: $0.00")
