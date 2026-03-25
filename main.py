
from delta_rest_client import DeltaRestClient, OrderType

# 🔐 Your API setup
import os

delta_client = DeltaRestClient(
    base_url='https://cdn-ind.testnet.deltaex.org',
    api_key=os.environ.get("DELTA_API_KEY"),
    api_secret=os.environ.get("DELTA_API_SECRET")
)
# Track current position (simple memory)
current_position = None  # can be "BUY", "SELL", or None


def place_order(signal):
    global current_position

    print(f"\n⚡ Processing Signal: {signal}")

    # ------------------ BUY LOGIC ------------------
    if signal == "BUY":
        if current_position == "SELL":
            print("Closing SELL position...")
            delta_client.place_order(
                product_id=84,
                size=1,
                side='buy',
                order_type=OrderType.MARKET
            )

        print("Placing BUY order...")
        delta_client.place_order(
            product_id=84,
            size=1,
            side='buy',
            order_type=OrderType.MARKET
        )

        current_position = "BUY"

    # ------------------ SELL LOGIC ------------------
    elif signal == "SELL":
        if current_position == "BUY":
            print("Closing BUY position...")
            delta_client.place_order(
                product_id=84,
                size=1,
                side='sell',
                order_type=OrderType.MARKET
            )

        print("Placing SELL order...")
        delta_client.place_order(
            product_id=84,
            size=1,
            side='sell',
            order_type=OrderType.MARKET
        )

        current_position = "SELL"

    else:
        print("Unknown signal")