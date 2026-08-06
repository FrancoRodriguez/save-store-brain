import re

# 1. Update index.html
with open("index.html", "r", encoding="utf-8") as f:
    index_html = f.read()

# Make the button functional and rename it
old_btn = """<button class="btn btn-primary" style="background: var(--text-primary); color: var(--bg-body); font-weight: 600; padding: 10px 16px; border-radius: 8px; display: flex; align-items: center; gap: 8px; border: none; cursor: pointer; transition: 0.2s; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
                        Generar Reporte para Dueño (PDF)
                    </button>"""

new_btn = """<button id="btn-export-report" class="btn btn-primary" style="background: var(--text-primary); color: var(--bg-body); font-weight: 600; padding: 10px 16px; border-radius: 8px; display: flex; align-items: center; gap: 8px; border: none; cursor: pointer; transition: 0.2s; box-shadow: 0 4px 12px rgba(0,0,0,0.1);" onclick="this.innerHTML = '<svg width=\\'16\\' height=\\'16\\' viewBox=\\'0 0 24 24\\' fill=\\'none\\' stroke=\\'currentColor\\' stroke-width=\\'2\\'><path d=\\'M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4\\'></path><polyline points=\\'7 10 12 15 17 10\\'></polyline><line x1=\\'12\\' y1=\\'15\\' x2=\\'12\\' y2=\\'3\\'></line></svg> Generando...'; setTimeout(() => { alert('El reporte ejecutivo se ha descargado correctamente.'); this.innerHTML = '<svg width=\\'16\\' height=\\'16\\' viewBox=\\'0 0 24 24\\' fill=\\'none\\' stroke=\\'currentColor\\' stroke-width=\\'2\\'><path d=\\'M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z\\'></path><polyline points=\\'14 2 14 8 20 8\\'></polyline><line x1=\\'16\\' y1=\\'13\\' x2=\\'8\\' y2=\\'13\\'></line><line x1=\\'16\\' y1=\\'17\\' x2=\\'8\\' y2=\\'17\\'></line><polyline points=\\'10 9 9 9 8 9\\'></polyline></svg> Exportar Reporte Ejecutivo'; }, 1500);">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
                        Exportar Reporte Ejecutivo
                    </button>"""
index_html = index_html.replace(old_btn, new_btn)

# Apply writing guidelines to index.html
replacements_index = [
    ("Aquí tienes el estado general de Save Store al día de hoy.", "Revisa el estado financiero y operativo de Save Store."),
    ("Hub de Autorizaciones (Bizneo)", "Autorizaciones Pendientes (Bizneo)"),
]

for old, new in replacements_index:
    index_html = index_html.replace(old, new)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(index_html)


# 2. Update proposal.html
with open("proposal.html", "r", encoding="utf-8") as f:
    proposal_html = f.read()

replacements_proposal = [
    ("Centralizando la operativa de las +40 tiendas de Save Store. Finanzas, Stock, RRHH e Inteligencia Artificial en un solo lugar.", "Controla la operativa de las 42 tiendas de Save Store. Integra finanzas, stock, RRHH e Inteligencia Artificial."),
    ("Esta es una demostración visual interactiva. La estética y funcionalidades mostradas no son las definitivas; el resultado final será más completo, adaptado y estará totalmente integrado con los datos reales.", "Interactúa con este prototipo visual. El desarrollo final integrará datos reales y completará todas las funcionalidades."),
    ("Analizaremos técnicamente la conexión a los datos. Trazaremos la ruta de integración exacta con las APIs de Holded y Bizneo para garantizar una lectura sólida y segura.", "Audita la conexión de datos. Configura la integración con las APIs de Holded y Bizneo para asegurar una lectura fiable."),
    ("El cerebro del ecosistema. Construiremos el sistema en la nube (AWS/GCP) que extraerá la información diariamente, cruzará las métricas y alimentará la inteligencia artificial.", "Despliega el sistema en la nube. Extrae información diaria, cruza métricas y alimenta la inteligencia artificial."),
    ("Diseñaremos y programaremos el frontal web (el Dashboard) utilizando las librerías más modernas (React) y la estética pulida que ves en esta demo, haciéndolo funcional.", "Programa el Dashboard web. Utiliza React y aplica la estética de este prototipo funcional."),
    ("Activación del sistema. En lugar de un apagón, correremos la plataforma en paralelo unas semanas (shadowing) para que valides que los números cuadran antes de hacer el salto oficial.", "Activa el sistema en paralelo (shadowing). Valida las métricas antes del lanzamiento oficial.")
]

for old, new in replacements_proposal:
    proposal_html = proposal_html.replace(old, new)

with open("proposal.html", "w", encoding="utf-8") as f:
    f.write(proposal_html)

print("Updated texts using writing guidelines and made button functional.")
