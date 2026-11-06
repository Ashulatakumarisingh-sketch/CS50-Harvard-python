import sys
import requests

def main():
    # 1. चेक करें कि यूजर ने कमांड-लाइन आर्गुमेंट दिया है या नहीं
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")

    # 2. चेक करें कि दिया गया आर्गुमेंट एक वैलिड नंबर (Float) है या नहीं
    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    # 3. CoinCap का v2 एंडपॉइंट (यह बिना किसी API Key के सीधे इंटरनेट पर लाइव काम करता है)
    url = "https://api.coincap.io/v2/assets/bitcoin"

    try:
        # बिना किसी एक्स्ट्रा नाम पैरामीटर के रिक्वेस्ट भेजें
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # v2 JSON स्ट्रक्चर से डॉलर प्राइस निकालें
        rate_float = float(data["data"]["priceUsd"])

    except (requests.RequestException, KeyError, ValueError):
        sys.exit("Error fetching Bitcoin price data")

    # 4. टोटल कॉस्ट कैलकुलेट करें
    total_cost = bitcoins * rate_float

    # 5. फॉर्मेट के साथ आउटपुट प्रिंट करें (चार डेसिमल प्लेस और कॉमा सेपरेटर)
    print(f"${total_cost:,.4f}")

if __name__ == "__main__":
    main()
