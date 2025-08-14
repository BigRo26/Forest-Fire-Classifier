# Shared constants for Forest Fire Classifier

# API Configuration
API_BASE_URL = "http://localhost:5000"
API_ENDPOINTS = {
    'classify': '/api/classify',
    'health': '/api/health'
}

# File Configuration
ALLOWED_IMAGE_EXTENSIONS = {'.png', '.jpg', '.jpeg', '.gif', '.bmp'}
MAX_FILE_SIZE_MB = 16
MAX_FILE_SIZE_BYTES = MAX_FILE_SIZE_MB * 1024 * 1024

# Classification Results
CLASSIFICATION_CLASSES = ['no fire', 'fire']
CLASSIFICATION_LABELS = {
    'no fire': '🌲 NO FIRE',
    'fire': '🔥 FIRE DETECTED'
}

# Image Processing
TARGET_IMAGE_SIZE = (224, 224)
IMAGE_CHANNELS = 3

# UI Configuration
THEME_COLORS = {
    'primary': '#4CAF50',
    'secondary': '#90EE90',
    'success': '#45a049',
    'danger': '#ff6b6b',
    'warning': '#ff9800',
    'info': '#2196F3'
}

# Error Messages
ERROR_MESSAGES = {
    'file_too_large': f'File size must be less than {MAX_FILE_SIZE_MB}MB',
    'invalid_file_type': f'Invalid file type. Allowed: {", ".join(ALLOWED_IMAGE_EXTENSIONS)}',
    'no_file_selected': 'No file selected',
    'classification_failed': 'Failed to classify image. Please try again.',
    'server_error': 'Server error occurred. Please try again later.'
}


