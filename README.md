# Capital Time API

## Description
This is a Flask API deployed on a GCP VM that returns the local time and UTC offset of a given capital city. Token authentication is required.

---

## Public IP of API
**URL**: `http://34.105.60.104:5000/get_time`

---

## Authorization

This API uses a simple token for security.

**Required Header**:
Authorization: uva_ticket24302

---

## How to Call the API

### Sample CURL Request:
```bash
curl -H "Authorization: uva_ticket24302" "http://34.105.60.104:5000/get_time?city=London"


# Example Output:

{
  "city": "London",
  "local_time": "2025-04-21 19:04:03",
  "utc_offset": "UTC+01:00"
}

# Errors

Invalid Token:
{
	“error”: “Unauthorized access”
}

City Not Found:

{
	“message”: “CityName not found in database”
}

# Supported Capitals

Washington
London Tokyo
Addis Ababa
Canberra
