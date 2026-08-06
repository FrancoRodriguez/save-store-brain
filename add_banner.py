import os
import glob

banner_html = """
            <div style="background-color: rgba(59, 130, 246, 0.1); border-left: 4px solid #3b82f6; padding: 12px 16px; margin-bottom: 24px; border-radius: 8px; display: flex; align-items: flex-start; gap: 12px;">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#3b82f6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink: 0; margin-top: 2px;"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
                <div style="color: var(--text-secondary); font-size: 14px; line-height: 1.5;">
                    <strong style="color: var(--text-primary);">Nota sobre el Prototipo:</strong> Esta es una demostración visual interactiva. La estética y funcionalidades mostradas no son las definitivas; el resultado final será más completo, adaptado y estará totalmente integrado con los datos reales.
                </div>
            </div>
"""

for file_path in glob.glob("*.html"):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "Nota sobre el Prototipo" not in content:
        content = content.replace('<main class="main-content">', '<main class="main-content">\n' + banner_html)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Added banner to {file_path}")
