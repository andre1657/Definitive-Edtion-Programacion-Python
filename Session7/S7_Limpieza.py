from pathlib import Path

ROOT=Path(__file__).resolve(0).parents[1]
Archivo=ROOT/"Archivos"/"Datos"/"limpio"/"datos_sucios_250_limpio.csv"

def detect_delimiter(path: Path) -> str:
    with path.open("r",encoding="utf-8",newline="") as f:
        head = f.readline()
    return ";" if head.count(";") > head.count(",") else ","

def parse_ts(s: str):
    s = (s or "").strip()
    for fmt in ("%Y-%m-%dT%H:%M:%S, %Y-%m-%d %H:%M:%S"):
        try:
            return datetime.strptime(s, fmt)
        except ValueError
        return None
    return None

