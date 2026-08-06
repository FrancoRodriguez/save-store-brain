import re

with open("stores.html", "r", encoding="utf-8") as f:
    content = f.read()

# Fix active menu items
content = content.replace('<a href="finance.html" class="nav-item active">', '<a href="finance.html" class="nav-item">')
content = content.replace('<a href="stores.html" class="nav-item">', '<a href="stores.html" class="nav-item active">')

# Add stores.js
if 'stores.js' not in content:
    content = content.replace('</head>', '    <script type="module" src="stores.js"></script>\n</head>')

# Replace everything inside <main class="main-content"> ... </main>
main_start = content.find('<main class="main-content">') + len('<main class="main-content">')
main_end = content.find('</main>')

new_main_content = """
            <header class="top-header">
                <div class="greeting">
                    <h1>Directorio de Tiendas</h1>
                    <p>Estado detallado y control de métricas por sucursal en tiempo real.</p>
                </div>
            </header>

            <div style="background: var(--bg-card); border-radius: 12px; border: 1px solid var(--border-color); overflow: hidden; display: flex; flex-direction: column;">
                <!-- Toolbar -->
                <div style="padding: 16px; border-bottom: 1px solid var(--border-color); display: flex; justify-content: space-between; align-items: center; gap: 16px;">
                    <div style="flex: 1; max-width: 400px; position: relative;">
                        <input type="text" id="search-store" placeholder="Buscar por ciudad, tipo o nombre..." style="width: 100%; padding: 10px 16px 10px 40px; border-radius: 8px; border: 1px solid var(--border-color); background: var(--bg-body); color: var(--text-primary); font-family: 'Inter', sans-serif;">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="position: absolute; left: 12px; top: 50%; transform: translateY(-50%); color: var(--text-secondary);"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                    </div>
                    <div style="display: flex; gap: 12px; font-size: 13px;">
                        <span style="color: var(--text-secondary);">Total Tiendas: <strong id="total-stores" style="color: var(--text-primary);">0</strong></span>
                    </div>
                </div>
                
                <!-- Table -->
                <div style="overflow-x: auto;">
                    <table style="width: 100%; border-collapse: collapse; text-align: left; font-size: 14px;">
                        <thead>
                            <tr style="background: rgba(0,0,0,0.02); border-bottom: 1px solid var(--border-color);">
                                <th style="padding: 12px 16px; color: var(--text-secondary); font-weight: 500;">Estado</th>
                                <th style="padding: 12px 16px; color: var(--text-secondary); font-weight: 500;">Tienda</th>
                                <th style="padding: 12px 16px; color: var(--text-secondary); font-weight: 500;">Ciudad (Tipo)</th>
                                <th style="padding: 12px 16px; color: var(--text-secondary); font-weight: 500;">Ingresos Hoy</th>
                                <th style="padding: 12px 16px; color: var(--text-secondary); font-weight: 500;">Inventario</th>
                                <th style="padding: 12px 16px; color: var(--text-secondary); font-weight: 500;">Incidencias</th>
                            </tr>
                        </thead>
                        <tbody id="stores-tbody">
                            <tr><td colspan="6" style="padding: 24px; text-align: center; color: var(--text-secondary);">Cargando directorio...</td></tr>
                        </tbody>
                    </table>
                </div>
            </div>
"""

content = content[:main_start] + new_main_content + content[main_end:]

with open("stores.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Created stores.html")
