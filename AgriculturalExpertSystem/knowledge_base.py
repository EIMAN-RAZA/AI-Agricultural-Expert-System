# knowledge_base.py

knowledge = {
    "yellow_spots": {
        "symptom": "Yellow spots on leaves",
        "diagnosis": "Fungal infection",
        "treatment": "Apply antifungal spray weekly"
    },
    "soil_ph_low": {
        "symptom": "Soil pH < 6",
        "diagnosis": "Acidic soil",
        "treatment": "Add agricultural lime to raise pH"
    },
    "holes_in_leaves": {
        "symptom": "Holes in leaves",
        "diagnosis": "Insect/pest attack",
        "treatment": "Use neem oil or organic pesticide"
    },
    "wilting_leaves": {
        "symptom": "Leaves are wilting despite watering",
        "diagnosis": "Root rot or fungal wilt",
        "treatment": "Improve soil drainage and treat with fungicide"
    },
    "white_powder": {
        "symptom": "White powder on leaf surface",
        "diagnosis": "Powdery mildew",
        "treatment": "Apply sulfur-based fungicide"
    },
    "brown_leaf_edges": {
        "symptom": "Brown edges on leaves",
        "diagnosis": "Potassium deficiency",
        "treatment": "Apply potassium-rich fertilizer"
    }
}

def get_knowledge():
    return knowledge