import json
import random

# Lista de ubicaciones aproximadas en España
cities = [
    {"city": "Madrid", "base_lat": 40.4168, "base_lng": -3.7038, "count": 10},
    {"city": "Barcelona", "base_lat": 41.3851, "base_lng": 2.1734, "count": 6},
    {"city": "Zaragoza", "base_lat": 41.6488, "base_lng": -0.8891, "count": 3},
    {"city": "Málaga", "base_lat": 36.7213, "base_lng": -4.4214, "count": 3},
    {"city": "Sevilla", "base_lat": 37.3891, "base_lng": -5.9845, "count": 3},
    {"city": "Las Palmas", "base_lat": 28.1235, "base_lng": -15.4363, "count": 2},
    {"city": "Tenerife", "base_lat": 28.4636, "base_lng": -16.2518, "count": 2},
    {"city": "Alicante", "base_lat": 38.3452, "base_lng": -0.4810, "count": 2},
    {"city": "San Sebastián", "base_lat": 43.3183, "base_lng": -1.9812, "count": 2},
    {"city": "Vigo", "base_lat": 42.2406, "base_lng": -8.7207, "count": 2},
    {"city": "Valencia", "base_lat": 39.4699, "base_lng": -0.3763, "count": 4},
    {"city": "Bilbao", "base_lat": 43.2630, "base_lng": -2.9350, "count": 3}
]

types = ["El Corte Inglés", "Carrefour", "Centro Comercial", "Street"]
street_names = ["Goya", "Castellana", "Callao", "Fuencarral", "Sanchinarro", "Princesa", "Meridiano", "Mesa y López"]

stores = []
store_id = 1

for city_data in cities:
    for i in range(city_data["count"]):
        t = random.choice(types)
        
        if t == "Street":
            name = f"Save Store {city_data['city']} Centro"
        else:
            suffix = random.choice(street_names)
            name = f"Save Store {t} {city_data['city']} {suffix}"
            
        lat = city_data["base_lat"] + random.uniform(-0.05, 0.05)
        lng = city_data["base_lng"] + random.uniform(-0.05, 0.05)
        
        stock_status = random.randint(65, 100)
        incidents = 0
        if random.random() < 0.2:
            incidents = random.randint(1, 3)
            
        daily_revenue = random.randint(500, 3000)
        
        stores.append({
            "id": f"store_{store_id:03d}",
            "name": name,
            "city": city_data["city"],
            "type": t,
            "lat": round(lat, 6),
            "lng": round(lng, 6),
            "stockStatus": stock_status,
            "activeIncidents": incidents,
            "dailyRevenue": daily_revenue
        })
        store_id += 1

with open("stores.json", "w", encoding="utf-8") as f:
    json.dump(stores, f, indent=4, ensure_ascii=False)
    
print(f"Generated {len(stores)} stores.")
