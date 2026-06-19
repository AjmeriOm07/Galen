"""
Flask API Server - Main application
"""
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import uuid
import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import from same directory
from model_loader import model_loader
from symptom_matcher import SymptomMatcher
from conversation_engine import ConversationEngine

app = Flask(__name__, static_folder='../frontend', static_url_path='')
CORS(app)

# Store active sessions
sessions = {}

# ============================================
# DISEASE KNOWLEDGE BASE WITH REMEDIES
# ============================================

def get_disease_remedies(disease_name):
    """Get comprehensive remedies, precautions, and recommendations for a disease"""
    
    remedies_db = {
        'Migraine': {
            'description': 'A neurological condition characterized by recurrent, severe headaches often accompanied by nausea, vomiting, and sensitivity to light and sound.',
            'precautions': [
                'Avoid bright lights and loud noises during episodes',
                'Maintain regular sleep schedule (7-8 hours)',
                'Stay hydrated throughout the day',
                'Identify and avoid trigger foods (chocolate, caffeine, aged cheese)',
                'Manage stress through relaxation techniques'
            ],
            'recommendations': [
                'Rest in a dark, quiet room',
                'Apply cold compress to forehead or temples',
                'Over-the-counter pain relievers (ibuprofen, acetaminophen)',
                'Prescription triptans for severe cases',
                'Preventive medications if frequent',
                'Consider magnesium or riboflavin supplements'
            ]
        },
        'Common Cold': {
            'description': 'A viral infection of the upper respiratory tract causing runny nose, cough, sore throat, and mild fatigue.',
            'precautions': [
                'Get plenty of rest (7-9 hours)',
                'Stay hydrated with water, herbal tea, or clear broths',
                'Practice good hand hygiene to prevent spread',
                'Avoid close contact with others',
                'Use tissues and dispose of them properly'
            ],
            'recommendations': [
                'Warm salt water gargle for sore throat',
                'Honey (1-2 tsp) for cough (adults only)',
                'Steam inhalation with eucalyptus oil',
                'Over-the-counter cold medicines',
                'Vitamin C and zinc lozenges',
                'Use humidifier in bedroom'
            ]
        },
        'Fungal infection': {
            'description': 'A fungal infection affecting skin, nails, or mucous membranes, causing itching, redness, and discomfort.',
            'precautions': [
                'Keep affected area clean and completely dry',
                'Avoid sharing towels, clothes, or personal items',
                'Wear breathable cotton fabrics',
                'Change socks and underwear daily',
                'Avoid scratching to prevent spread'
            ],
            'recommendations': [
                'Over-the-counter antifungal creams (clotrimazole, miconazole)',
                'Keep area dry with antifungal powder',
                'Wash with antifungal soap',
                'Prescription oral antifungals for severe cases',
                'Wear flip-flops in public showers'
            ]
        },
        'GERD': {
            'description': 'Gastroesophageal reflux disease where stomach acid frequently flows back into the esophagus, causing heartburn and irritation.',
            'precautions': [
                'Avoid spicy, fatty, and acidic foods',
                'Don\'t lie down for 3 hours after eating',
                'Elevate head of bed 6-8 inches',
                'Eat smaller, more frequent meals',
                'Avoid tight-fitting clothing around waist'
            ],
            'recommendations': [
                'Antacids for quick relief (Tums, Rolaids)',
                'H2 blockers (Famotidine, Ranitidine)',
                'Proton pump inhibitors (Omeprazole)',
                'Chew sugar-free gum after meals',
                'Drink ginger or chamomile tea',
                'Lose weight if overweight'
            ]
        },
        'Hypertension': {
            'description': 'A condition where blood pressure in arteries is persistently elevated, increasing risk of heart disease and stroke.',
            'precautions': [
                'Reduce sodium intake (limit to 1500-2300mg daily)',
                'Exercise regularly (30 minutes, 5 days/week)',
                'Maintain healthy weight (BMI < 25)',
                'Limit alcohol consumption',
                'Quit smoking immediately',
                'Manage stress through meditation or yoga'
            ],
            'recommendations': [
                'Take prescribed blood pressure medications daily',
                'Monitor blood pressure at home regularly',
                'Follow DASH diet (fruits, vegetables, whole grains)',
                'Reduce caffeine intake',
                'Get adequate sleep (7-8 hours)',
                'Regular check-ups with doctor'
            ]
        },
        'Diabetes': {
            'description': 'A chronic condition affecting how the body converts food into energy due to problems with insulin production or utilization.',
            'precautions': [
                'Monitor blood sugar levels regularly',
                'Follow diabetic meal plan consistently',
                'Exercise regularly (30 minutes daily)',
                'Inspect feet daily for cuts or blisters',
                'Never skip meals or medications',
                'Stay hydrated with water'
            ],
            'recommendations': [
                'Take insulin or oral medications as prescribed',
                'Count carbohydrates in meals',
                'Regular eye exams (yearly)',
                'Foot exams by podiatrist',
                'Carry fast-acting sugar for hypoglycemia',
                'Join diabetes support group'
            ]
        },
        'Arthritis': {
            'description': 'Inflammation of one or more joints causing pain, stiffness, and decreased mobility.',
            'precautions': [
                'Low-impact exercise (swimming, walking)',
                'Maintain healthy weight to reduce joint stress',
                'Use joint protection techniques',
                'Apply heat before activity, ice after',
                'Avoid repetitive movements'
            ],
            'recommendations': [
                'NSAIDs for pain and inflammation',
                'Physical therapy for strengthening',
                'Topical pain relievers (capsaicin cream)',
                'Glucosamine and chondroitin supplements',
                'Warm baths with Epsom salts',
                'Assistive devices if needed'
            ]
        },
        'Pneumonia': {
            'description': 'Infection that inflames air sacs in the lungs, causing cough with phlegm, fever, chills, and difficulty breathing.',
            'precautions': [
                'Complete full course of antibiotics',
                'Get plenty of rest (2-3 days bed rest)',
                'Stay hydrated with warm fluids',
                'Use humidifier to loosen mucus',
                'Avoid smoking and secondhand smoke',
                'Isolate to prevent spread'
            ],
            'recommendations': [
                'Take antibiotics as prescribed',
                'Use fever reducers (acetaminophen)',
                'Practice deep breathing exercises',
                'Sleep in upright position',
                'Follow up with chest X-ray',
                'Get pneumonia vaccine after recovery'
            ]
        },
        'Urinary tract infection': {
            'description': 'Infection in any part of the urinary system, typically caused by bacteria entering the urethra.',
            'precautions': [
                'Drink plenty of water (8-10 glasses daily)',
                'Urinate frequently (don\'t hold it)',
                'Wipe front to back after using toilet',
                'Urinate before and after intercourse',
                'Avoid harsh soaps and douches'
            ],
            'recommendations': [
                'Take prescribed antibiotics completely',
                'Cranberry juice or supplements',
                'Use heating pad for discomfort',
                'Over-the-counter urinary pain relievers',
                'Probiotics to restore good bacteria',
                'Wear cotton underwear'
            ]
        },
        'Jaundice': {
            'description': 'Yellow discoloration of skin and eyes caused by high bilirubin levels, indicating liver problems.',
            'precautions': [
                'Complete abstinence from alcohol',
                'Avoid acetaminophen and hepatotoxic drugs',
                'Eat small, frequent meals',
                'Get adequate rest',
                'Avoid fatty and processed foods'
            ],
            'recommendations': [
                'Treat underlying liver condition',
                'Increase fluid intake',
                'Eat liver-friendly foods (leafy greens)',
                'Vitamin K supplements if needed',
                'Follow up with gastroenterologist',
                'Monitor bilirubin levels regularly'
            ]
        }
    }
    
    # Try to match disease name with database
    for key, value in remedies_db.items():
        if key.lower() in disease_name.lower() or disease_name.lower() in key.lower():
            return value
    
    # Default response for any disease not in database
    return {
        'description': f'{disease_name} - A medical condition that requires proper medical evaluation and treatment.',
        'precautions': [
            'Consult a qualified healthcare professional',
            'Follow prescribed treatment plan exactly',
            'Monitor symptoms and report changes',
            'Get adequate rest and proper nutrition',
            'Avoid self-medication without consultation'
        ],
        'recommendations': [
            'Schedule appointment with specialist',
            'Complete recommended diagnostic tests',
            'Follow up regularly with your doctor',
            'Maintain healthy lifestyle habits',
            'Keep a symptom diary for reference'
        ]
    }

