import json

def save_json(data, filename="output.json"):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        print(f"Saved extracted data to {filename}")
    except Exception as e:
        print(f"Failed to save JSON: {e}")