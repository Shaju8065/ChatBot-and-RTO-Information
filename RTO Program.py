import http.client

conn = http.client.HTTPSConnection("rto-vehicle-details.p.rapidapi.com")

payload = "{\r\n    \"vehicleId\": \"mh27by8065\"\r\n}"

headers = {
    'content-type': "application/json",
    'Content-Type': "application/json",
    'X-RapidAPI-Key': "da3214be91msh0d3551e429c1789p1b0e30jsn10fd373d19a1",
    'X-RapidAPI-Host': "rto-vehicle-details.p.rapidapi.com"
}

conn.request("POST", "/", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))