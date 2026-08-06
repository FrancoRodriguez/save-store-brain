import os
import glob

nav_item = '''                <a href="stores.html" class="nav-item">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
                    Stores Directory
                </a>
'''

html_files = ["index.html", "finance.html", "inventory.html", "incidents.html", "proposal.html"]

for fpath in html_files:
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "stores.html" not in content:
        # Insert before proposal.html nav item
        target = '<a href="proposal.html" class="nav-item">'
        if target in content:
            content = content.replace(target, nav_item + "                " + target)
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Updated {fpath}")

