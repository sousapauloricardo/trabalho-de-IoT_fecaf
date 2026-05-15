import pandas as pd
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from data.database import get_engine

def run_ingestion():
    engine = get_engine()
    csv_path = os.path.join('data', 'iot_telemetry_data.csv')
    
    if not os.path.exists(csv_path):
        print("Erro: Arquivo CSV não encontrado em /data")
        return

    print("Lendo e processando dados...")
    df = pd.read_csv(csv_path)
    
    if 'ts' in df.columns:
        df['ts'] = pd.to_datetime(df['ts'], unit='s')
    
    print("Enviando para o MySQL...")
    df.to_sql('temperature_readings', con=engine, if_exists='replace', index=False)
    print("Ingestão concluída!")

if __name__ == "__main__":
    run_ingestion()