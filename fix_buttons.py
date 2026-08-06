import os

with open("proposal.html", "r", encoding="utf-8") as f:
    content = f.read()

# Remove the old "Guardar Nota" buttons
import re
content = re.sub(r'<button onclick="submitComment\(\d+\)" class="btn-secondary"[^>]*>Guardar Nota</button>\s*', '', content)

# Fix the "Enviar" button styling
# Current style: "background: var(--primary-color); color: white; border: none; border-radius: 8px; padding: 0 16px; font-weight: 500; cursor: pointer;"
content = content.replace(
    'background: var(--primary-color); color: white; border: none; border-radius: 8px; padding: 0 16px; font-weight: 500; cursor: pointer;',
    'background: #3b82f6; color: white; border: none; border-radius: 8px; padding: 0 16px; font-weight: 600; cursor: pointer; display: flex; align-items: center; justify-content: center;'
)

with open("proposal.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Removed old buttons and fixed Enviar styling.")
