import os
import re

with open("proposal.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace textareas with chat containers
for i in range(1, 5):
    old_textarea = f'<textarea id="comment-{i}" placeholder="Deja tu comentario aquí..." style="width: 100%; padding: 12px; border-radius: 8px; border: 1px solid var(--border-color); background: var(--bg-body); color: var(--text-primary); font-family: \'Inter\', sans-serif; resize: vertical; min-height: 60px;"></textarea>'
    new_html = f'''<div class="chat-container" data-phase="{i}">
                                    <div class="chat-messages" id="chat-messages-{i}" style="max-height: 200px; overflow-y: auto; margin-bottom: 12px; display: flex; flex-direction: column; gap: 8px;"></div>
                                    <div class="chat-input-wrapper" style="display: flex; gap: 8px;">
                                        <textarea id="comment-{i}" placeholder="Añadir nota compartida..." style="flex: 1; padding: 12px; border-radius: 8px; border: 1px solid var(--border-color); background: var(--bg-body); color: var(--text-primary); font-family: 'Inter', sans-serif; resize: vertical; min-height: 40px;"></textarea>
                                        <button class="btn-send-note" data-phase="{i}" style="background: var(--primary-color); color: white; border: none; border-radius: 8px; padding: 0 16px; font-weight: 500; cursor: pointer;">Enviar</button>
                                    </div>
                                </div>'''
    content = content.replace(old_textarea, new_html)

# Remove the localStorage script
localstorage_script = '''        // Persistencia automática de comentarios en localStorage (JSON)
        document.addEventListener("DOMContentLoaded", () => {
            const textareas = document.querySelectorAll("textarea");
            
            // Cargar datos guardados (en formato JSON)
            const savedData = JSON.parse(localStorage.getItem("saveStoreNotes") || "{}");
            
            textareas.forEach(textarea => {
                if (textarea.id && savedData[textarea.id]) {
                    textarea.value = savedData[textarea.id];
                }
                
                // Guardar automáticamente al escribir
                textarea.addEventListener("input", (e) => {
                    if (!e.target.id) return;
                    const currentData = JSON.parse(localStorage.getItem("saveStoreNotes") || "{}");
                    currentData[e.target.id] = e.target.value;
                    localStorage.setItem("saveStoreNotes", JSON.stringify(currentData));
                });
            });
        });'''

content = content.replace(localstorage_script, '// El chat ahora se maneja vía Firebase (ver chat.js)')

# Add chat.js script inclusion before closing body
if 'src="chat.js"' not in content:
    content = content.replace('</body>', '    <script type="module" src="chat.js"></script>\n</body>')

with open("proposal.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Updated proposal.html with chat containers.")
