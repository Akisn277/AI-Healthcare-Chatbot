from astar_diagnosis import a_star_search, graph, heuristics

def get_bot_response(message):
    message = message.lower()
    keywords = ["fever", "headache", "cough", "cold", "fatigue"]
    symptoms = [word for word in message.split() if word in keywords]

    if not symptoms:
        return "Please enter symptoms like fever, cough, headache, etc."

    for goal in ["flu", "covid", "cold"]:
        path = a_star_search("start", goal, graph, heuristics)
        if path and all(symptom in path for symptom in symptoms):
            return f"Based on symptoms, you may have {goal.capitalize()}. Path: {' -> '.join(path)}"

    return "I'm not sure about the diagnosis. Please consult a doctor."
