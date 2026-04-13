"""
calculate_metrics.py
====================
Calcula para cada colegio en data_merged.json:

  1. pct_avance_global   → promedio de TODOS los criterios numéricos de todas las etapas.
  2. eje_transformacion  → promedio de los criterios cuyo 'tipo' == "Nivel de transformación de las prácticas docentes"
  3. eje_descenso        → promedio de los criterios cuyo 'tipo' contiene "descenso curricular"

Los criterios y su mapeo a ejes transversales provienen del criteriosDictionary 
definido en index.html:

  criterio{n}_{etapa} en el diccionario  →  criterios.e{etapa}.criterio_{n}  en el JSON

Criterios con tipo vacío ("") se usan en el promedio global pero NO en ningún eje.
criterio1_1 es texto (modelo pedagógico) → siempre excluido de promedios numéricos.
"""

import json
import os

# ── Mapeo de ejes ──────────────────────────────────────────────────────────────
# Formato: (etapa_key, criterio_key): 'eje_label'
# Derivado directamente del criteriosDictionary del index.html

EJE_TRANSFORMACION = "transformacion_practicas"
EJE_DESCENSO = "descenso_curricular"

CRITERIO_EJE = {
    # E1
    ("e1", "criterio_2"): EJE_DESCENSO,
    ("e1", "criterio_3"): EJE_TRANSFORMACION,
    # E2
    ("e2", "criterio_1"): EJE_DESCENSO,
    # criterio_2 e2 → tipo vacío → sin eje
    ("e2", "criterio_3"): EJE_TRANSFORMACION,
    # E3
    # criterio_1 e3 → tipo vacío → sin eje
    ("e3", "criterio_2"): EJE_TRANSFORMACION,
    # E4
    ("e4", "criterio_1"): EJE_TRANSFORMACION,
    # criterio_2 e4 → tipo vacío → sin eje
    ("e4", "criterio_3"): EJE_DESCENSO,
    # E5
    ("e5", "criterio_1"): EJE_DESCENSO,
    ("e5", "criterio_2"): EJE_DESCENSO,
    ("e5", "criterio_3"): EJE_TRANSFORMACION,
    # E6
    ("e6", "criterio_1"): EJE_TRANSFORMACION,
    ("e6", "criterio_2"): EJE_DESCENSO,
    ("e6", "criterio_3"): EJE_DESCENSO,
}

# Criterio que es siempre texto (no numérico)
TEXT_CRITERIOS = {("e1", "criterio_1")}


def calcular_metricas(inst):
    """Dada una institución, calcula y retorna el dict de métricas."""
    criterios = inst.get("criterios", {})

    all_vals = []
    trans_vals = []
    desc_vals = []

    for etapa_key in ["e1", "e2", "e3", "e4", "e5", "e6"]:
        for crit_key, cval in (criterios.get(etapa_key) or {}).items():
            # Ignorar valores texto o None
            if (etapa_key, crit_key) in TEXT_CRITERIOS:
                continue
            if not isinstance(cval, (int, float)):
                continue
            if cval != cval:  # isnan check
                continue

            all_vals.append(cval)

            eje = CRITERIO_EJE.get((etapa_key, crit_key))
            if eje == EJE_TRANSFORMACION:
                trans_vals.append(cval)
            elif eje == EJE_DESCENSO:
                desc_vals.append(cval)

    def safe_avg(lst):
        return round(sum(lst) / len(lst), 4) if lst else None

    return {
        "pct_avance_global": safe_avg(all_vals),
        "eje_transformacion_practicas": safe_avg(trans_vals),
        "eje_descenso_curricular": safe_avg(desc_vals),
    }


def main():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(root_dir, "data", "data_merged.json")

    print(f"Leyendo {data_path} ...")
    with open(data_path, encoding="utf-8") as f:
        data = json.load(f)

    updated = 0
    skipped = 0
    for inst in data:
        metricas = calcular_metricas(inst)
        # Sólo agregar si hay al menos un valor calculado
        if any(v is not None for v in metricas.values()):
            inst["metricas"] = metricas
            updated += 1
        else:
            inst["metricas"] = metricas  # guarda Nones por consistencia
            skipped += 1

    # Ejemplo de salida
    sample = next((d for d in data if d.get("metricas", {}).get("pct_avance_global") is not None), None)
    if sample:
        print(f"\nEjemplo -> {sample.get('nombre_oficial') or sample.get('institucion')}")
        for k, v in sample["metricas"].items():
            label = {
                "pct_avance_global": "% Avance Global",
                "eje_transformacion_practicas": "Eje Transformación Prácticas",
                "eje_descenso_curricular": "Eje Descenso Curricular",
            }.get(k, k)
            pct = f"{round(v*100,1)}%" if v is not None else "N/D"
            print(f"  {label}: {pct}")

    print(f"\nInstituciones con métricas calculadas: {updated}")
    print(f"Instituciones sin datos numéricos:      {skipped}")

    with open(data_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\nOK: data_merged.json actualizado correctamente.")


if __name__ == "__main__":
    main()
