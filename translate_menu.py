import os

html_files = ["index.html", "finance.html", "inventory.html", "incidents.html", "proposal.html", "stores.html"]

replacements = [
    (">Executive Summary</a>", ">Resumen Ejecutivo</a>"),
    (">Executive Summary\n", ">Resumen Ejecutivo\n"),
    (">Financial Performance</a>", ">Rendimiento Financiero</a>"),
    (">Financial Performance\n", ">Rendimiento Financiero\n"),
    (">Inventory Status</a>", ">Estado de Inventario</a>"),
    (">Inventory Status\n", ">Estado de Inventario\n"),
    (">Store Incidents</a>", ">Incidencias de Tienda</a>"),
    (">Store Incidents\n", ">Incidencias de Tienda\n"),
    (">Stores Directory</a>", ">Directorio de Tiendas</a>"),
    (">Stores Directory\n", ">Directorio de Tiendas\n"),
    (">Project Proposal</a>", ">Propuesta de Proyecto</a>"),
    (">Project Proposal\n", ">Propuesta de Proyecto\n")
]

for fpath in html_files:
    if os.path.exists(fpath):
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Replace padded text as well
        # Sometimes there's whitespace, so let's do a more robust replace using regex
        import re
        content = re.sub(r'>\s*Executive Summary\s*<', '>Resumen Ejecutivo<', content)
        content = re.sub(r'>\s*Financial Performance\s*<', '>Rendimiento Financiero<', content)
        content = re.sub(r'>\s*Inventory Status\s*<', '>Estado de Inventario<', content)
        content = re.sub(r'>\s*Store Incidents\s*<', '>Incidencias de Tienda<', content)
        content = re.sub(r'>\s*Stores Directory\s*<', '>Directorio de Tiendas<', content)
        content = re.sub(r'>\s*Project Proposal\s*<', '>Propuesta de Proyecto<', content)

        # Handle cases where the text is before the closing </a> but has spaces
        # Using a pattern to match the text before </a>
        # The above regex covers the exact match between > and <
        
        # But wait, SVG icons might be inside the <a> tag.
        # Example:
        # <a href="index.html" class="nav-item active">
        #    <svg ...></svg>
        #    Executive Summary
        # </a>
        
        content = content.replace("Executive Summary", "Resumen Ejecutivo")
        content = content.replace("Financial Performance", "Rendimiento Financiero")
        content = content.replace("Inventory Status", "Estado de Inventario")
        content = content.replace("Store Incidents", "Incidencias de Tiendas")
        content = content.replace("Stores Directory", "Directorio de Tiendas")
        content = content.replace("Project Proposal", "Propuesta de Proyecto")
        
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Translated menu in {fpath}")
