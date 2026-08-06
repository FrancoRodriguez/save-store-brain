import os
import glob

guard_script = '    <script type="module" src="auth-guard.js"></script>\n'

for file_path in glob.glob("*.html"):
    if file_path == "login.html":
        continue
        
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "auth-guard.js" not in content:
        # Insert before </head>
        content = content.replace('</head>', guard_script + '</head>')
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Added auth guard to {file_path}")