# ============================================
# API ROUTES
# ============================================

@app.route('/')
def serve_frontend():
    """Serve the HTML frontend"""
    return send_from_directory('../frontend', 'index.html')

@app.route('/api/start', methods=['POST'])
def start_conversation():
    """Start a new consultation"""
    session_id = str(uuid.uuid4())
    
    # Initialize matcher with all symptoms
    matcher = SymptomMatcher(model_loader.get_all_symptoms())
    engine = ConversationEngine(matcher)
    
    sessions[session_id] = {
        'engine': engine,
        'matcher': matcher,
        'symptoms': []
    }
    
    greeting = engine.get_greeting()
    
    return jsonify({
        'session_id': session_id,
        'message': greeting,
        'quick_replies': ['Headache', 'Fever', 'Cough', 'Fatigue', 'Stomach pain', 'Nausea']
    })

@app.route('/api/chat', methods=['POST'])
def chat():
    """Process user message"""
    data = request.json
    session_id = data.get('session_id')
    user_message = data.get('message', '')
    
    session = sessions.get(session_id)
    if not session:
        return jsonify({'error': 'Session not found'}), 404
    
    engine = session['engine']
    
    # Process user message
    response = engine.process_message(user_message)
    
    # Store extracted symptoms in session
    session['symptoms'] = engine.collected_symptoms
    
    # If ready for prediction, include predictions with remedies
    if response['type'] == 'ready' or engine.ready_for_prediction:
        predictions = model_loader.predict(engine.collected_symptoms)
        
        # Add remedies and precautions to each prediction
        enhanced_predictions = []
        for pred in predictions:
            remedies = get_disease_remedies(pred['disease'])
            enhanced_predictions.append({
                'disease': pred['disease'],
                'confidence': pred['confidence'],
                'description': remedies['description'],
                'precautions': remedies['precautions'],
                'recommendations': remedies['recommendations']
            })
        
        return jsonify({
            'type': 'prediction',
            'message': response['message'],
            'predictions': enhanced_predictions,
            'symptoms': engine.collected_symptoms
        })
    
    # Return conversation response
    return jsonify({
        'type': response['type'],
        'message': response['message'],
        'quick_replies': response.get('quick_replies', [])
    })

@app.route('/api/reset', methods=['POST'])
def reset_session():
    """Reset a session"""
    data = request.json
    session_id = data.get('session_id')
    
    if session_id in sessions:
        sessions[session_id]['engine'].reset()
        sessions[session_id]['symptoms'] = []
    
    return jsonify({'success': True})

# ============================================
# MAIN ENTRY POINT
# ============================================

if __name__ == '__main__':
    print("\n" + "="*60)
    print("🤖 GALEN AI - Medical Diagnosis System")
    print("="*60)
    print(f"\n✅ Model loaded: {len(model_loader.get_all_diseases())} diseases")
    print(f"✅ Symptoms: {len(model_loader.get_all_symptoms())}")
    print(f"✅ Remedies database loaded for 10+ conditions")
    print("\n🌐 Server running at: http://127.0.0.1:5000")
    print("="*60 + "\n")
    
    app.run(debug=True, host='127.0.0.1', port=5000)