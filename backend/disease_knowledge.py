"""
Disease Knowledge Base - Contains descriptions, precautions, and recommendations for all 41 diseases
"""

disease_knowledge = {
    '(vertigo) Paroymsal Positional Vertigo': {
        'description': 'Benign paroxysmal positional vertigo (BPPV) is an inner ear disorder that causes brief episodes of intense dizziness (vertigo) triggered by head movements.',
        'precautions': [
            'Avoid sudden head movements',
            'Sleep with head elevated',
            'Avoid looking up for long periods',
            'Move slowly when getting out of bed'
        ],
        'recommendations': [
            'Perform Epley maneuver as directed by doctor',
            'Vestibular rehabilitation exercises',
            'Avoid driving during episodes'
        ]
    },
    'AIDS': {
        'description': 'Acquired Immunodeficiency Syndrome (AIDS) is a chronic, life-threatening condition caused by the human immunodeficiency virus (HIV).',
        'precautions': [
            'Practice safe sex',
            'Avoid sharing needles',
            'Regular medical checkups',
            'Take ART medication consistently'
        ],
        'recommendations': [
            'Antiretroviral therapy (ART)',
            'Regular CD4 count monitoring',
            'Prevention of opportunistic infections'
        ]
    },
    'Acne': {
        'description': 'Acne is a skin condition that occurs when hair follicles become plugged with oil and dead skin cells, causing pimples, blackheads, or whiteheads.',
        'precautions': [
            'Keep face clean but don\'t over-wash',
            'Avoid touching face',
            'Don\'t pop pimples',
            'Use non-comedogenic products'
        ],
        'recommendations': [
            'Benzoyl peroxide or salicylic acid',
            'Topical retinoids',
            'Antibiotics if severe'
        ]
    },
    'Alcoholic hepatitis': {
        'description': 'Alcoholic hepatitis is liver inflammation caused by heavy alcohol consumption over an extended period.',
        'precautions': [
            'Complete alcohol abstinence',
            'Avoid acetaminophen',
            'Maintain proper nutrition',
            'Regular liver function tests'
        ],
        'recommendations': [
            'Alcohol cessation program',
            'Corticosteroids for severe cases',
            'Nutritional supplements'
        ]
    },
    'Allergy': {
        'description': 'An allergy is an immune system reaction to a foreign substance that is not typically harmful to the body.',
        'precautions': [
            'Identify and avoid allergens',
            'Keep home dust-free',
            'Use air purifiers',
            'Avoid known trigger foods'
        ],
        'recommendations': [
            'Antihistamines',
            'Nasal corticosteroids',
            'Allergy shots (immunotherapy)'
        ]
    },
    'Arthritis': {
        'description': 'Arthritis is the swelling and tenderness of one or more joints, causing joint pain and stiffness.',
        'precautions': [
            'Low-impact exercise',
            'Maintain healthy weight',
            'Use joint protection techniques',
            'Apply heat/cold therapy'
        ],
        'recommendations': [
            'NSAIDs for pain relief',
            'Physical therapy',
            'Disease-modifying antirheumatic drugs (DMARDs)'
        ]
    },
    'Bronchial Asthma': {
        'description': 'Bronchial asthma is a condition where airways narrow and swell, producing extra mucus, making breathing difficult.',
        'precautions': [
            'Avoid asthma triggers',
            'Keep rescue inhaler always',
            'Monitor peak flow',
            'Avoid smoke and strong odors'
        ],
        'recommendations': [
            'Inhaled corticosteroids',
            'Bronchodilators',
            'Asthma action plan'
        ]
    },
    'Cervical spondylosis': {
        'description': 'Cervical spondylosis is age-related wear and tear of spinal disks in the neck.',
        'precautions': [
            'Good neck posture',
            'Avoid heavy lifting',
            'Use ergonomic workstation',
            'Neck strengthening exercises'
        ],
        'recommendations': [
            'Physical therapy',
            'Neck traction',
            'Pain medications'
        ]
    },
    'Chicken pox': {
        'description': 'Chickenpox is a viral infection causing an itchy rash with small, fluid-filled blisters.',
        'precautions': [
            'Isolate to prevent spread',
            'Avoid scratching blisters',
            'Keep fingernails short',
            'Use calamine lotion'
        ],
        'recommendations': [
            'Antiviral medications',
            'Cool baths with oatmeal',
            'Acetaminophen for fever'
        ]
    },
    'Chronic cholestasis': {
        'description': 'Chronic cholestasis is a liver disease where bile flow is reduced or blocked.',
        'precautions': [
            'Avoid alcohol',
            'Low-fat diet',
            'Adequate calcium intake',
            'Monitor vitamin levels'
        ],
        'recommendations': [
            'Ursodeoxycholic acid',
            'Antihistamines for itching',
            'Vitamin supplements'
        ]
    },
    'Common Cold': {
        'description': 'The common cold is a viral infection of upper respiratory tract affecting nose and throat.',
        'precautions': [
            'Rest and stay hydrated',
            'Practice hand hygiene',
            'Avoid close contact with others',
            'Use humidifier'
        ],
        'recommendations': [
            'Over-the-counter cold remedies',
            'Warm salt water gargle',
            'Honey for cough'
        ]
    },
    'Dengue': {
        'description': 'Dengue is a mosquito-borne viral infection causing high fever, severe headache, and joint pain.',
        'precautions': [
            'Prevent mosquito bites',
            'Use mosquito nets/repellents',
            'Eliminate standing water',
            'Monitor platelet count'
        ],
        'recommendations': [
            'Rest and hydration',
            'Acetaminophen (avoid aspirin)',
            'Hospitalization if severe'
        ]
    },
    'Diabetes': {
        'description': 'Diabetes is a chronic condition affecting how body converts food into energy due to insulin problems.',
        'precautions': [
            'Monitor blood sugar regularly',
            'Follow diabetic diet',
            'Regular exercise',
            'Foot care daily'
        ],
        'recommendations': [
            'Insulin or oral medications',
            'Carbohydrate counting',
            'Regular eye and foot exams'
        ]
    },
    'Dimorphic hemmorhoids(piles)': {
        'description': 'Hemorrhoids are swollen veins in the lower rectum and anus, causing discomfort and bleeding.',
        'precautions': [
            'High-fiber diet',
            'Drink plenty water',
            'Avoid straining during bowel movements',
            'Don\'t sit for long periods'
        ],
        'recommendations': [
            'Topical treatments',
            'Sitz baths',
            'Minimally invasive procedures if severe'
        ]
    },
    'Drug Reaction': {
        'description': 'An adverse drug reaction is an unwanted or harmful reaction experienced following administration of a drug.',
        'precautions': [
            'Stop suspected medication',
            'Inform all doctors about allergies',
            'Wear medical alert bracelet',
            'Keep medication list'
        ],
        'recommendations': [
            'Antihistamines for mild reactions',
            'Corticosteroids',
            'Emergency care for severe reactions'
        ]
    },
    'Fungal infection': {
        'description': 'Fungal infections are caused by fungi and can affect skin, nails, or internal organs.',
        'precautions': [
            'Keep skin clean and dry',
            'Avoid sharing personal items',
            'Wear breathable fabrics',
            'Change socks and underwear daily'
        ],
        'recommendations': [
            'Antifungal creams or ointments',
            'Oral antifungal medications',
            'Proper hygiene practices'
        ]
    },
    'GERD': {
        'description': 'Gastroesophageal reflux disease (GERD) is chronic acid reflux where stomach acid flows back into the esophagus.',
        'precautions': [
            'Avoid trigger foods',
            'Don\'t lie down after eating',
            'Elevate head while sleeping',
            'Eat smaller meals'
        ],
        'recommendations': [
            'Proton pump inhibitors',
            'H2 blockers',
            'Lifestyle modifications'
        ]
    },
    'Gastroenteritis': {
        'description': 'Gastroenteritis is inflammation of the stomach and intestines, typically causing diarrhea and vomiting.',
        'precautions': [
            'Stay hydrated',
            'Rest digestive system',
            'Practice good hygiene',
            'Avoid dairy and fatty foods'
        ],
        'recommendations': [
            'Oral rehydration solution',
            'BRAT diet (Bananas, Rice, Applesauce, Toast)',
            'Probiotics'
        ]
    },
    'Heart attack': {
        'description': 'A heart attack (myocardial infarction) occurs when blood flow to the heart is severely reduced or blocked.',
        'precautions': [
            'Call emergency immediately',
            'Chew aspirin if not allergic',
            'Stay calm and rest',
            'CPR if person is unconscious'
        ],
        'recommendations': [
            'Emergency medical care',
            'Angioplasty or stenting',
            'Cardiac rehabilitation'
        ]
    },
    'Hepatitis B': {
        'description': 'Hepatitis B is a serious liver infection caused by the hepatitis B virus (HBV).',
        'precautions': [
            'Get vaccinated',
            'Practice safe sex',
            'Don\'t share needles',
            'Avoid alcohol'
        ],
        'recommendations': [
            'Antiviral medications',
            'Regular liver function monitoring',
            'Liver transplant if severe'
        ]
    },
    'Hepatitis C': {
        'description': 'Hepatitis C is a viral infection that causes liver inflammation, sometimes leading to serious liver damage.',
        'precautions': [
            'Avoid sharing personal items',
            'No alcohol consumption',
            'Safe injection practices',
            'Regular monitoring'
        ],
        'recommendations': [
            'Direct-acting antiviral medications',
            'Lifestyle modifications',
            'Liver specialist follow-up'
        ]
    },
    'Hepatitis D': {
        'description': 'Hepatitis D is a liver infection caused by the hepatitis D virus, which only occurs in people with hepatitis B.',
        'precautions': [
            'Prevent hepatitis B first',
            'Avoid alcohol',
            'Safe sex practices',
            'No needle sharing'
        ],
        'recommendations': [
            'Pegylated interferon alpha',
            'Liver protection medications',
            'Regular liver function tests'
        ]
    },
    'Hepatitis E': {
        'description': 'Hepatitis E is a liver disease caused by the hepatitis E virus, typically spread through contaminated water.',
        'precautions': [
            'Drink clean water',
            'Practice good sanitation',
            'Cook food thoroughly',
            'Avoid raw shellfish'
        ],
        'recommendations': [
            'Supportive care',
            'Rest and hydration',
            'Hospitalization if severe'
        ]
    },
    'Hepatitis A': {
        'description': 'Hepatitis A is a highly contagious liver infection caused by the hepatitis A virus.',
        'precautions': [
            'Get vaccinated',
            'Wash hands frequently',
            'Avoid contaminated food/water',
            'Practice good sanitation'
        ],
        'recommendations': [
            'Supportive care',
            'Rest and nutrition',
            'Avoid alcohol and acetaminophen'
        ]
    },
    'Hypertension': {
        'description': 'Hypertension (high blood pressure) is a common condition where blood pressure is consistently too high.',
        'precautions': [
            'Reduce salt intake',
            'Regular exercise',
            'Maintain healthy weight',
            'Limit alcohol'
        ],
        'recommendations': [
            'Blood pressure medications',
            'DASH diet',
            'Regular blood pressure monitoring'
        ]
    },
    'Hyperthyroidism': {
        'description': 'Hyperthyroidism occurs when the thyroid gland produces too much thyroxine hormone.',
        'precautions': [
            'Avoid iodine-rich foods',
            'Manage stress',
            'Regular thyroid tests',
            'Avoid stimulants'
        ],
        'recommendations': [
            'Antithyroid medications',
            'Radioactive iodine',
            'Beta-blockers for symptoms'
        ]
    },
    'Hypoglycemia': {
        'description': 'Hypoglycemia is a condition where blood sugar levels drop below normal levels.',
        'precautions': [
            'Eat regular meals',
            'Carry fast-acting sugar source',
            'Monitor blood sugar',
            'Don\'t skip meals'
        ],
        'recommendations': [
            '15-15 rule (15g carbs, wait 15 minutes)',
            'Adjust diabetes medication',
            'Regular meal schedule'
        ]
    },
    'Hypothyroidism': {
        'description': 'Hypothyroidism occurs when the thyroid gland doesn\'t produce enough thyroid hormone.',
        'precautions': [
            'Take medication consistently',
            'Avoid raw goitrogenic foods',
            'Regular TSH monitoring',
            'Report symptoms to doctor'
        ],
        'recommendations': [
            'Levothyroxine replacement',
            'Thyroid function tests',
            'Dietary adjustments'
        ]
    },
    'Impetigo': {
        'description': 'Impetigo is a common, highly contagious skin infection causing red sores and blisters.',
        'precautions': [
            'Keep sores clean and covered',
            'Avoid scratching',
            'Don\'t share towels/clothes',
            'Wash hands frequently'
        ],
        'recommendations': [
            'Topical antibiotics',
            'Oral antibiotics if severe',
            'Good hygiene practices'
        ]
    },
    'Jaundice': {
        'description': 'Jaundice is a condition causing yellowing of skin and eyes due to high bilirubin levels.',
        'precautions': [
            'Avoid alcohol',
            'Eat balanced diet',
            'Rest adequately',
            'Follow liver-friendly diet'
        ],
        'recommendations': [
            'Treat underlying cause',
            'Phototherapy if indicated',
            'Liver function monitoring'
        ]
    },
    'Malaria': {
        'description': 'Malaria is a mosquito-borne disease caused by parasites, causing fever, chills, and flu-like illness.',
        'precautions': [
            'Use mosquito nets',
            'Apply insect repellent',
            'Take preventive medication if traveling',
            'Remove standing water'
        ],
        'recommendations': [
            'Antimalarial medications',
            'Supportive care',
            'Hospitalization if severe'
        ]
    },
    'Migraine': {
        'description': 'Migraine is a neurological condition causing severe headaches, often with nausea and sensitivity to light/sound.',
        'precautions': [
            'Identify and avoid triggers',
            'Maintain regular sleep schedule',
            'Stay hydrated',
            'Manage stress'
        ],
        'recommendations': [
            'Acute pain relief medications',
            'Preventive medications',
            'Lifestyle modifications'
        ]
    },
    'Osteoarthristis': {
        'description': 'Osteoarthritis is the most common form of arthritis, causing joint cartilage breakdown.',
        'precautions': [
            'Maintain healthy weight',
            'Low-impact exercise',
            'Use joint protection',
            'Apply heat/cold therapy'
        ],
        'recommendations': [
            'Pain relievers',
            'Physical therapy',
            'Joint replacement if severe'
        ]
    },
    'Paralysis (brain hemorrhage)': {
        'description': 'Brain hemorrhage is bleeding in or around the brain, often causing paralysis and other neurological deficits.',
        'precautions': [
            'Control blood pressure',
            'Immediate emergency care',
            'Prevent falls',
            'Regular medical follow-up'
        ],
        'recommendations': [
            'Emergency medical treatment',
            'Rehabilitation therapy',
            'Lifestyle modifications'
        ]
    },
    'Peptic ulcer disease': {
        'description': 'Peptic ulcer disease involves open sores that develop on the stomach lining and upper small intestine.',
        'precautions': [
            'Avoid NSAIDs',
            'Quit smoking',
            'Limit alcohol',
            'Avoid spicy/acidic foods'
        ],
        'recommendations': [
            'Proton pump inhibitors',
            'Antibiotics if H. pylori present',
            'Antacids for symptom relief'
        ]
    },
    'Pneumonia': {
        'description': 'Pneumonia is an infection that inflames air sacs in one or both lungs, causing them to fill with fluid.',
        'precautions': [
            'Get vaccinated',
            'Practice good hygiene',
            'Avoid smoking',
            'Rest and hydration'
        ],
        'recommendations': [
            'Antibiotics if bacterial',
            'Antiviral medications',
            'Rest and fluids'
        ]
    },
    'Psoriasis': {
        'description': 'Psoriasis is a skin disease causing red, itchy, scaly patches, most commonly on knees, elbows, trunk, and scalp.',
        'precautions': [
            'Avoid skin injuries',
            'Manage stress',
            'Avoid trigger medications',
            'Moisturize regularly'
        ],
        'recommendations': [
            'Topical corticosteroids',
            'Phototherapy',
            'Systemic medications'
        ]
    },
    'Tuberculosis': {
        'description': 'Tuberculosis (TB) is a bacterial infection that primarily affects the lungs but can affect other organs.',
        'precautions': [
            'Isolate during contagious period',
            'Cover mouth when coughing',
            'Complete full treatment course',
            'Ensure good ventilation'
        ],
        'recommendations': [
            'Multi-drug regimen',
            'Directly observed therapy',
            'Regular monitoring'
        ]
    },
    'Typhoid': {
        'description': 'Typhoid fever is a bacterial infection caused by Salmonella typhi, spread through contaminated food and water.',
        'precautions': [
            'Drink clean water',
            'Get vaccinated',
            'Wash hands frequently',
            'Avoid raw foods when traveling'
        ],
        'recommendations': [
            'Antibiotics',
            'Hydration',
            'Rest and nutrition'
        ]
    },
    'Urinary tract infection': {
        'description': 'A UTI is an infection in any part of the urinary system, typically caused by bacteria.',
        'precautions': [
            'Stay hydrated',
            'Urinate when needed',
            'Wipe front to back',
            'Urinate after intercourse'
        ],
        'recommendations': [
            'Antibiotics',
            'Increased fluid intake',
            'Cranberry products (may help)'
        ]
    },
    'Varicose veins': {
        'description': 'Varicose veins are enlarged, twisted veins that usually appear blue or dark purple, often in legs.',
        'precautions': [
            'Regular exercise',
            'Elevate legs when resting',
            'Avoid prolonged standing',
            'Wear compression stockings'
        ],
        'recommendations': [
            'Compression therapy',
            'Sclerotherapy',
            'Laser treatment'
        ]
    }
}

def get_disease_info(disease_name):
    """Get disease information by name"""
    if disease_name in disease_knowledge:
        return disease_knowledge[disease_name]
    else:
        # Return default info if disease not found
        return {
            'description': f'{disease_name} is a medical condition that should be evaluated by a healthcare professional.',
            'precautions': [
                'Consult a healthcare professional',
                'Follow prescribed treatment plan',
                'Monitor symptoms regularly'
            ],
            'recommendations': [
                'Seek professional medical advice',
                'Complete recommended tests',
                'Follow up with your doctor'
            ]
        }

def get_all_disease_names():
    """Return list of all diseases in knowledge base"""
    return list(disease_knowledge.keys())