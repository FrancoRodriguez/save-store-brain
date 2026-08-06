import os
import re

with open("proposal.html", "r", encoding="utf-8") as f:
    content = f.read()

# Define the new Q&A HTML
qa_section_new = """
            <!-- Entrevista de Diagnostico (Q&A) -->
            <div style="background: var(--bg-card); border-radius: 12px; border: 1px solid var(--border-color); padding: 24px; margin-bottom: 32px;">
                <h2 style="font-size: 18px; color: var(--text-primary); margin-bottom: 20px; display: flex; align-items: center; gap: 8px;">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="color: #0071e3;"><circle cx="12" cy="12" r="10"></circle><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"></path><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>
                    Diagnóstico Inicial (Visión CEO)
                </h2>
                
                <div style="display: flex; flex-direction: column; gap: 16px;">
                    
                    <div style="background: rgba(0,0,0,0.02); padding: 16px; border-radius: 8px; border-left: 3px solid #ff3b30;">
                        <p style="font-size: 14px; color: var(--text-secondary); font-style: italic; margin-bottom: 12px; font-weight: 500;">1. ¿En qué tareas operativas sientes que pierdes más tiempo cada semana y que no deberían depender de ti?</p>
                        <div style="font-size: 14px; color: var(--text-primary); margin: 0; line-height: 1.6;">
                            <ul style="padding-left: 20px; margin: 0;">
                                <li>Armar el cierre de mes cruzando el ERP contable, la plataforma de stock/ventas y el banco a mano en Excel para tener una sola foto financiera.</li>
                                <li>Armar reportes para el dueño del grupo desde cero cada mes.</li>
                                <li>Resolver por mail cadenas larguísimas de incidencias de tienda (reclamos, horas extra de nómina, temas de facturación) que deberían resolverse un nivel más abajo sin llegar a mí.</li>
                                <li>Seguimiento manual de pagos comprometidos con proveedores.</li>
                            </ul>
                        </div>
                    </div>
                    
                    <div style="background: rgba(0,0,0,0.02); padding: 16px; border-radius: 8px; border-left: 3px solid #ff9500;">
                        <p style="font-size: 14px; color: var(--text-secondary); font-style: italic; margin-bottom: 8px; font-weight: 500;">2. Cuando necesitas saber cómo va el negocio hoy, ¿a cuántas aplicaciones o personas tienes que consultar para tener la foto completa?</p>
                        <p style="font-size: 14px; color: var(--text-primary); margin: 0; line-height: 1.6;">"Para tener la foto completa hoy tengo que meterme en al menos 4 sistemas (ERP contable, plataforma de stock/ventas, banco, un BI parcial) más un Excel que arma todo a mano, y consultar a 2-3 personas de finanzas/operaciones. No hay una vista única."</p>
                    </div>
                    
                    <div style="background: rgba(0,0,0,0.02); padding: 16px; border-radius: 8px; border-left: 3px solid #34c759;">
                        <p style="font-size: 14px; color: var(--text-secondary); font-style: italic; margin-bottom: 8px; font-weight: 500;">3. ¿Qué datos te gustaría tener en tu teléfono cada mañana mientras tomas el café? (Esta pregunta define el Dashboard).</p>
                        <p style="font-size: 14px; color: var(--text-primary); margin: 0; line-height: 1.6;">"Lo que quiero cada mañana con el café: caja disponible actualizada, quema mensual real (burn rate), próximos pagos comprometidos a 30-60-90 días, venta del día/semana vs objetivo, e incidencias abiertas por tienda."</p>
                    </div>

                    <div style="background: rgba(0,0,0,0.02); padding: 16px; border-radius: 8px; border-left: 3px solid #8e8e93;">
                        <p style="font-size: 14px; color: var(--text-secondary); font-style: italic; margin-bottom: 12px; font-weight: 500;">4. ¿Puedes hacerme una lista de todas las aplicaciones principales que usan hoy?</p>
                        <div style="font-size: 14px; color: var(--text-primary); margin: 0; line-height: 1.6;">
                            <ul style="padding-left: 20px; margin: 0;">
                                <li>ERP contable (en proceso de salida/reemplazo a Holded)</li>
                                <li>Plataforma de gestión propia de stock y ventas del grupo</li>
                                <li>Software de RRHH/nómina Bizneo</li>
                                <li>Un BI para reporting parcial</li>
                                <li>Excel como capa de consolidación manual (cierre de mes, modelo financiero, seguimiento de proveedores)</li>
                                <li>Mail como canal principal de coordinación operativa (no hay chat/ticketing unificado)</li>
                                <li>En evaluación: un ERP nuevo más liviano, más un par de herramientas de gastos/POS</li>
                            </ul>
                        </div>
                    </div>

                    <div style="background: rgba(0,0,0,0.02); padding: 16px; border-radius: 8px; border-left: 3px solid #ff3b30;">
                        <p style="font-size: 14px; color: var(--text-secondary); font-style: italic; margin-bottom: 8px; font-weight: 500;">5. ¿Cuántas veces un empleado tiene que copiar un dato de una aplicación y pegarlo manualmente en otra?</p>
                        <p style="font-size: 14px; color: var(--text-primary); margin: 0; line-height: 1.6;">"Copy-paste manual pasa seguido: horas extra reportadas por mail por un empleado de tienda que después se cargan a mano en la nómina del mes siguiente; el cierre de mes completo se arma exportando de 3 sistemas distintos y pegando todo a mano en Excel; incidencias de facturación que se resuelven por hilos de mail en vez de por flujo de sistema."</p>
                    </div>

                    <div style="background: rgba(0,0,0,0.02); padding: 16px; border-radius: 8px; border-left: 3px solid #ff9500;">
                        <p style="font-size: 14px; color: var(--text-secondary); font-style: italic; margin-bottom: 8px; font-weight: 500;">6. ¿Dónde está la "verdad absoluta" de la empresa? ¿Es un Excel, es el sistema de facturación, o está dispersa?</p>
                        <p style="font-size: 14px; color: var(--text-primary); margin: 0; line-height: 1.6;">"La verdad está dispersa, no hay una sola fuente. El ERP contable tiene lo contable, la plataforma propia tiene ventas/stock, el banco tiene el movimiento real de caja, y todo se reconcilia a mano una vez al mes en Excel. Además, en la red de franquicias hay al menos un caso de un sistema paralelo no integrado con el nuestro, ese ya es un tema aparte que estamos resolviendo por otro lado."</p>
                    </div>
                </div>
            </div>
"""

# Extract everything before Q&A and everything from Timeline onwards
start_str = "<!-- Entrevista de Diagnostico (Q&A) -->"
end_str = "<!-- Timeline -->"

start_idx = content.find(start_str)
end_idx = content.find(end_str)

if start_idx != -1 and end_idx != -1:
    new_content = content[:start_idx] + qa_section_new + "            " + content[end_idx:]
    with open("proposal.html", "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Updated proposal.html with Rodrigo's real Q&A")
else:
    print("Could not find insertion points")
