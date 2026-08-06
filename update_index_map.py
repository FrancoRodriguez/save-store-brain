import os

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add Leaflet CSS/JS and seed/map scripts
leaflet_tags = '''
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=" crossorigin=""/>
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=" crossorigin=""></script>
    <script type="module" src="seed.js"></script>
    <script type="module" src="map.js"></script>
</head>
'''
if "leaflet.css" not in content:
    content = content.replace("</head>", leaflet_tags)

# 2. Add Seeder button to header actions
seeder_btn = '''
                    <button id="btn-seed" onclick="window.seedStores()" style="background: #10b981; color: white; border: none; padding: 6px 12px; border-radius: 6px; cursor: pointer; font-size: 13px; font-weight: 600; margin-right: 8px;">Migrar a Firebase</button>
                    <div class="date-badge">
'''
if "btn-seed" not in content:
    content = content.replace('<div class="date-badge">', seeder_btn)

# 3. Add Map Container below the metrics grid
map_html = '''
            <div style="margin-top: 24px; background: var(--bg-card); border-radius: 12px; border: 1px solid var(--border-color); overflow: hidden;">
                <div style="padding: 16px; border-bottom: 1px solid var(--border-color); display: flex; justify-content: space-between; align-items: center;">
                    <h3 style="margin: 0; font-size: 16px; color: var(--text-primary);">Mapa de Sucursales (Cerebro)</h3>
                    <div style="font-size: 12px; color: var(--text-secondary);">Leído en tiempo real desde Firebase</div>
                </div>
                <div id="map" style="width: 100%; height: 500px; background: #e5e7eb; z-index: 1;"></div>
            </div>
'''
if 'id="map"' not in content:
    content = content.replace('</div>\n\n            <!-- Two Column Layout -->', '</div>\n' + map_html + '\n            <!-- Two Column Layout -->')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Updated index.html for map and seeding.")
