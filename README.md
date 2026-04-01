# 📊 DataPromce — Dashboard de Análisis Institucional FONDECUN

**DataPromce** es una plataforma interactiva de análisis y seguimiento diseñada para visualizar el impacto, avance y desafíos del programa **FONDECUN** en las instituciones educativas del departamento de Cundinamarca. 

Este dashboard consolida datos de participación en las 6 etapas del programa, integrando análisis cuantitativo (indicadores de avance) y cualitativo (logros, retos y sugerencias procesados con IA).

---

## 🚀 Funcionalidades Principales

### 1. Visualización Geográfica e Interactiva
*   **Mapa de Calor (Leaflet):** Localización exacta de cada IED con marcadores inteligentes que cambian de color según la etapa máxima alcanzada por la institución.
*   **Diagrama Sankey:** Visualización del flujo de las instituciones a través de las diferentes etapas, permitiendo identificar puntos críticos de deserción o avance masivo.

### 2. Sistema Avanzado de Filtros (Sticky Bar)
Ubucado siempre en la parte superior para facilitar la exploración de datos:
*   **Filtros Multiselección:** Permite filtrar por Zona (Urbana/Rural), Nivel (Preescolar a Media), Jornada y Carácter de la institución. Incluye funcionalidad de "Seleccionar Todo" y "Deseleccionar Todo".
*   **Control de Participantes (Slider):** Ajuste del rango de instituciones según el número de participantes activos.
*   **Buscador Inteligente:** Filtro rápido por nombre de institución o código DANE.

### 3. Perfil Institucional Detallado (Sidebar)
Al seleccionar una institución, se despliega un panel lateral con información profunda:
*   **Línea de Tiempo Operativa:** Visualización clara de las etapas completadas con insignias de color (Verde: Completado, Amarillo: En proceso, Rojo: No iniciado).
*   **Indicadores Cuantitativos:** Desglose de cumplimiento por cada criterio de evaluación en cada etapa.
*   **Análisis Cualitativo de IA:** 
    *   **Categorización Top 5:** Listado de los 5 logros, retos y sugerencias más relevantes de la institución, normalizados mediante procesamiento de lenguaje natural.
    *   **Descripción Detallada:** Sección colapsable que permite leer los relatos originales de los docentes y directivos de forma organizada.

### 4. Análisis Agregado de Calidad
En el panel principal, se presentan tarjetas de resumen cualitativo que agrupan los hallazgos de todas las instituciones seleccionadas:
*   **Top 25 Insights:** Listado interactivo de los 25 temas más recurrentes en logros, retos y sugerencias.
*   **Interfaz con Scroll:** Diseño optimizado para manejar grandes volúmenes de etiquetas sin saturar la vista.

### 5. Herramientas de Reporte y Exportación
*   **Exportar a Excel:** Descarga inmediata de la tabla de datos filtrada.
*   **Informe PDF Institucional:** Generación de un reporte PDF profesional con el perfil completo de la institución seleccionada, ideal para entrega a directivos.
*   **Imprimir Todo:** Opción para generar un documento PDF que consolida los perfiles de todas las instituciones que cumplen con los filtros actuales.

---

## 🛠️ Tecnologías Utilizadas

*   **Frontend:** HTML5, CSS3 (Vanilla), Alpine.js (Gestión de estado y reactividad).
*   **Mapas:** Leaflet.js con capas de OpenStreetMap.
*   **Gráficos:** Google Charts Service (Sankey Diagram).
*   **Análisis de Datos:** Python 3 + Pandas (Procesamiento de archivos Excel fuente).
*   **Inteligencia Artificial:** OpenAI GPT-4o-mini (Normalización y categorización de textos cualitativos).

---

## 📁 Estructura del Repositorio

```text
FONDECUN/
├── index.html                   # Aplicación principal (Single Page Application)
├── styles.css                   # Hoja de estilos personalizada
├── analisis_cualitativo.py      # Script de IA para categorizar logros y retos
├── merge_data.py                # Script de consolidación de datos Excel a JSON
├── data/                        # Contenedor de datos fuente
│   └── data_merged.json         # Base de datos principal consumida por el dashboard
├── analysis/                    # Resultados del procesamiento de IA
│   ├── analisis_cualitativo_normalizado.csv
│   └── taxonomia_final.json
└── assets/                      # Recursos gráficos y logotipos
```

---

## ⚙️ Guía de Uso del Desarrollador

### Preparación de Datos
Para actualizar la información del dashboard desde los archivos Excel de seguimiento:
1. Instalar dependencias: `pip install pandas openai tqdm`.
2. Consolidar datos base: `python merge_data.py`.
3. (Opcional) Ejecutar análisis cualitativo: `python analisis_cualitativo.py`. 
   *Requiere configurar la variable de entorno `OPENAI_API_KEY`.*

### Ejecución Local
Debido a políticas de seguridad del navegador (CORS), el archivo JSON debe cargarse mediante un servidor.
```bash
# Iniciar servidor simple con Python
python -m http.server 8000
```
Luego, acceder a `http://localhost:8000`.

---

## 📄 Créditos y Licencia
Desarrollado para el fortalecimiento de la educación en el departamento de Cundinamarca. 
Proyecto impulsado bajo el marco del programa **FONDECUN**.
