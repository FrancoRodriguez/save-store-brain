import os
import glob

css = """
/* Global Loader */
#global-loader {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background-color: var(--bg-body);
    z-index: 99999;
    display: flex;
    justify-content: center;
    align-items: center;
    transition: opacity 0.5s ease-out, visibility 0.5s ease-out;
}

#global-loader.hidden {
    opacity: 0;
    visibility: hidden;
}

.loader-logo {
    width: 180px;
    animation: pulse 1.5s infinite ease-in-out;
}

@keyframes pulse {
    0% { transform: scale(0.95); opacity: 0.7; }
    50% { transform: scale(1.05); opacity: 1; }
    100% { transform: scale(0.95); opacity: 0.7; }
}
"""

with open("styles.css", "a", encoding="utf-8") as f:
    f.write(css)

loader_html = """
    <!-- Global Loader -->
    <div id="global-loader">
        <img src="https://savestore.es/wp-content/uploads/2022/04/logo-save.svg" alt="Save Store Logo" class="loader-logo">
    </div>
"""

loader_js = """
    <script>
        window.addEventListener('load', function() {
            setTimeout(function() {
                const loader = document.getElementById('global-loader');
                if(loader) {
                    loader.classList.add('hidden');
                }
            }, 800); // 800ms minimum display time for the cool pulse effect
        });
    </script>
"""

html_files = glob.glob("*.html")

for file in html_files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # inject HTML after <body>
    if "<body" in content and 'id="global-loader"' not in content:
        # Find the end of the body tag (e.g. <body> or <body class="...">)
        body_end = content.find('>', content.find('<body')) + 1
        content = content[:body_end] + loader_html + content[body_end:]
    
    # inject JS before </body>
    if "</body>" in content and "global-loader" in loader_js and "global-loader" not in content.split("</body>")[0][-500:]:
        # Simple check, let's just replace </body>
        content = content.replace("</body>", loader_js + "\n</body>")
        
    with open(file, "w", encoding="utf-8") as f:
        f.write(content)

print("Injected global loader into all HTML files.")
