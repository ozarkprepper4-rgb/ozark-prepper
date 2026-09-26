from pathlib import Path
import subprocess
import json

def check_stripe_connected():
    result = subprocess.run(
        ["/home/destiny/video_env/bin/python3", "/home/destiny/query_vault.py", "Stripe API Key"],
        capture_output=True, text=True, timeout=10
    )
    try:
        data = json.loads(result.stdout)
        if "error" in data:
            return False, None
        return True, data.get("password")
    except Exception:
        return False, None

def run():
    connected, api_key = check_stripe_connected()
    if not connected:
        return "Stripe is not connected yet. I need Neil to add a real Stripe API key to the vault (group: Stripe and Payments, title: Stripe API Key) before I can check for real sales or report revenue."

    return "Stripe is connected. Real revenue checking against the live Stripe API is not yet built - this is the next real step once a key is added."

if __name__ == "__main__":
    print(run())
