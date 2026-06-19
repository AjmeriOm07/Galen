"""
Conversation Engine - Natural doctor-patient conversation flow
"""
import random

class ConversationEngine:
    def __init__(self, symptom_matcher):
        self.matcher = symptom_matcher
        self.reset()
    
    def reset(self):
        """Reset conversation state"""
        self.collected_symptoms = []
        self.asked_questions = []
        self.current_focus = None
        self.greeted = False
        self.ready_for_prediction = False
        self.question_count = 0
        self.awaiting_diagnosis = False
        self.duration_asked = False
        self.severity_asked = False
    
    def get_greeting(self):
        """Doctor's initial greeting - Natural and friendly"""
        greetings = [
            "Hello! I'm Dr. Galen. How are you feeling today? Tell me what's been going on.",
            "Hi there. How has your day been? What brings you in today?",
            "Good to see you. How are you feeling? Take your time and tell me what's troubling you.",
            "Hey, nice to meet you. How's your day going? I'm here to listen to your concerns."
        ]
        self.greeted = True
        self.question_count = 0
        return random.choice(greetings)
    
    def process_message(self, message):
        """Process user message and generate response"""
        message_lower = message.lower()
        
        # Check if user wants to finish/diagnose
        finish_keywords = [
            "that's it", "that is it", "diagnose me", "what do i have", 
            "predict", "tell me what i have", "make diagnosis", 
            "that's all", "no more", "finish", "done", "go ahead",
            "yes diagnose", "proceed", "diagnose"
        ]
        
        if any(kw in message_lower for kw in finish_keywords):
            self.ready_for_prediction = True
            return {
                'type': 'ready',
                'message': "Thank you for sharing all the information. Let me analyze your symptoms carefully and provide my assessment.",
                'quick_replies': None
            }
        
        # Extract symptoms from message
        new_symptoms = self.matcher.extract_symptoms(message)
        
        # Add new symptoms
        for symptom in new_symptoms:
            if symptom not in self.collected_symptoms:
                self.collected_symptoms.append(symptom)
        
        self.question_count += 1
        
        # If we have enough symptoms (2 or more), suggest finishing after some questions
        if len(self.collected_symptoms) >= 2 and self.question_count >= 3 and not self.awaiting_diagnosis:
            self.awaiting_diagnosis = True
            return {
                'type': 'question',
                'message': f"I've noted your symptoms: {', '.join(self.collected_symptoms[:5]).replace('_', ' ')}.\n\nWould you like me to proceed with the diagnosis, or is there anything else you'd like to add?",
                'quick_replies': ['Proceed with diagnosis', 'Add more symptoms', 'That\'s all']
            }
        
        # Generate appropriate response
        return self._generate_response(new_symptoms)
    
    def _generate_response(self, new_symptoms):
        """Generate intelligent follow-up response"""
        
        # Case 1: No symptoms found at all
        if not new_symptoms and not self.collected_symptoms:
            return {
                'type': 'question',
                'message': "I didn't quite catch that. Could you describe how you're feeling? For example:\n• Headache\n• Fever\n• Cough\n• Stomach pain\n• Fatigue\n• Nausea",
                'quick_replies': ['Headache', 'Fever', 'Cough', 'Stomach pain', 'Fatigue', 'Nausea']
            }
        
        # Case 2: First symptoms found - ask about duration
        if new_symptoms and not self.duration_asked:
            self.duration_asked = True
            return {
                'type': 'question',
                'message': f"I see you're experiencing {self._format_symptoms(new_symptoms)}. How long have you been having these symptoms?",
                'quick_replies': ['Today', 'Yesterday', '2-3 days', 'Over a week', 'Not sure']
            }
        
        # Case 3: Ask about severity (if not asked)
        if self.collected_symptoms and not self.severity_asked:
            self.severity_asked = True
            return {
                'type': 'question',
                'message': f"Thank you. On a scale of 1-10, how severe are your symptoms? (1 = very mild, 10 = very severe)",
                'quick_replies': ['1-2 (Mild)', '3-4 (Moderate)', '5-6 (Quite severe)', '7-8 (Very severe)', '9-10 (Extreme)']
            }
        
        # Case 4: Ask about related symptoms (based on first symptom)
        if self.current_focus is None and self.collected_symptoms:
            self.current_focus = self.collected_symptoms[0]
        
        if self.current_focus and self.current_focus not in self.asked_questions and len(self.collected_symptoms) < 4:
            related = self.matcher.get_related_symptoms(self.current_focus)
            if related:
                self.asked_questions.append(self.current_focus)
                related_formatted = [r.replace('_', ' ') for r in related[:3]]
                return {
                    'type': 'question',
                    'message': f"Just to understand better, are you also experiencing any of these: {', '.join(related_formatted)}?",
                    'quick_replies': related_formatted + ['No, none of these', 'Not sure']
                }
        
        # Case 5: Ask if ready for diagnosis (fallback)
        if len(self.collected_symptoms) >= 1 and not self.awaiting_diagnosis:
            self.awaiting_diagnosis = True
            return {
                'type': 'question',
                'message': f"Thank you for all the information. I have noted your symptoms. Would you like me to proceed with the diagnosis now?",
                'quick_replies': ['Yes, proceed', 'Wait, one more thing', 'Proceed with diagnosis']
            }
        
        # Default: ask for more details
        return {
            'type': 'question',
            'message': "Can you tell me more about your symptoms? Any other discomfort you're feeling?",
            'quick_replies': ['Yes', 'That\'s all', 'Proceed with diagnosis']
        }
    
    def _format_symptoms(self, symptoms):
        """Format symptom list nicely for display"""
        formatted = [s.replace('_', ' ') for s in symptoms[:3]]
        if len(formatted) == 0:
            return "symptoms"
        elif len(formatted) == 1:
            return formatted[0]
        elif len(formatted) == 2:
            return f"{formatted[0]} and {formatted[1]}"
        else:
            return f"{', '.join(formatted[:-1])}, and {formatted[-1]}"
    
    def get_summary(self):
        """Get summary of collected symptoms"""
        return {
            'symptoms': self.collected_symptoms,
            'ready': self.ready_for_prediction or (len(self.collected_symptoms) >= 2 and self.question_count >= 3)
        }