#limpiar _csv_simple.py
#objetivo: leer csv "Sucio",limpiar datos y guardar "Limpio"
#timestamp en formato ISO YYYY-MM-DDTHH:MM:SS
#value como float con punto y 3 decimales
#separador de salida: coma
# files invalidos: se saltan
import csv
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[0] # Ir a la carpeta padre
TXT = ROOT /"Archivos"
IN_FILE = TXT / "voltajes_250_sucio.csv"
OUT_FILE = TXT / "voltajes_250_limpio.csv"
#Apertura de archivos
with open(IN_FILE, 'r', encoding="utf-8", newline="" ) as fin,\
       open(OUT_FILE, 'w', encoding='utf-8', newline="") as fout:
       reader = csv.DictReader(fin, delimiter=';')
       writer = csv.DictWriter(fout, fieldnames=["timestamp", "value"])
       writer.writeheader()
#Leer linea por lineal y selecionar en crudo raw
       total = kept = 0
       for row in reader:
              total += 1
              ts_raw =(row.get("timestamp") or "").strip()
              val_raw =(row.get("value") or "").strip()
#limpiar datos
              val_raw = val_raw.replace(",",".")
              val_low = val_raw.lower()
              if val_low in ("", "na", "n/a", "nan", "null", "none", "error"):
                     continue
              try:
                     val = float(val_raw)
              except ValueError:
                     continue
                   #limpieza de datos de tiempo
              ts_clean = None
              for fmt in ("%Y-%m-%d %H:%M:%S", "%d-%m-%Y %H:%M:%S"):
                     try:
                           dt = datetime.strptime(ts_raw[:19], fmt)
                           ts_clean = dt.strftime("%Y-%m-%dT%H:%M:%S")
                           break
                     except ValueError:
                              pass
              if ts_clean is None and "T" in ts_raw and len(ts_raw) >= 19:
                           try:
                               dt = datetime.strptime(ts_raw[:19], "%Y-%m-%dT%H:%M:%S")
                               ts_clean = dt.strftime("%Y-%m-%dT%H:%M:%S")
                           except ValueError:
                               ts_clean = None
              if ts_clean is None:
                                   continue
                         #grabar datos en writer
              writer.writerow({"timestamp": ts_clean, "value": f"{val:-.3f}"})
              kept += 1
                       
                                 
                           
                   


              




