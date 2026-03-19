# FONDECUN — Dashboard de Seguimiento Institucional

Dashboard web interactivo para el seguimiento de instituciones educativas del departamento de Cundinamarca en el marco del programa **FONDECUN**. Permite visualizar el avance de cada institución a través de las 6 etapas del programa de formación docente.

---

## 🗺️ Funcionalidades

- **Mapa interactivo** con marcadores por institución, coloreados según la etapa máxima alcanzada.
- **Diagrama Sankey** del flujo de participación entre etapas.
- **Tabla buscable y paginada** con avances por etapa de cada IED.
- **Panel de perfil detallado** por institución: datos generales, línea de tiempo de etapas, indicadores cuantitativos y cualitativos (logros, retos, sugerencias).

---

## 📁 Estructura del proyecto

```
FONDECUN/
├── index.html                        # Aplicación web principal
├── styles.css                        # Estilos del dashboard
├── merge_data.py                     # Script para generar data_merged.json
├── data_merged.json                  # Datos consolidados (generado)
├── sedes_educativas_cundinamarca.geojson  # Geodatos de sedes educativas
├── diccionario_variables.docx        # Diccionario de variables del dataset
├── especificacion_dashboard.docx     # Especificación funcional del dashboard
├── Descripción del proceso.pdf       # Descripción del proceso FONDECUN
├── Semáforo por etapa/               # Archivos fuente de datos por etapa (xlsx)
│   ├── Información_general_fixed.xlsx
│   ├── Semáforo Etapa 1.xlsx ... Semáforo Etapa 6.xlsx
└── Guía por etapa/                   # Guías pedagógicas en PDF
    ├── Guia Etapa 1.pdf ... Guias Etapa 6.pdf
```

---

## ⚙️ Uso

### 1. Preparar los datos

Asegúrese de tener Python 3 con las librerías necesarias:

```bash
pip install pandas openpyxl numpy
```

Luego ejecute el script de consolidación:

```bash
python merge_data.py
```

Esto genera el archivo `data_merged.json` con la información de todas las instituciones.

### 2. Servir la aplicación

El dashboard es una aplicación web estática. Para verla localmente, use un servidor HTTP simple:

```bash
# Con Python
python -m http.server 8000
```

Luego abra `http://localhost:8000` en su navegador.

> **Nota:** El archivo `index.html` no puede abrirse directamente con doble clic (por restricciones de CORS al cargar el JSON). Debe servirse a través de un servidor local.

---

## 🧰 Tecnologías

| Tecnología | Uso |
|---|---|
| [Leaflet.js](https://leafletjs.com/) | Mapa interactivo |
| [Google Charts (Sankey)](https://developers.google.com/chart/interactive/docs/gallery/sankey) | Diagrama de flujo |
| [Alpine.js](https://alpinejs.dev/) | Reactividad del dashboard |
| Python + Pandas | Procesamiento y consolidación de datos |

---

## 📌 Dependencias externas (CDN)

- Leaflet CSS/JS `1.9.4`
- Alpine.js `3.x`
- Google Charts Loader

---

## 📄 Licencia

Proyecto desarrollado para uso interno en el marco del programa FONDECUN — Cundinamarca.
