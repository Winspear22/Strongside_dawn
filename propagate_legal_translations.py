import json
import os
import glob

# Paths
locales_dir = 'dawn/locales'
en_file_path = os.path.join(locales_dir, 'en.default.json')

# Load English translations source
with open(en_file_path, 'r', encoding='utf-8') as f:
    en_data = json.load(f)

# Extract the legal_pages block
legal_pages_block = en_data['strongside'].get('legal_pages')

if not legal_pages_block:
    print("Error: Could not find strongside.legal_pages in en.default.json")
    exit(1)

# Iterate over all other JSON files
json_files = glob.glob(os.path.join(locales_dir, '*.json'))

for file_path in json_files:
    filename = os.path.basename(file_path)
    
    # Skip French and English files
    if filename in ['fr.json', 'en.default.json', 'en.json']:
        continue
    
    # Skip schema files
    if 'schema' in filename:
        continue

    print(f"Processing {filename}...")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Ensure 'strongside' key exists
        if 'strongside' not in data:
            data['strongside'] = {}
        
        # Inject or overwrite legal_pages with English content
        data['strongside']['legal_pages'] = legal_pages_block
        
        # Save back
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
    except Exception as e:
        print(f"Failed to process {filename}: {e}")

print("Done! All locales now have English legal pages.")
