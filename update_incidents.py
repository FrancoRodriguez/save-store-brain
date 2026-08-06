import os

with open("incidents.html", "r", encoding="utf-8") as f:
    content = f.read()

metrics_html = """
            <!-- KPI & Analytics Grid -->
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 24px; margin-bottom: 32px;">
                <!-- Total Abiertas -->
                <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px;">
                    <div style="display: flex; justify-content: space-between; margin-bottom: 16px;">
                        <span style="color: var(--text-secondary); font-size: 14px; font-weight: 500;">Abiertas Hoy</span>
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#ff9500" stroke-width="2"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path><line x1="12" y1="9" x2="12" y2="13"></line><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>
                    </div>
                    <div style="font-size: 32px; font-weight: 700; color: var(--text-primary); margin-bottom: 8px;">5</div>
                    <div style="font-size: 13px; color: #34c759; display: flex; align-items: center; gap: 4px;">
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="23 6 13.5 15.5 8.5 10.5 1 18"></polyline><polyline points="17 6 23 6 23 12"></polyline></svg>
                        -12% vs semana pasada
                    </div>
                </div>

                <!-- Críticas -->
                <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px;">
                    <div style="display: flex; justify-content: space-between; margin-bottom: 16px;">
                        <span style="color: var(--text-secondary); font-size: 14px; font-weight: 500;">Severidad Crítica</span>
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#ff3b30" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
                    </div>
                    <div style="font-size: 32px; font-weight: 700; color: var(--text-primary); margin-bottom: 8px;">2</div>
                    <div style="font-size: 13px; color: #ff3b30; display: flex; align-items: center; gap: 4px;">
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="23 18 13.5 8.5 8.5 13.5 1 6"></polyline><polyline points="17 18 23 18 23 12"></polyline></svg>
                        Requiere acción inmediata
                    </div>
                </div>

                <!-- Tiempo Medio -->
                <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px;">
                    <div style="display: flex; justify-content: space-between; margin-bottom: 16px;">
                        <span style="color: var(--text-secondary); font-size: 14px; font-weight: 500;">Tiempo de Resolución</span>
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#0071e3" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
                    </div>
                    <div style="font-size: 32px; font-weight: 700; color: var(--text-primary); margin-bottom: 8px;">2.4h</div>
                    <div style="font-size: 13px; color: var(--text-secondary); display: flex; align-items: center; gap: 4px;">
                        Promedio últimos 30 días
                    </div>
                </div>

                <!-- Gráfica de Fluctuación -->
                <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px;">
                    <div style="display: flex; justify-content: space-between; margin-bottom: 12px;">
                        <span style="color: var(--text-secondary); font-size: 14px; font-weight: 500;">Tendencia (Últ. 7 días)</span>
                    </div>
                    <div style="display: flex; align-items: flex-end; justify-content: space-between; height: 40px; gap: 4px;">
                        <div style="width: 14%; background: #e5e5ea; border-radius: 4px 4px 0 0; height: 60%;" title="Lunes: 6"></div>
                        <div style="width: 14%; background: #e5e5ea; border-radius: 4px 4px 0 0; height: 80%;" title="Martes: 8"></div>
                        <div style="width: 14%; background: #e5e5ea; border-radius: 4px 4px 0 0; height: 40%;" title="Miércoles: 4"></div>
                        <div style="width: 14%; background: #ff3b30; border-radius: 4px 4px 0 0; height: 100%;" title="Jueves: 10 (Pico)"></div>
                        <div style="width: 14%; background: #e5e5ea; border-radius: 4px 4px 0 0; height: 50%;" title="Viernes: 5"></div>
                        <div style="width: 14%; background: #e5e5ea; border-radius: 4px 4px 0 0; height: 20%;" title="Sábado: 2"></div>
                        <div style="width: 14%; background: #0071e3; border-radius: 4px 4px 0 0; height: 50%;" title="Hoy: 5"></div>
                    </div>
                    <div style="display: flex; justify-content: space-between; margin-top: 8px; font-size: 11px; color: var(--text-secondary);">
                        <span>Lun</span>
                        <span>Hoy</span>
                    </div>
                </div>
            </div>
"""

target = '</header>\n\n            <div class="details-grid"'
if target in content:
    new_content = content.replace(target, '</header>\n\n' + metrics_html + '            <div class="details-grid"')
    with open("incidents.html", "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Updated incidents.html with totals and charts.")
else:
    print("Could not find insertion point in incidents.html")
