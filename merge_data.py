import pandas as pd
import os
import json
import numpy as np

def clean_val(v):
    if pd.isna(v) or v is None:
        return None
    if isinstance(v, (np.integer, int)):
        return int(v)
    if isinstance(v, (np.floating, float)):
        f = float(v)
        return None if np.isnan(f) else round(f, 4)
    return str(v).strip()


def row_to_dict(row):
    return {k: clean_val(v) for k, v in row.to_dict().items() if not str(k).startswith('Unnamed')}


def merge_data():
    base_path = 'Semáforo por etapa'
    info_gen_path = os.path.join(base_path, 'Información_general_fixed.xlsx')

    df_info = pd.read_excel(info_gen_path)
    print("INFO COLS:", df_info.columns.tolist())

    master_data = {}
    for _, row in df_info.iterrows():
        d_raw = row.get('id')
        if pd.isna(d_raw):
            continue
        dane = str(int(d_raw))

        master_data[dane] = {
            "id": dane,
            "municipio": clean_val(row.get('municipio')),
            "estado": clean_val(row.get('estado')),
            "institucion": clean_val(row.get('institucion')),
            "lat": clean_val(row.get('latitud')),
            "lng": clean_val(row.get('longitud')),
            "mp": clean_val(row.get('mp')),
            "jornada": clean_val(row.get('jornada')),
            "caracter": clean_val(row.get('caracter')),
            "rector": clean_val(row.get('rector')),
            "especialidad": clean_val(row.get('especialidad')),
            "foco_e2": clean_val(row.get('foco_e2')),
            "participantes": {
                "e1": clean_val(row.get('participantes_e1')),
                "e2": clean_val(row.get('participantes_e2')),
                "e3": clean_val(row.get('participantes_e3')),
                "e4": clean_val(row.get('participantes_e4')),
                "e5": clean_val(row.get('participantes_e5')),
                "e6": clean_val(row.get('participantes_e6')),
            },
            "avances": {
                "e1": clean_val(row.get('avance_e1')),
                "e2": clean_val(row.get('avance_e2')),
                "e3": clean_val(row.get('avance_e3')),
                "e4": clean_val(row.get('avance_e4')),
                "e5": clean_val(row.get('avance_e5')),
                "e6": clean_val(row.get('avance_e6')),
            },
            "etapas_cursadas": {
                "e1": int(row.get('e1', 0)) if pd.notnull(row.get('e1', 0)) else 0,
                "e2": int(row.get('e2', 0)) if pd.notnull(row.get('e2', 0)) else 0,
                "e3": int(row.get('e3', 0)) if pd.notnull(row.get('e3', 0)) else 0,
                "e4": int(row.get('e4', 0)) if pd.notnull(row.get('e4', 0)) else 0,
                "e5": int(row.get('e5', 0)) if pd.notnull(row.get('e5', 0)) else 0,
                "e6": int(row.get('e6', 0)) if pd.notnull(row.get('e6', 0)) else 0,
            },
            "detalles": {}
        }

    # Add stage-specific detail
    semaforo_files = {
        "e1": ("Semáforo Etapa 1.xlsx", "id"),
        "e2": ("Semáforo Etapa 2.xlsx", "id"),
        "e3": ("Semáforo Etapa 3.xlsx", "id"),
        "e4": ("Semáforo Etapa 4.xlsx", "id3"),
        "e5": ("Semáforo Etapa 5.xlsx", "id3"),
        "e6": ("Semáforo Etapa 6.xlsx", "codigo"),
    }

    for key, (file, id_col) in semaforo_files.items():
        filepath = os.path.join(base_path, file)
        if not os.path.exists(filepath):
            continue
        try:
            df = pd.read_excel(filepath)
            # drop unnamed cols
            df = df[[c for c in df.columns if not str(c).startswith('Unnamed')]]

            if id_col not in df.columns:
                # Try 'id' fallback
                alts = [c for c in df.columns if 'id' in c.lower() or 'codigo' in c.lower()]
                if alts:
                    id_col = alts[0]
                else:
                    print(f"  ! No ID column found in {file}")
                    continue

            print(f"  Processing {file} with id_col={id_col}, cols={df.columns.tolist()[:8]}")

            for dane, group in df.groupby(df[id_col].apply(lambda x: str(int(x)) if pd.notnull(x) else None)):
                if dane and dane in master_data:
                    # aggregate: take first row but merge text fields
                    agg = {}
                    for col in group.columns:
                        if col == id_col:
                            continue
                        vals = [v for v in group[col].tolist() if pd.notnull(v) and str(v).strip()]
                        if not vals:
                            agg[col] = None
                        elif all(isinstance(v, (int, float, np.integer, np.floating)) for v in vals):
                            agg[col] = round(float(np.nanmean(vals)), 4)
                        else:
                            agg[col] = ' / '.join(str(v).strip() for v in vals[:3])
                    master_data[dane]["detalles"][key] = agg

        except Exception as e:
            print(f"Error processing {file}: {e}")

    output_path = 'data_merged.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(list(master_data.values()), f, ensure_ascii=False, indent=2)

    print(f"\nMerged data for {len(master_data)} institutions into {output_path}")


if __name__ == "__main__":
    merge_data()
