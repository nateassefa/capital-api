from flask import Flask, request, jsonify
from datetime import datetime
import pytz

app = Flask(__name__)

AUTHORIZED_TOKEN = "uva_ticket24302" 

capital_timezones = {
    "Washington": "America/New_York",
    "London": "Europe/London",
    "Tokyo": "Asia/Tokyo",
    "Addis Ababa": "Africa/Addis_Ababa",
    "Canberra": "Australia/Sydney"
}

@app.route('/get_time', methods=['GET'])
def get_time():
    token = request.headers.get("Authorization")
    if token != AUTHORIZED_TOKEN:
        return jsonify({"error": "Unauthorized access"}), 401

    city = request.args.get("city")
    if city not in capital_timezones:
        return jsonify({"message": f"{city} not found in database"}), 404

    tz = pytz.timezone(capital_timezones[city])
    now = datetime.now(tz)
    utc_offset = now.strftime('%z')
    offset_formatted = f"UTC{utc_offset[:3]}:{utc_offset[3:]}"
    return jsonify({
        "city": city,
        "local_time": now.strftime("%Y-%m-%d %H:%M:%S"),
        "utc_offset": offset_formatted
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
