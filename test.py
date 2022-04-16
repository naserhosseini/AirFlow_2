from pathlib import Path

log_dir="C:\\Activities\\airflow2\\marketvol\\"

file_list = Path(log_dir).rglob('*.log')

for file in file_list:
    print(file)