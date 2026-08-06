import os
import re

with open("proposal.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace <div class="timeline-item">\n <div class="timeline-meta">TEXT</div>\n <div class="timeline-content">
# with the accordion structure

def accordion_replacer(match):
    meta_text = match.group(1)
    # Return the new wrapper. We need to wrap the rest of the content, but since timeline-item closes later,
    # we can just wrap timeline-content. Wait, timeline-item contains timeline-meta and timeline-content.
    # If we just change the opening tags and put the closing tag at the end of timeline-content...
    # Actually, it's easier to just do string manipulation.
    return f'''
    <div class="timeline-header" style="cursor: pointer; display: flex; justify-content: space-between; align-items: center; background: var(--bg-card); padding: 16px; border-radius: 8px; border: 1px solid var(--border-color); margin-bottom: 8px;" onclick="const content = this.nextElementSibling; const arrow = this.querySelector('.arrow'); if(content.style.display === 'none') {{ content.style.display = 'block'; arrow.innerHTML = '▲'; }} else {{ content.style.display = 'none'; arrow.innerHTML = '▼'; }}">
        <div class="timeline-meta" style="margin:0;">{meta_text}</div>
        <div class="arrow" style="color: var(--text-secondary); font-size: 12px;">▼</div>
    </div>
    <div class="timeline-content-wrapper" style="display: none; padding: 16px 0 24px 0;">
        <div class="timeline-content">
'''

# The pattern looks for:
# <div class="timeline-item">
#     <div class="timeline-meta">Fase 1 (Semanas 1-3)</div>
#     <div class="timeline-content">

pattern = re.compile(r'<div class="timeline-meta">([^<]+)</div>\s*<div class="timeline-content">')
content = pattern.sub(accordion_replacer, content)

# Now we need to close the `<div class="timeline-content-wrapper">` right before the closing `</div>` of `timeline-item`.
# This is tricky with regex. Let's do it by finding `<!-- Fase X -->` and doing block replacement.

content = content.replace('</div>\n\n                <!-- Fase 2 -->', '</div>\n    </div>\n</div>\n\n                <!-- Fase 2 -->')
content = content.replace('</div>\n\n                <!-- Fase 3 -->', '</div>\n    </div>\n</div>\n\n                <!-- Fase 3 -->')
content = content.replace('</div>\n\n                <!-- Fase 4 -->', '</div>\n    </div>\n</div>\n\n                <!-- Fase 4 -->')
content = content.replace('</div>\n\n                <!-- Implementación -->', '</div>\n    </div>\n</div>\n\n                <!-- Implementación -->')

# Save it back
with open("proposal.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Added accordions to proposal.html")
