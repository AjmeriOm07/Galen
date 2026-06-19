#!/usr/bin/env python
"""
GALEN AI - Startup Script
Run: python run.py
"""

import os
import sys

# Check if model files exist
model_files = [
    'models/disease_model.pkl',
    'models/disease_encoder.pkl',
    'models/symptom_columns.pkl'
]

missing = [f for f in model_files if not os.path.exists(f)]

if missing:
    print("\n" + "="*60)
    print("❌ ERROR: Model files not found!")
    print("="*60)
    print("\nPlease train your model first in Jupyter:")
    print("  1. Open your training notebook")
    print("  2. Run the model training cell")
    print("  3. Copy the 'models' folder to this directory")
    print("\nMissing files:")
    for f in missing:
        print(f"   • {f}")
    print("="*60)
    sys.exit(1)

# Start the server
print("\n🚀 Starting Galen AI Server...")
print("📍 Open: http://127.0.0.1:5000")
print("💡 Type 'quit' to exit\n")

# Import and run app
from backend.app import app

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)