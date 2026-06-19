"""
Symptom Matcher - Advanced NLP for symptom extraction from natural language
Includes ALL 131 symptoms from your dataset
"""
import re
from difflib import get_close_matches

class SymptomMatcher:
    def __init__(self, symptom_columns):
        self.symptom_columns = symptom_columns
        self.symptom_aliases = self._create_aliases()
        self.symptom_patterns = self._create_patterns()
    
    def _create_aliases(self):
        """Create comprehensive natural language aliases for ALL 131 symptoms"""
        aliases = {}
        
        # Complete mapping for ALL symptoms from your dataset
        alias_map = {
            # Original 131 symptoms with natural language variations
            'abdominal_pain': ['stomach pain', 'belly pain', 'tummy ache', 'abdomen pain', 'stomach ache', 'belly ache', 'abdominal discomfort', 'cramping', 'pain in stomach'],
            'abnormal_menstruation': ['irregular periods', 'abnormal periods', 'menstrual problems', 'period issues', 'irregular cycle', 'heavy periods', 'missed periods'],
            'acidity': ['acid reflux', 'heartburn', 'acidity problem', 'acidic stomach', 'hyperacidity', 'burning sensation in chest', 'sour stomach'],
            'acute_liver_failure': ['liver failure', 'liver problems', 'liver damage', 'severe liver condition'],
            'altered_sensorium': ['altered mental state', 'consciousness changes', 'mental confusion', 'changed awareness'],
            'anxiety': ['nervous', 'worried', 'stressed', 'panic', 'feeling anxious', 'restless', 'uneasy', 'anxious feeling'],
            'back_pain': ['back ache', 'lower back pain', 'back hurting', 'spinal pain', 'lumbar pain', 'back discomfort', 'pain in back'],
            'belly_pain': ['belly ache', 'stomach pain', 'tummy pain', 'abdominal pain', 'belly hurting'],
            'blackheads': ['black heads', 'clogged pores', 'skin blackheads', 'black spots on skin', 'open comedones'],
            'bladder_discomfort': ['bladder pain', 'urinary discomfort', 'bladder irritation', 'bladder pressure', 'uncomfortable bladder'],
            'blister': ['blisters', 'skin blister', 'fluid filled bumps', 'vesicles', 'bubbles on skin'],
            'blood_in_sputum': ['blood in mucus', 'coughing blood', 'bloody phlegm', 'hemoptysis', 'blood when coughing'],
            'bloody_stool': ['blood in stool', 'bloody feces', 'blood in poop', 'rectal bleeding', 'blood when pooping', 'bloody bowel movement'],
            'blurred_and_distorted_vision': ['blurred vision', 'blurry vision', 'vision problems', 'can\'t see clearly', 'distorted vision', 'fuzzy vision', 'blurred sight'],
            'breathlessness': ['shortness of breath', 'difficulty breathing', 'can\'t breathe', 'out of breath', 'dyspnea', 'breathing difficulty', 'struggling to breathe'],
            'brittle_nails': ['weak nails', 'breaking nails', 'fragile nails', 'nails breaking easily', 'soft nails'],
            'bruising': ['bruises', 'easy bruising', 'black and blue marks', 'contusions', 'bruise easily'],
            'burning_micturition': ['burning urine', 'painful urination', 'burning when peeing', 'dysuria', 'pain while urinating', 'burning sensation while urinating'],
            'chest_pain': ['chest discomfort', 'heart pain', 'sternum pain', 'chest tightness', 'pain in chest', 'chest pressure'],
            'chills': ['shivering', 'cold chills', 'feeling cold', 'rigors', 'shaking chills', 'cold flashes', 'body shaking'],
            'cold_hands_and_feets': ['cold hands', 'cold feet', 'cold extremities', 'hands and feet cold', 'poor circulation'],
            'coma': ['unconscious', 'passed out', 'unresponsive', 'comatose', 'not waking up'],
            'congestion': ['nasal congestion', 'stuffy nose', 'blocked nose', 'nasal blockage', 'stuffed up nose', 'clogged nose'],
            'constipation': ['hard stool', 'difficulty pooping', 'constipated', 'irregular bowel', 'can\'t poop', 'straining', 'hard to pass stool'],
            'continuous_feel_of_urine': ['constant urge to urinate', 'frequent urination', 'always need to pee', 'urinary frequency'],
            'continuous_sneezing': ['sneezing', 'sneezing fits', 'constant sneezing', 'keeps sneezing', 'sneezing repeatedly'],
            'cough': ['coughing', 'dry cough', 'wet cough', 'hacking', 'coughing fit', 'persistent cough', 'chronic cough'],
            'cramps': ['muscle cramps', 'leg cramps', 'stomach cramps', 'cramping pain', 'muscle spasms', 'charley horse'],
            'dark_urine': ['dark urine', 'dark yellow urine', 'brown urine', 'tea colored urine', 'dark pee', 'cola colored urine', 'dark yellow pee', 'urine dark color'],
            'dehydration': ['dry mouth', 'thirsty', 'fluid loss', 'not drinking enough', 'parched', 'dehydrated', 'feeling very thirsty'],
            'depression': ['feeling down', 'sadness', 'hopeless', 'depressed mood', 'low mood', 'unhappy', 'feeling depressed'],
            'diarrhoea': ['loose stools', 'watery stool', 'diarrhea', 'frequent bowel movements', 'loose motion', 'running stomach'],
            'dischromic_patches': ['skin discoloration', 'color change on skin', 'patchy skin', 'discolored patches', 'uneven skin tone'],
            'distention_of_abdomen': ['bloated stomach', 'swollen belly', 'abdominal bloating', 'gas distention', 'stomach distended'],
            'dizziness': ['dizzy', 'lightheaded', 'spinning sensation', 'vertigo', 'woozy', 'feeling faint', 'room spinning', 'unsteady'],
            'drying_and_tingling_lips': ['dry lips', 'chapped lips', 'tingling lips', 'dry and tingly lips', 'lip discomfort'],
            'enlarged_thyroid': ['swollen thyroid', 'thyroid enlargement', 'goiter', 'neck swelling', 'thyroid swelling'],
            'excessive_hunger': ['always hungry', 'constant hunger', 'polyphagia', 'hungry all the time', 'increased appetite'],
            'extra_marital_contacts': ['unprotected sex', 'sexual contact outside marriage', 'std risk', 'unsafe sexual contact'],
            'family_history': ['family medical history', 'genetic condition', 'runs in family', 'family has history', 'hereditary'],
            'fast_heart_rate': ['rapid heartbeat', 'tachycardia', 'racing heart', 'heart racing', 'fast pulse', 'heart beating fast'],
            'fatigue': ['tired', 'exhausted', 'low energy', 'sleepy', 'worn out', 'fatigued', 'lack of energy', 'feeling weak', 'drained', 'no energy'],
            'fluid_overload': ['water retention', 'excess fluid', 'edema', 'fluid retention', 'swelling from fluid'],
            'foul_smell_of urine': ['bad smelling urine', 'foul urine odor', 'stinky pee', 'urine smells bad', 'strong urine smell'],
            'headache': ['head pain', 'head hurts', 'pain in head', 'migraine', 'headache pain', 'throbbing head', 'splitting headache', 'head pounding', 'skull pain'],
            'high_fever': ['high temperature', 'very hot', 'high grade fever', 'fever above 101', 'high temp', 'burning up'],
            'hip_joint_pain': ['hip pain', 'pain in hip', 'hip discomfort', 'hip joint hurting', 'sore hip'],
            'history_of_alcohol_consumption': ['alcohol use', 'drinking history', 'alcoholic', 'heavy drinker', 'drinks alcohol', 'past drinking'],
            'increased_appetite': ['eating more', 'hungry often', 'polyphagia', 'appetite increase', 'more hungry than usual'],
            'indigestion': ['upset stomach', 'dyspepsia', 'stomach discomfort after eating', 'difficulty digesting', 'food not digesting'],
            'inflammatory_nails': ['inflamed nails', 'nail inflammation', 'red around nails', 'swollen nail bed'],
            'internal_itching': ['itching inside', 'internal itch', 'deep itching', 'inner itching sensation'],
            'irregular_sugar_level': ['blood sugar fluctuation', 'unstable sugar', 'glucose variation', 'sugar level ups and downs'],
            'irritability': ['easily annoyed', 'short tempered', 'irritable mood', 'frustrated easily', 'getting angry quickly'],
            'irritation_in_anus': ['anal itching', 'rectal irritation', 'itchy anus', 'anal discomfort', 'burning anus'],
            'itching': ['itchy', 'itch', 'itching sensation', 'pruritus', 'skin itching', 'constantly scratching', 'itchy skin'],
            'joint_pain': ['joint ache', 'pain in joints', 'arthralgia', 'joints hurting', 'arthritic pain', 'sore joints'],
            'knee_pain': ['pain in knee', 'knee ache', 'knee discomfort', 'knee hurting', 'sore knee'],
            'lack_of_concentration': ['can\'t focus', 'poor concentration', 'difficulty concentrating', 'brain fog', 'can\'t think straight'],
            'lethargy': ['sluggish', 'lack of energy', 'feeling sluggish', 'unmotivated', 'moving slowly'],
            'loss_of_appetite': ['no appetite', 'don\'t want to eat', 'can\'t eat', 'anorexia', 'not hungry', 'eating less'],
            'loss_of_balance': ['unsteady', 'balance problems', 'falling easily', 'equilibrium issue', 'can\'t walk straight'],
            'loss_of_smell': ['can\'t smell', 'anosmia', 'smell loss', 'no sense of smell', 'lost smell', 'cannot smell'],
            'malaise': ['feeling unwell', 'general discomfort', 'sick feeling', 'under the weather', 'feeling off'],
            'mild_fever': ['low grade fever', 'slight fever', 'mild temperature', 'low fever', 'slight temperature'],
            'mood_swings': ['emotional changes', 'rapid mood changes', 'mood fluctuations', 'bipolar like', 'mood changing fast'],
            'movement_stiffness': ['stiff movements', 'rigid movement', 'stiffness in motion', 'moving stiffly', 'hard to move'],
            'mucoid_sputum': ['mucus in phlegm', 'sputum with mucus', 'thick phlegm', 'mucous discharge', 'slimy cough'],
            'muscle_pain': ['muscle ache', 'body ache', 'sore muscles', 'myalgia', 'whole body aches', 'muscle soreness'],
            'muscle_wasting': ['muscle loss', 'muscle atrophy', 'losing muscle mass', 'muscles getting smaller', 'wasting away'],
            'muscle_weakness': ['weak muscles', 'muscle fatigue', 'reduced muscle strength', 'muscles feel weak', 'can\'t lift'],
            'nausea': ['feel sick', 'queasy', 'nauseous', 'sick to stomach', 'stomach upset', 'want to throw up', 'feeling nauseated', 'green around gills'],
            'neck_pain': ['neck ache', 'cervical pain', 'stiff neck', 'neck discomfort', 'pain in neck', 'sore neck'],
            'nodal_skin_eruptions': ['skin nodes', 'nodules on skin', 'skin bumps', 'lumps on skin', 'nodular rash'],
            'obesity': ['overweight', 'excess weight', 'fat overweight', 'high bmi', 'very overweight', 'morbidly obese'],
            'pain_behind_the_eyes': ['eye pain', 'orbital pain', 'pain in back of eyes', 'eye pressure', 'eyes hurting'],
            'pain_during_bowel_movements': ['painful poop', 'pain when pooping', 'dyschezia', 'hurts to poop'],
            'pain_in_anal_region': ['anal pain', 'rectal pain', 'pain in anus', 'anus hurting'],
            'painful_walking': ['pain when walking', 'walking difficulty due to pain', 'ambulation pain', 'hurts to walk'],
            'palpitations': ['heart palpitations', 'racing heartbeat', 'irregular heartbeat', 'heart fluttering', 'heart pounding', 'skipped beats'],
            'passage_of_gases': ['flatulence', 'passing gas', 'farting', 'bloating gas', 'gas passing'],
            'patches_in_throat': ['throat patches', 'pharyngeal patches', 'throat spots', 'white patches throat'],
            'phlegm': ['mucus', 'sputum', 'throat mucus', 'phlegm production', 'coughing up mucus'],
            'polyuria': ['excessive urination', 'peeing a lot', 'frequent urination', 'urinating often', 'peeing too much'],
            'prominent_veins_on_calf': ['visible leg veins', 'varicose veins', 'bulging calf veins', 'spider veins', 'swollen leg veins'],
            'puffy_face_and_eyes': ['facial swelling', 'puffiness around eyes', 'swollen face', 'periorbital edema', 'puffy eyes'],
            'pus_filled_pimples': ['pustules', 'pimples with pus', 'infected pimples', 'acne with pus', 'whiteheads'],
            'receiving_blood_transfusion': ['blood transfusion history', 'received blood', 'transfusion'],
            'receiving_unsterile_injections': ['unclean injections', 'dirty needles', 'unsterile shots', 'unsafe injections'],
            'red_sore_around_nose': ['redness around nose', 'sore nose', 'nasal redness', 'red nose'],
            'red_spots_over_body': ['red dots', 'petechiae', 'red spots on skin', 'rash spots', 'red marks on body'],
            'redness_of_eyes': ['red eyes', 'bloodshot eyes', 'eye redness', 'conjunctival redness', 'eyes look red'],
            'restlessness': ['can\'t sit still', 'restless feeling', 'agitation', 'fidgety', 'always moving'],
            'runny_nose': ['nose running', 'nasal discharge', 'rhinorrhea', 'dripping nose', 'runny nose', 'watery nose'],
            'rusty_sputum': ['rust colored phlegm', 'brown sputum', 'rust phlegm', 'brown mucus'],
            'scurring': ['scarring', 'skin scars', 'scar tissue', 'scar formation'],
            'shivering': ['shakes', 'trembling', 'shivering fit', 'rigors', 'body shaking'],
            'silver_like_dusting': ['silvery scales', 'dandruff like scales', 'scaly skin', 'silver scales'],
            'sinus_pressure': ['sinus pain', 'facial pressure', 'sinus congestion', 'sinus headache', 'pressure in face'],
            'skin_peeling': ['peeling skin', 'flaking skin', 'skin desquamation', 'skin coming off', 'shedding skin'],
            'skin_rash': ['rash', 'skin irritation', 'red rash', 'skin eruption', 'dermatitis', 'red spots', 'bumps on skin'],
            'slurred_speech': ['speech difficulty', 'slurred talking', 'dysarthria', 'can\'t speak clearly', 'talking funny'],
            'small_dents_in_nails': ['nail pitting', 'dented nails', 'nail depressions', 'holes in nails'],
            'spinning_movements': ['vertigo', 'room spinning', 'spinning sensation', 'rotatory dizziness', 'everything spinning'],
            'spotting_urination': ['blood in urine', 'hematuria', 'bloody pee', 'urine spotting', 'blood when peeing'],
            'stiff_neck': ['neck stiffness', 'rigid neck', 'nuchal rigidity', 'can\'t move neck', 'stiff neck'],
            'stomach_bleeding': ['gastric bleeding', 'blood in stomach', 'upper gi bleed', 'bleeding stomach'],
            'stomach_pain': ['abdominal pain', 'belly ache', 'stomach ache', 'gastric pain', 'pain in belly'],
            'sunken_eyes': ['hollow eyes', 'enophthalmos', 'deep set eyes', 'eyes sunken in'],
            'sweating': ['perspiration', 'sweaty', 'diaphoresis', 'excessive sweating', 'sweating a lot'],
            'swelled_lymph_nodes': ['swollen lymph nodes', 'lymphadenopathy', 'enlarged lymph nodes', 'swollen glands', 'lumps in neck'],
            'swelling_joints': ['joint swelling', 'swollen joints', 'arthritic swelling', 'joint effusion', 'puffy joints'],
            'swelling_of_stomach': ['abdominal swelling', 'distended belly', 'swollen abdomen', 'gastric distension', 'bloated belly'],
            'swollen_blood_vessels': ['vascular swelling', 'engorged vessels', 'dilated veins', 'swollen veins'],
            'swollen_extremeties': ['limb swelling', 'swollen arms/legs', 'peripheral edema', 'swollen limbs'],
            'swollen_legs': ['leg edema', 'leg swelling', 'swollen feet and legs', 'puffy legs'],
            'throat_irritation': ['scratchy throat', 'throat irritation', 'raw throat', 'irritated throat'],
            'toxic_look_typhos': ['toxic appearance', 'typhoid state', 'looks very ill', 'severely ill appearance'],
            'ulcers_on_tongue': ['tongue ulcers', 'mouth ulcers', 'tongue sores', 'oral ulcers', 'sores on tongue'],
            'unsteadiness': ['unsteady gait', 'loss of balance', 'ataxia', 'staggering', 'walking unsteady'],
            'visual_disturbances': ['vision changes', 'visual problems', 'eyesight issues', 'seeing things'],
            'vomiting': ['throw up', 'puking', 'emesis', 'vomiting episodes', 'throwing up', 'vomiting repeatedly'],
            'watering_from_eyes': ['teary eyes', 'excessive tearing', 'watery eyes', 'epiphora', 'eyes watering'],
            'weakness_in_limbs': ['limb weakness', 'weak arms/legs', 'extremity weakness', 'weak limbs'],
            'weakness_of_one_body_side': ['hemiparesis', 'one side weakness', 'unilateral weakness', 'weak on one side'],
            'weight_gain': ['gaining weight', 'weight increase', 'putting on weight', 'getting heavier', 'weight gain'],
            'weight_loss': ['losing weight', 'weight decrease', 'unexplained weight loss', 'shedding pounds', 'getting thinner'],
            'yellow_crust_ooze': ['yellow oozing', 'purulent drainage', 'yellow discharge', 'yellow pus'],
            'yellow_urine': ['yellow pee', 'dark yellow urine', 'concentrated urine', 'yellow colored urine'],
            'yellowing_of_eyes': ['yellow eyes', 'icterus', 'scleral icterus', 'yellow sclera', 'eyes turned yellow'],
            'yellowish_skin': ['yellow skin', 'jaundice', 'yellow discoloration skin', 'icteric skin', 'skin turning yellow']
        }
        
        for symptom in self.symptom_columns:
            clean_name = symptom.replace('_', ' ')
            aliases[symptom] = [clean_name, symptom]
            
            # Add mappings from alias_map
            if symptom in alias_map:
                aliases[symptom].extend(alias_map[symptom])
            
            # Also check by clean name
            for key, values in alias_map.items():
                if clean_name == key or clean_name in key or key in clean_name:
                    aliases[symptom].extend(values)
            
            aliases[symptom] = list(set(aliases[symptom]))
        
        return aliases
    
    def _create_patterns(self):
        """Create regex patterns for symptom extraction"""
        patterns = {
            'duration': r'(since|from|for|past) (\w+|\d+\s*(days?|weeks?|hours?|months?))',
            'severity': r'(severe|mild|moderate|intense|excruciating|slight|extreme|bad|terrible|horrible)',
            'pain_type': r'(throbbing|sharp|dull|burning|stabbing|aching|constant|intermittent)',
            'location': r'(in my|on my|at the) (\w+)',
            'negation': r'(no |not |without |never |don\'t have |doesn\'t have )'
        }
        return patterns
    
    def extract_symptoms(self, text):
        """Extract symptoms from natural language text with fuzzy matching"""
        text = text.lower()
        found_symptoms = []
        
        # Direct matching with aliases
        for symptom, aliases in self.symptom_aliases.items():
            for alias in aliases:
                if alias.lower() in text:
                    if symptom not in found_symptoms:
                        found_symptoms.append(symptom)
                    break
        
        # Fuzzy matching for misspelled symptoms
        words = re.findall(r'\b\w+\b', text)
        for word in words:
            if len(word) > 3:
                matches = get_close_matches(word, [s.replace('_', ' ') for s in self.symptom_columns], n=1, cutoff=0.7)
                if matches:
                    for symptom in self.symptom_columns:
                        if matches[0] == symptom.replace('_', ' '):
                            if symptom not in found_symptoms:
                                found_symptoms.append(symptom)
        
        # Remove duplicates
        unique_symptoms = []
        for s in found_symptoms:
            if s not in unique_symptoms:
                unique_symptoms.append(s)
        
        return unique_symptoms
    
    def extract_context(self, text):
        """Extract additional context like duration, severity, etc."""
        text = text.lower()
        context = {
            'duration': None,
            'severity': None,
            'pain_type': None,
            'body_part': None,
            'negated': False
        }
        
        # Extract duration
        duration_match = re.search(self.patterns['duration'], text)
        if duration_match:
            context['duration'] = duration_match.group(0)
        
        # Extract severity
        severity_match = re.search(self.patterns['severity'], text)
        if severity_match:
            context['severity'] = severity_match.group(0)
        
        # Extract pain type
        pain_match = re.search(self.patterns['pain_type'], text)
        if pain_match:
            context['pain_type'] = pain_match.group(0)
        
        # Extract body part
        location_match = re.search(self.patterns['location'], text)
        if location_match:
            context['body_part'] = location_match.group(2)
        
        # Check for negation (symptoms user DOES NOT have)
        negation_match = re.search(self.patterns['negation'], text)
        if negation_match:
            context['negated'] = True
        
        return context
    
    def get_related_symptoms(self, symptom, limit=3):
        """Get symptoms related to a given symptom"""
        related_map = {
            'dark_urine': ['yellow_urine', 'yellowing_of_eyes', 'yellowish_skin', 'fatigue', 'loss_of_appetite', 'nausea'],
            'yellowing_of_eyes': ['yellowish_skin', 'dark_urine', 'fatigue', 'loss_of_appetite', 'nausea'],
            'yellowish_skin': ['yellowing_of_eyes', 'dark_urine', 'fatigue', 'loss_of_appetite'],
            'headache': ['nausea', 'dizziness', 'vomiting', 'blurred_and_distorted_vision', 'neck_pain'],
            'fever': ['chills', 'fatigue', 'cough', 'muscle_pain', 'sweating', 'dehydration'],
            'cough': ['fever', 'fatigue', 'breathlessness', 'phlegm', 'chest_pain', 'runny_nose'],
            'nausea': ['vomiting', 'dizziness', 'abdominal_pain', 'loss_of_appetite', 'diarrhoea'],
            'fatigue': ['headache', 'muscle_pain', 'dizziness', 'lack_of_concentration', 'sleepy'],
        }
        
        # Find related symptoms
        related = related_map.get(symptom, [])
        
        # Filter to existing symptoms
        result = [s for s in related if s in self.symptom_columns][:limit]
        
        return result
    
    def extract_all(self, text):
        """Extract everything - symptoms and context"""
        return {
            'symptoms': self.extract_symptoms(text),
            'context': self.extract_context(text)
        }