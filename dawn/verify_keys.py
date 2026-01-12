import json
import sys

def get_keys(obj, prefix=""):
    keys = set()
    if isinstance(obj, dict):
        for k, v in obj.items():
            full_key = f"{prefix}.{k}" if prefix else k
            keys.add(full_key)
            keys.update(get_keys(v, full_key))
    return keys

def compare_locales(file1, file2):
    try:
        with open(file1, 'r') as f1:
            data1 = json.load(f1)
        with open(file2, 'r') as f2:
            data2 = json.load(f2)

        # Focus only on strongside section
        strongside1 = data1.get("strongside", {})
        strongside2 = data2.get("strongside", {})

        keys1 = get_keys(strongside1, "strongside")
        keys2 = get_keys(strongside2, "strongside")

        missing_in_target = keys1 - keys2
        
        print(f"Total keys in EN strongside: {len(keys1)}")
        print(f"Total keys in TARGET strongside: {len(keys2)}")

        if missing_in_target:
            print("\n❌ MISSING Keys in TARGET (present in EN):")
            for k in sorted(missing_in_target):
                print(f"  - {k}")
        
        if not missing_in_target:
            print("\n✅ structure matches! No keys missing.")

    except Exception as e:
        print(f"Error: {e}")

compare_locales('locales/en.default.json', 'locales/de.json')
