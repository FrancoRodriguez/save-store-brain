# Save Store Brain 🧠

![Save Store Brain Prototype](https://short-ends-trade.loca.lt/favicon.ico) <!-- Placeholder para futuro banner -->

Este repositorio contiene la **maqueta interactiva y propuesta comercial** inicial del sistema de gestión "Save Store Brain". Ha sido diseñado como un prototipo de alta fidelidad para presentar al cliente la visión, el retorno de inversión (ROI) y la interfaz de usuario del futuro panel de control (Dashboard).

## 🚀 Objetivo del Proyecto (Fase 1: Prototipo)

1. **Propuesta de Valor:** Justificar la inversión mediante el cálculo de ahorro en horas y eliminación de errores humanos.
2. **Navegación Visual:** Mostrar al cliente cómo será la experiencia de usuario (UX/UI) utilizando un diseño moderno, limpio y con una estética premium basada en directrices de diseño "Apple-like" (Glassmorphism, transiciones suaves, interfaces oscuras/claras dinámicas).
3. **Módulo de IA Integrado:** Presentar el concepto del "Motor Invisible" o LLM integrado para el cruce de datos inteligente.

## 🛠️ Tecnologías Utilizadas

Por el momento, el proyecto es completamente *estático* para facilitar despliegues rápidos de demostración (como en Railway, Vercel o Surge):

- **HTML5:** Estructura semántica.
- **Vanilla CSS3:** Variables (Custom Properties), Flexbox, CSS Grid y micro-interacciones (hover, view transitions, backdrop-filter).
- **JavaScript (Vanilla):** Scripts auxiliares y sincronización de menús (`sync_menu.py` utilizado como herramienta interna de desarrollo para inyectar componentes estáticos).

## 📁 Estructura del Proyecto

- `proposal.html`: La carta de presentación comercial, el desglose de precios y el análisis de ROI.
- `index.html`: Dashboard principal (visión general).
- `finance.html`: Módulo de Finanzas.
- `inventory.html`: Módulo de Inventario.
- `incidents.html`: Módulo de Incidencias.
- `styles.css` / `styles-proposal.css`: Sistemas de diseño y tokens visuales.

## 🏃 Cómo ejecutar en local

Dado que es un proyecto de frontend estático, no requiere instalación de dependencias pesadas.

Puedes usar Python:
```bash
# Iniciar servidor local
python3 -m http.server 8000
# Abrir en el navegador: http://localhost:8000
```

O si prefieres Node.js:
```bash
npx serve .
```

## 🌐 Despliegue

Este repositorio está preparado para integrarse de forma automática con plataformas como **Railway**, **Vercel** o **Surge** mediante un flujo de CI/CD continuo conectado a la rama `master`.
