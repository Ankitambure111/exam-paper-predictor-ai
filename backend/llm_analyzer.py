import json

def analyze_exam_questions(questions_list):
    # This "fakes" the AI response so you can test your FastAPI
    print("LOG: Using Mock AI because API is busy...")
    
    mock_data = {
        "common_topics": ["Renewable Energy", "Solar Cells", "Wind Turbines"],
        "important_topics": ["Photovoltaic Effect", "Betz Law"],
        "predicted_questions": [
            "Explain the working of a Single Basin Tidal Power Plant.",
            "Compare Horizontal and Vertical axis wind turbines."
        ]
    }
    return json.dumps(mock_data)