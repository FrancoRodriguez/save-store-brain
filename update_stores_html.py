import os

with open("stores.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add pagination container after the table
pagination_html = """
                <!-- Pagination Controls -->
                <div id="pagination-controls" style="padding: 16px; border-top: 1px solid var(--border-color); display: flex; justify-content: space-between; align-items: center; background: rgba(0,0,0,0.01);">
                    <div style="font-size: 13px; color: var(--text-secondary);" id="pagination-info">Mostrando 0-0 de 0</div>
                    <div style="display: flex; gap: 8px;">
                        <button id="btn-prev" style="padding: 6px 12px; border-radius: 6px; border: 1px solid var(--border-color); background: var(--bg-body); color: var(--text-primary); cursor: pointer; font-size: 13px; font-weight: 500;" disabled>Anterior</button>
                        <button id="btn-next" style="padding: 6px 12px; border-radius: 6px; border: 1px solid var(--border-color); background: var(--bg-body); color: var(--text-primary); cursor: pointer; font-size: 13px; font-weight: 500;" disabled>Siguiente</button>
                    </div>
                </div>
"""
content = content.replace('</table>\n                </div>\n            </div>', '</table>\n                </div>' + pagination_html + '\n            </div>')

# 2. Add slide-over panel just before closing </body>
slide_over_html = """
    <!-- Slide-over panel -->
    <div id="slide-over-backdrop" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.4); backdrop-filter: blur(4px); z-index: 9998; opacity: 0; visibility: hidden; transition: 0.3s;"></div>
    <div id="slide-over-panel" style="position: fixed; top: 0; right: -100%; width: 100%; max-width: 400px; height: 100%; background: var(--bg-card); z-index: 9999; box-shadow: -5px 0 25px rgba(0,0,0,0.1); transition: 0.3s cubic-bezier(0.4, 0, 0.2, 1); display: flex; flex-direction: column; border-left: 1px solid var(--border-color);">
        <div style="padding: 24px; border-bottom: 1px solid var(--border-color); display: flex; justify-content: space-between; align-items: center;">
            <h2 id="slide-store-name" style="margin: 0; font-size: 20px; color: var(--text-primary);">Nombre de Tienda</h2>
            <button id="btn-close-panel" style="background: transparent; border: none; font-size: 24px; color: var(--text-secondary); cursor: pointer;">&times;</button>
        </div>
        <div style="padding: 24px; flex: 1; overflow-y: auto;">
            <div style="margin-bottom: 24px;">
                <span id="slide-store-id" style="font-size: 13px; color: var(--text-secondary); font-family: monospace; background: rgba(0,0,0,0.05); padding: 4px 8px; border-radius: 4px;">#ID</span>
                <span id="slide-store-city" style="font-size: 13px; color: var(--text-secondary); margin-left: 8px;">Ciudad (Tipo)</span>
            </div>
            
            <div style="background: rgba(0,0,0,0.02); border: 1px solid var(--border-color); padding: 16px; border-radius: 8px; margin-bottom: 16px;">
                <div style="font-size: 13px; color: var(--text-secondary); margin-bottom: 4px;">Manager Responsable</div>
                <div id="slide-store-manager" style="font-size: 15px; color: var(--text-primary); font-weight: 500;">Cargando...</div>
            </div>

            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 24px;">
                <div style="background: rgba(59, 130, 246, 0.05); border: 1px solid rgba(59, 130, 246, 0.2); padding: 16px; border-radius: 8px;">
                    <div style="font-size: 12px; color: #3b82f6; font-weight: 600; text-transform: uppercase;">Ingresos Hoy</div>
                    <div id="slide-store-revenue" style="font-size: 24px; color: var(--text-primary); font-weight: 700; margin-top: 8px;">$0</div>
                </div>
                <div style="background: rgba(16, 185, 129, 0.05); border: 1px solid rgba(16, 185, 129, 0.2); padding: 16px; border-radius: 8px;" id="slide-inv-box">
                    <div style="font-size: 12px; color: #10b981; font-weight: 600; text-transform: uppercase;">Salud Inventario</div>
                    <div id="slide-store-inventory" style="font-size: 24px; color: var(--text-primary); font-weight: 700; margin-top: 8px;">0%</div>
                </div>
            </div>

            <div style="background: var(--bg-body); border: 1px solid var(--border-color); padding: 16px; border-radius: 8px; margin-bottom: 24px;">
                <div style="font-size: 14px; color: var(--text-primary); font-weight: 600; margin-bottom: 12px; display: flex; justify-content: space-between;">
                    <span>Incidencias Activas</span>
                    <span id="slide-store-incidents-badge" style="background: #ef4444; color: white; padding: 2px 8px; border-radius: 12px; font-size: 12px;">0</span>
                </div>
                <div id="slide-store-incidents-list" style="font-size: 13px; color: var(--text-secondary); line-height: 1.5;">
                    Cargando historial de incidencias...
                </div>
            </div>
            
            <div style="text-align: center;">
                <button style="background: var(--text-primary); color: var(--bg-body); border: none; padding: 12px 24px; border-radius: 8px; font-weight: 600; cursor: pointer; width: 100%;">
                    Ver Reporte Completo Holded
                </button>
            </div>
        </div>
    </div>
"""

content = content.replace('</body>', slide_over_html + '\n</body>')

with open("stores.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Updated stores.html with pagination and slide-over")
