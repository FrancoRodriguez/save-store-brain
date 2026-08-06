import os

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update the Export Button
old_btn = """<button class="btn btn-secondary">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
                        Exportar Resumen
                    </button>"""
new_btn = """<button class="btn btn-primary" style="background: var(--text-primary); color: var(--bg-body); font-weight: 600; padding: 10px 16px; border-radius: 8px; display: flex; align-items: center; gap: 8px; border: none; cursor: pointer; transition: 0.2s; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
                        Generar Reporte para Dueño (PDF)
                    </button>"""
content = content.replace(old_btn, new_btn)


# 2. Add Conciliacion KPI
conciliacion_kpi = """
                <!-- Conciliacion Automatica -->
                <div class="metric-card glass" style="border: 1px solid rgba(52, 199, 89, 0.3);">
                    <div class="metric-header">
                        <span class="metric-title">Conciliación Holded ↔ Banco</span>
                        <div class="icon-box green">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
                        </div>
                    </div>
                    <div class="metric-value">99.2%</div>
                    <div class="metric-trend positive" style="display: flex; justify-content: space-between; align-items: center; width: 100%;">
                        <span>Automático</span>
                        <a href="#" style="color: #ff9500; font-size: 11px; text-decoration: underline; background: rgba(255, 149, 0, 0.1); padding: 2px 6px; border-radius: 4px;">4 por revisar</a>
                    </div>
                </div>
"""

# Find the end of the metrics-grid (before <!-- Detailed Sections -->)
target = '</div>\n\n            <!-- Detailed Sections -->'
if conciliacion_kpi not in content:
    content = content.replace(target, conciliacion_kpi + target)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Updated index.html with the ultimate CEO features.")
