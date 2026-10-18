import json
from datetime import datetime

def save_history(type: str, query: str,result):
    try:
        with open("history.json", "r") as f:
            history = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        history = []
    
    entry = {
        "type": type,
        "query": query,
        "result": result,
        "time": datetime.now().isoformat()
    }
    history.append(entry)
    
    with open("history.json", "w") as f:
        json.dump(history, f, indent=2)

def get_history():
    try:
        with open("history.json", "r") as f:
            history = json.load(f)
        return history[-10:] if len(history) > 10 else history
    except (FileNotFoundError, json.JSONDecodeError):
        return []