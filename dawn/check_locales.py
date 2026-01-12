import json
import glob

def check_structure(file_path):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        issues = []
        strongside = data.get("strongside", {})
        
        # Check videos.list vs videoTitles
        videos = strongside.get("videos", {})
        if "videoTitles" in videos:
            issues.append("HAS_BROKEN_VIDEO_TITLES")
        if "list" not in videos:
            issues.append("MISSING_VIDEO_LIST")
            
        # Check shop.features
        shop = strongside.get("shop", {})
        if "features" not in shop:
            issues.append("MISSING_SHOP_FEATURES")
            
        # Check training cards location
        training = strongside.get("training", {})
        if "cards" not in training:
            issues.append("MISSING_TRAINING_CARDS")
            
        if issues:
            print(f"{file_path}: {', '.join(issues)}")
        else:
            print(f"{file_path}: OK")
            
    except Exception as e:
        print(f"{file_path}: ERROR {e}")

locales = ['locales/fr.json', 'locales/de.json', 'locales/es.json', 'locales/it.json', 'locales/pt-PT.json', 'locales/nl.json', 'locales/sv.json', 'locales/en.default.json']
for loc in locales:
    check_structure(loc)
