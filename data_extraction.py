import os
import yaml
import pandas as pd

yaml_root = "C:/Users/Digital Suppliers/Desktop/Stock_analysis_project/YAML_data"
csv_output_folder = "C:/Users/Digital Suppliers/Desktop/Stock_analysis_project/csv_data"

os.makedirs(csv_output_folder, exist_ok=True)
symbol_data = {}

def load_yaml_data(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

# Recursively walk through all subfolders to find YAML files
for root, dirs, files in os.walk(yaml_root):
    for file in files:
        if file.endswith('.yaml'):
            file_path = os.path.join(root, file)
            print(f"Reading: {file_path}")
            data = load_yaml_data(file_path)

            if data:
                date = file.split('.')[0]  # Extract date from filename

                for entry in data:
                    symbol = entry.get('Ticker')
                    if not symbol:
                        continue

                    entry['symbol'] = symbol
                    entry['date'] = date

                    if symbol not in symbol_data:
                        symbol_data[symbol] = []

                    symbol_data[symbol].append(entry)

# Save each stock’s data as a separate CSV
if symbol_data:
    print("Saving CSV files...")
    for symbol, records in symbol_data.items():
        df = pd.DataFrame(records)
        df.sort_values('date', inplace=True)
        df.to_csv(os.path.join(csv_output_folder, f"{symbol}.csv"), index=False)
        print(f"Saved: {symbol}.csv")
else:
    print("No valid stock data collected. CSVs will not be saved.")

print("DONE! All CSVs are saved in the output folder.")






