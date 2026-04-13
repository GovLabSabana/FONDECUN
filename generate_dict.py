import json

data = json.load(open('analysis/taxonomia_final.json', encoding='utf-8'))
unique_items = set()
for k, v in data.items():
    for item in v:
        unique_items.add(item.strip())

descriptions = {}

def generate_desc(item):
    item_lower = item.lower()
    if "evaluaci" in item_lower or "calificaci" in item_lower:
        return f"La {item.lower()} es fundamental para medir el impacto de las estrategias implementadas. Este componente permite identificar áreas de aprendizaje, diagnosticar obstáculos y ajustar el enfoque pedagógico continuamente para favorecer el progreso del estudiante."
    elif "curr" in item_lower or "planeaci" in item_lower or "plan " in item_lower:
        return f"El aspecto de {item.lower()} estructura la hoja de ruta a seguir en el aula. Garantiza que los contenidos y metodologías estén alineados de manera coherente con los objetivos de aprendizaje de los estudiantes."
    elif "docente" in item_lower or "enseñanza" in item_lower or "pedag" in item_lower or "praxis" in item_lower:
        return f"Enfocarse en {item.lower()} potencia directamente la calidad educativa transmitida a los alumnos. Transformar y fortalecer estos procesos profesionales es clave para lograr un aprendizaje dinámico y significativo."
    elif "emocion" in item_lower or "mindfulness" in item_lower or "neuro" in item_lower or "clima" in item_lower or "estrés" in item_lower:
        return f"El trabajo enfocado en {item.lower()} mejora tangiblemente el bienestar de toda la comunidad educativa. Establece un ambiente socioemocional seguro y propicio para el desarrollo tanto cognitivo como personal."
    elif "comuni" in item_lower or "social" in item_lower or "equipo" in item_lower or "familia" in item_lower or "colaborativo" in item_lower:
        return f"Fomentar {item.lower()} crea una indispensable red de apoyo y retroalimentación alrededor de los estudiantes y maestros. A través de este tejido compartido, el aprendizaje se vuelve una experiencia mucho más enriquecedora y contextualizada."
    elif "tic" in item_lower or "tecnolog" in item_lower or "recurso" in item_lower or "herramienta" in item_lower or "conectividad" in item_lower:
        return f"La integración y optimización de {item.lower()} moderniza, facilita y diversifica los métodos de enseñanza. Abre nuevas posibilidades didácticas para conectar con los intereses actuales de los alumnos de manera interactiva."
    elif "reflexi" in item_lower or "análisis" in item_lower or "seguimiento" in item_lower or "autoevaluaci" in item_lower or "diagnóstico" in item_lower:
        return f"Llevar a cabo un proceso constante de {item.lower()} fomenta la autocrítica constructiva y la adaptación dentro de la institución. Es el paso inicial e indispensable para cualquier innovación y mejora escolar que busque ser sostenible en el tiempo."
    elif "proyecto" in item_lower or "experiencia" in item_lower or "actividades" in item_lower or "práctica" in item_lower:
        return f"Impulsar y diseñar adecuadamente {item.lower()} acerca la teoría a la práctica y al contexto vital del estudiante, haciéndola relevante. Mediante este enfoque práctico, los estudiantes desarrollan competencias transversales que van más allá del aprendizaje tradicional de aula."
    elif "liderazgo" in item_lower or "directivo" in item_lower or "gestión" in item_lower or "institucional" in item_lower:
        return f"Desarrollar capacidades en {item.lower()} permite canalizar y organizar los esfuerzos de la base docente hacia metas comunes. Es un pilar organizativo clave que provee la visión, los recursos y el tiempo necesarios para ejecutar transformaciones profundas."
    else:
        return f"El abordaje detallado de {item.lower()} representa una área central y de alto impacto para el desarrollo de la institución. Atenderla o potenciarla sistemáticamente fortalece de manera integral el marco de calidad educativa del colegio."

for item in unique_items:
    descriptions[item] = generate_desc(item)

with open('data/diccionario_cualitativo.json', 'w', encoding='utf-8') as f:
    json.dump(descriptions, f, ensure_ascii=False, indent=4)

print("Created diccionario_cualitativo.json with", len(descriptions), "items.")
