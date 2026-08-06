import os

files = ['index.html', 'finance.html', 'inventory.html', 'incidents.html', 'proposal.html']
directory = '/Users/franco.rodriguez/.gemini/antigravity/scratch/rodrigo-dashboard'

replacements = {
    'href="finanzas.html"': 'href="finance.html"',
    'Finanzas (Holded)': 'Finance (Holded)',
    'href="inventario.html"': 'href="inventory.html"',
    'Inventario & Ventas': 'Inventory & Sales',
    'href="incidencias.html"': 'href="incidents.html"',
    'Incidencias Tiendas': 'Store Incidents',
    'href="propuesta.html"': 'href="proposal.html"',
    'Propuesta': 'Proposal',
    'Resumen Ejecutivo': 'Executive Summary'
}

for filename in files:
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r') as file:
        content = file.read()
        
    for old, new in replacements.items():
        content = content.replace(old, new)
        
    with open(filepath, 'w') as file:
        file.write(content)

print("Replacements done.")
