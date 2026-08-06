import os
import glob

logout_html = '''                <a href="#" onclick="window.logout()" class="nav-item" style="color: #ef4444; margin-top: auto;">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"></path><polyline points="16 17 21 12 16 7"></polyline><line x1="21" y1="12" x2="9" y2="12"></line></svg>
                    Cerrar Sesión
                </a>'''

for file_path in glob.glob("*.html"):
    if file_path == "login.html":
        continue
        
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "Cerrar Sesión" not in content:
        # Insert before </nav>
        content = content.replace('</nav>', logout_html + '\n            </nav>')
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Added logout button to {file_path}")
