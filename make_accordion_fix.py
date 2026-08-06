import re

with open("proposal.html", "r", encoding="utf-8") as f:
    content = f.read()

# We need to find each timeline-item block.
# Let's use re.sub with a custom function to process each timeline-item block.
# The pattern will match the whole timeline-item block up to its closing </div>.
# Since it's nested, regex is tricky. Let's do it manually by finding `<!-- Fase ` and `<!-- Implementación -->` as delimiters.

blocks = [
    "<!-- Fase 1 -->",
    "<!-- Fase 2 -->",
    "<!-- Fase 3 -->",
    "<!-- Fase 4 -->",
    "<!-- Implementación -->",
    "</div>\n            </div>\n        </main>" # End of timeline
]

for i in range(len(blocks)-1):
    start_marker = blocks[i]
    end_marker = blocks[i+1]
    
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker, start_idx)
    
    block_str = content[start_idx:end_idx]
    
    # 1. Replace <div class="timeline-item"> with <div class="timeline-item" style="margin-bottom: 16px;">
    block_str = block_str.replace('<div class="timeline-item">', '<div class="timeline-item" style="margin-bottom: 16px;">', 1)
    
    # 2. Extract Title from timeline-meta
    meta_match = re.search(r'<div class="timeline-meta">(.*?)</div>', block_str)
    if not meta_match:
        continue
    title = meta_match.group(1)
    
    new_header = f"""
    <div class="timeline-header" style="cursor: pointer; display: flex; justify-content: space-between; align-items: center; background: var(--bg-card); padding: 16px; border-radius: 8px; border: 1px solid var(--border-color);" onclick="const content = this.nextElementSibling; const arrow = this.querySelector('.arrow'); if(content.style.display === 'none') {{ content.style.display = 'block'; arrow.innerHTML = '▲'; }} else {{ content.style.display = 'none'; arrow.innerHTML = '▼'; }}">
        <div class="timeline-meta" style="margin:0;">{title}</div>
        <div class="arrow" style="color: var(--text-secondary); font-size: 12px;">▼</div>
    </div>
    <div class="timeline-content-wrapper" style="display: none; padding: 16px 0 24px 0;">"""
    
    block_str = block_str.replace(f'<div class="timeline-meta">{title}</div>', new_header, 1)
    
    # 3. Add closing </div> right before the last </div> of this block
    # The block ends with "            </div>\n\n                "
    # We find the last "</div>" and insert another "</div>" before it.
    last_div_idx = block_str.rfind('</div>')
    if last_div_idx != -1:
        block_str = block_str[:last_div_idx] + '</div>\n' + block_str[last_div_idx:]
        
    content = content[:start_idx] + block_str + content[end_idx:]

with open("proposal.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Fixed accordions")
