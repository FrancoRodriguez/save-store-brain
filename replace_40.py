import re

with open('/Users/franco.rodriguez/.gemini/antigravity/scratch/rodrigo-dashboard/proposal.html', 'r') as f:
    content = f.read()

# Replace 40 tiendas with +40 tiendas
content = content.replace('40 tiendas', '+40 tiendas')
content = content.replace('40 cierres', '+40 cierres')

# Update the AI module list item
old_ai_item = '<li><span class="check-icon">✓</span> Módulo Integrado de Consultor IA (Chatbot)</li>'
new_ai_item = '<li><span class="check-icon">✓</span> Módulo de Consultor IA <strong style="color: #28a745; font-size: 13px; margin-left: 4px;">(Bonificado - Habitualmente 3.000€)</strong></li>'
content = content.replace(old_ai_item, new_ai_item)

with open('/Users/franco.rodriguez/.gemini/antigravity/scratch/rodrigo-dashboard/proposal.html', 'w') as f:
    f.write(content)
