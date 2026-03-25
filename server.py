from flask import Flask, request
from main import place_order
import os

app = Flask(__name__)

last_signal = None

@app.route('/webhook', methods=['POST'])
def webhook():
    global last_signal

    # 👇 Accept EVERYTHING (fixes 415)
    data = request.data.decode("utf-8")

    print("\n🔥 ALERT RECEIVED 🔥")
    print("RAW DATA:", data)

    # 👇 Detect signal
    if "BUY" in data.upper():
        signal = "BUY"
    elif "SELL" in data.upper():
        signal = "SELL"
    else:
        print("❌ Signal not found")
        return "ok"

    # جلوگیری duplicate
    if signal == last_signal:
        print("⚠️ Duplicate signal ignored")
        return "ok"

    last_signal = signal

    place_order(signal)

    return "ok"



if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

