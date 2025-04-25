import json
import os


def save_json(data, filename="output.json"):
    """
    Saves the provided data to a JSON file.

    :param data: The data to be serialized and saved.
    :param filename: The name of the file where data will be saved.
    """
    try:
        # Ensure the directory exists
        os.makedirs(os.path.dirname(filename), exist_ok=True)
    except FileNotFoundError:
        # If no directory is specified in filename, os.path.dirname returns an empty string
        pass
    except Exception as e:
        print(f"Failed to create directory for {filename}: {e}")
        return

    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Saved extracted data to {filename}")
    except Exception as e:
        print(f"Failed to save JSON to {filename}: {e}")
