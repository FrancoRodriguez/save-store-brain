import os

# 1. UPDATE PROPOSAL.HTML
with open("proposal.html", "r", encoding="utf-8") as f:
    proposal_content = f.read()

qa_section = """
            <!-- Entrevista de Diagnostico (Q&A) -->
            <div style="background: var(--bg-card); border-radius: 12px; border: 1px solid var(--border-color); padding: 24px; margin-bottom: 32px;">
                <h2 style="font-size: 18px; color: var(--text-primary); margin-bottom: 20px; display: flex; align-items: center; gap: 8px;">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="color: #0071e3;"><circle cx="12" cy="12" r="10"></circle><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"></path><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>
                    Diagnóstico Inicial (Visión CEO)
                </h2>
                
                <div style="display: flex; flex-direction: column; gap: 16px;">
                    <div style="background: rgba(0,0,0,0.02); padding: 16px; border-radius: 8px; border-left: 3px solid #0071e3;">
                        <p style="font-size: 14px; color: var(--text-secondary); font-style: italic; margin-bottom: 8px;">"¿Cuál es el mayor cuello de botella a final de mes?"</p>
                        <p style="font-size: 15px; color: var(--text-primary); font-weight: 500; margin: 0;">— "Las horas perdidas cruzando excels de Holded, el banco y nuestra plataforma para cuadrar la caja de las 42 tiendas."</p>
                    </div>
                    
                    <div style="background: rgba(0,0,0,0.02); padding: 16px; border-radius: 8px; border-left: 3px solid #ff3b30;">
                        <p style="font-size: 14px; color: var(--text-secondary); font-style: italic; margin-bottom: 8px;">"¿Qué te quita el sueño operativamente?"</p>
                        <p style="font-size: 15px; color: var(--text-primary); font-weight: 500; margin: 0;">— "Funcionamos como un enrutador humano. Todo me llega por correo. Desde incidencias de TPV hasta aprobaciones de horas extra en Bizneo."</p>
                    </div>
                    
                    <div style="background: rgba(0,0,0,0.02); padding: 16px; border-radius: 8px; border-left: 3px solid #34c759;">
                        <p style="font-size: 14px; color: var(--text-secondary); font-style: italic; margin-bottom: 8px;">"¿Qué esperas de este proyecto?"</p>
                        <p style="font-size: 15px; color: var(--text-primary); font-weight: 500; margin: 0;">— "Quiero una torre de control. Una sola pantalla donde pueda ver si gano dinero, si me voy a quedar sin stock de iPhone, y aprobar nóminas sin entrar a 4 programas distintos."</p>
                    </div>
                </div>
            </div>
"""
if "Diagnóstico Inicial" not in proposal_content:
    target = '</div>\n\n            <!-- Timeline -->'
    proposal_content = proposal_content.replace(target, '</div>\n\n' + qa_section + '            <!-- Timeline -->')
    with open("proposal.html", "w", encoding="utf-8") as f:
        f.write(proposal_content)

# 2. UPDATE INDEX.HTML (CEO Modules)
with open("index.html", "r", encoding="utf-8") as f:
    index_content = f.read()

ceo_modules = """
            <!-- CEO Modules -->
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 24px; margin-bottom: 32px;">
                <!-- Autorizaciones One-Click (Bizneo) -->
                <div style="background: var(--bg-card); border-radius: 12px; border: 1px solid var(--border-color); padding: 24px;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
                        <h3 style="font-size: 16px; color: var(--text-primary); display: flex; align-items: center; gap: 8px;">
                            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="color: #0071e3;"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
                            Hub de Autorizaciones (Bizneo)
                        </h3>
                        <span style="background: rgba(0, 113, 227, 0.1); color: #0071e3; padding: 2px 8px; border-radius: 12px; font-size: 12px; font-weight: 600;">2 Pendientes</span>
                    </div>
                    
                    <div style="display: flex; flex-direction: column; gap: 12px;">
                        <div style="border: 1px solid var(--border-color); padding: 12px; border-radius: 8px; display: flex; justify-content: space-between; align-items: center;">
                            <div>
                                <div style="font-size: 14px; font-weight: 600; color: var(--text-primary);">Avenida América</div>
                                <div style="font-size: 12px; color: var(--text-secondary);">Solicita 5h extras (Turno tarde)</div>
                            </div>
                            <button style="background: #34c759; color: white; border: none; padding: 6px 12px; border-radius: 6px; font-size: 12px; font-weight: 600; cursor: pointer;">Aprobar</button>
                        </div>
                        <div style="border: 1px solid var(--border-color); padding: 12px; border-radius: 8px; display: flex; justify-content: space-between; align-items: center;">
                            <div>
                                <div style="font-size: 14px; font-weight: 600; color: var(--text-primary);">Madrid Meridiano</div>
                                <div style="font-size: 12px; color: var(--text-secondary);">Cambio de cuadrante (Falta personal)</div>
                            </div>
                            <button style="background: #34c759; color: white; border: none; padding: 6px 12px; border-radius: 6px; font-size: 12px; font-weight: 600; cursor: pointer;">Aprobar</button>
                        </div>
                    </div>
                </div>

                <!-- Alertas de Stock Predictivas -->
                <div style="background: var(--bg-card); border-radius: 12px; border: 1px solid var(--border-color); padding: 24px;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
                        <h3 style="font-size: 16px; color: var(--text-primary); display: flex; align-items: center; gap: 8px;">
                            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="color: #ff9500;"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path><polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline><line x1="12" y1="22.08" x2="12" y2="12"></line></svg>
                            Alertas de Stock Predictivas
                        </h3>
                        <span style="background: rgba(255, 149, 0, 0.1); color: #ff9500; padding: 2px 8px; border-radius: 12px; font-size: 12px; font-weight: 600;">Crítico</span>
                    </div>
                    
                    <div style="background: rgba(255, 59, 48, 0.05); border-left: 3px solid #ff3b30; padding: 12px; border-radius: 4px; margin-bottom: 12px;">
                        <div style="font-size: 14px; font-weight: 600; color: var(--text-primary); margin-bottom: 4px;">iPhone 15 Pro Max (256GB)</div>
                        <div style="font-size: 13px; color: var(--text-secondary);">Rotura estimada en <strong>4 días</strong> en 3 tiendas (Burn rate: 5 uds/día).</div>
                        <button style="margin-top: 8px; font-size: 12px; color: #ff3b30; background: transparent; border: 1px solid #ff3b30; border-radius: 4px; padding: 4px 8px; cursor: pointer; font-weight: 600;">Emitir orden de compra a Ingram</button>
                    </div>

                    <div style="background: rgba(255, 149, 0, 0.05); border-left: 3px solid #ff9500; padding: 12px; border-radius: 4px;">
                        <div style="font-size: 14px; font-weight: 600; color: var(--text-primary); margin-bottom: 4px;">AirPods Pro (2nd Gen)</div>
                        <div style="font-size: 13px; color: var(--text-secondary);">Stock mínimo alcanzado en <strong>Las Arenas</strong>.</div>
                    </div>
                </div>
            </div>
"""

if "CEO Modules" not in index_content:
    # Insert right after the KPI grid and before the map container
    target = '<!-- Map Container -->'
    index_content = index_content.replace(target, ceo_modules + '\n            ' + target)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(index_content)

print("Updated proposal.html and index.html")
