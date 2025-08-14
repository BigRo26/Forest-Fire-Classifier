from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from werkzeug.utils import secure_filename
import logging
from model import predict
import torch

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['UPLOAD_FOLDER'] = 'uploads'

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Enable CORS for React frontend
CORS(app, origins=['http://localhost:3000', 'http://127.0.0.1:3000'])

# Allowed file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp'}

def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'message': 'Forest Fire Classifier API is running',
        'version': '1.0.0',
        'model': 'PyTorch Inception V3 (forest_fire_classifier.pth)'
    })

@app.route('/api/classify', methods=['POST'])
def classify_image():
    """Classify uploaded forest image for fire detection using PyTorch model"""
    try:
        # Check if image file is present
        if 'image' not in request.files:
            return jsonify({'error': 'No image file provided'}), 400
        
        file = request.files['image']
        
        # Check if file was selected
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        # Check file extension
        if not allowed_file(file.filename):
            return jsonify({'error': 'Invalid file type. Allowed: PNG, JPG, JPEG, GIF, BMP'}), 400
        
        # Secure filename and save
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        logger.info(f"Processing image: {filename} using PyTorch Inception V3 model")
        
        try:
            # Use PyTorch model from model.py to make prediction
            logger.info("Calling PyTorch model.predict() function...")
            pred_label, pred_prob = predict(filepath)
            
            # Clean up uploaded file
            os.remove(filepath)
            
            # Convert prediction to label
            if pred_label == "fire":
                classification = "fire"
            else:
                classification = "no fire"
            
            # Get confidence from the highest probability
            confidence = float(torch.max(pred_prob).item())
            
            # Get individual class probabilities
            fire_prob = float(pred_prob[0][0].item())  # Probability for "fire" class
            no_fire_prob = float(pred_prob[0][1].item())  # Probability for "no fire" class
            
            logger.info(f"PyTorch model prediction: {pred_label} (confidence: {confidence:.3f})")
            logger.info(f"Class probabilities - Fire: {fire_prob:.3f}, No Fire: {no_fire_prob:.3f}")
            
            return jsonify({
                'classification': classification,
                'confidence': round(confidence, 3),
                'message': f"Image classified as: {classification}",
                'raw_prediction': pred_label,
                'probabilities': {
                    'fire': round(fire_prob, 3),
                    'no_fire': round(no_fire_prob, 3)
                },
                'model_info': {
                    'architecture': 'Inception V3',
                    'weights': 'forest_fire_classifier.pth',
                    'framework': 'PyTorch'
                }
            })
            
        except Exception as e:
            # Clean up file on error
            if os.path.exists(filepath):
                os.remove(filepath)
            logger.error(f"PyTorch model classification error: {str(e)}")
            return jsonify({'error': 'Failed to process image with PyTorch model'}), 500
            
    except Exception as e:
        logger.error(f"API error: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/health', methods=['GET'])
def health():
    """Health check for API endpoints"""
    return jsonify({
        'status': 'healthy',
        'endpoints': {
            'classify': '/api/classify',
            'health': '/api/health'
        },
        'model_status': 'PyTorch Inception V3 loaded and ready'
    })

@app.errorhandler(413)
def too_large(e):
    """Handle file too large error"""
    return jsonify({'error': 'File too large. Maximum size is 16MB.'}), 413

@app.errorhandler(500)
def internal_error(e):
    """Handle internal server error"""
    logger.error(f"Internal server error: {e}")
    return jsonify({'error': 'Internal server error occurred'}), 500

if __name__ == '__main__':
    logger.info("Starting Forest Fire Classifier Flask App...")
    logger.info("Using PyTorch Inception V3 model from forest_fire_classifier.pth")
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
    
