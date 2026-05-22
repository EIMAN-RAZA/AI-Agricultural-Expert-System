# inference_engine.py

from knowledge_base import get_knowledge

def infer(symptom_key):
    knowledge = get_knowledge()
    if symptom_key in knowledge:
        entry = knowledge[symptom_key]
        return {
            "Diagnosis": entry["diagnosis"],
            "Treatment": entry["treatment"],
            "Explanation": f"Based on the symptom '{entry['symptom']}', the system infers '{entry['diagnosis']}' and suggests: {entry['treatment']}"
        }
    else:
        return {
            "Diagnosis": "Unknown",
            "Treatment": "Consult an agronomist",
            "Explanation": "Symptom not found in knowledge base."
        }