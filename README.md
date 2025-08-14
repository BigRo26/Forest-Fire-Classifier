# Foresty - Forest Fire Classifier

A full-stack web application for detecting fire presence in forest images. Features a React frontend with a beautiful light green theme and a Flask backend with ML classification capabilities.

## 🏗️ Project Structure

```
Forest Fire Classifier/
├── frontend/                    # React frontend
│   ├── public/                 # Static files
│   ├── src/                    # React components
│   ├── package.json            # Frontend dependencies
│   └── README.md               # Frontend documentation
├── backend/                     # Flask backend
│   ├── app.py                  # Main Flask application
│   ├── requirements.txt        # Python dependencies
│   ├── models/                 # ML models and image processing
│   ├── routes/                 # API endpoints
│   ├── utils/                  # Helper functions
│   ├── uploads/                # Temporary image storage
│   └── tests/                  # Backend tests
├── shared/                     # Shared utilities/config
│   └── constants.py            # Common constants
└── README.md                   # This file
```

## ✨ Features

- 🌲 **Beautiful UI**: Light green theme with modern design
- 📷 **Image Upload**: Drag and drop or click to browse functionality
- 🔍 **Real-time Analysis**: Instant classification results via Flask API
- 📱 **Responsive Design**: Works on all device sizes
- 🎨 **Modern Animations**: Smooth transitions and hover effects
- 🚀 **Flask Backend**: RESTful API with ML classification
- 🖼️ **Image Processing**: Advanced image preprocessing capabilities

## 🚀 Quick Start

### Prerequisites

- **Frontend**: Node.js (version 14 or higher)
- **Backend**: Python 3.8 or higher
- **Package Managers**: npm and pip

### 1. Clone and Setup

```bash
git clone <repository-url>
cd forest-fire-classifier
```

### 2. Frontend Setup

```bash
cd frontend
npm install
npm start
```

The React app will run at `http://localhost:3000`

### 3. Backend Setup

```bash
cd backend
pip install -r requirements.txt
python app.py
```

The Flask API will run at `http://localhost:5000`

### 4. Test the Application

1. Open `http://localhost:3000` in your browser
2. Upload a forest image
3. Click "Analyze Image" to get classification results

## 🔧 Development

### Frontend Development

```bash
cd frontend
npm start          # Start development server
npm run build      # Build for production
npm test           # Run tests
```

### Backend Development

```bash
cd backend
python app.py      # Start Flask development server
python -m pytest  # Run tests (when implemented)
```

### API Endpoints

- `GET /` - Health check
- `GET /api/health` - API health status
- `POST /api/classify` - Image classification endpoint

## 🧠 ML Model Integration

The current implementation includes:

- **Mock Classifier**: Basic classification for development
- **Image Processor**: Image preprocessing and validation
- **Extensible Architecture**: Easy to integrate real ML models

### To Integrate a Real ML Model:

1. Replace `backend/models/classifier.py` with your model
2. Update `backend/models/image_processor.py` for your model's requirements
3. Add model files to `backend/models/` directory

## 🚀 Deployment

### Frontend Deployment

```bash
cd frontend
npm run build
# Deploy build/ folder to CDN (Netlify, Vercel, etc.)
```

### Backend Deployment

```bash
cd backend
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:create_app()
# Deploy to cloud platform (Heroku, AWS, etc.)
```

## 🧪 Testing

### Frontend Tests

```bash
cd frontend
npm test
```

### Backend Tests

```bash
cd backend
python -m pytest
```

## 📁 File Organization

- **Frontend**: React components, styling, and user interface
- **Backend**: Flask API, ML models, and business logic
- **Shared**: Common constants and utilities
- **Uploads**: Temporary image storage (auto-cleaned)

## 🔒 Security Features

- File type validation
- File size limits (16MB max)
- Secure filename handling
- CORS configuration for development
- Input validation and sanitization

## 🚧 Current Status

- ✅ **Frontend**: Complete React application with modern UI
- ✅ **Backend**: Flask API with basic structure
- ✅ **Image Processing**: Basic image preprocessing
- ✅ **Mock Classification**: Development-ready classification
- 🔄 **ML Integration**: Ready for real model integration
- 🔄 **Testing**: Basic structure, needs implementation

## 🎯 Next Steps

1. **Integrate Real ML Model**: Replace mock classifier with trained model
2. **Add Authentication**: User accounts and result history
3. **Implement Testing**: Comprehensive test coverage
4. **Add Monitoring**: Logging and performance metrics
5. **Deploy to Production**: Cloud deployment and CI/CD

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🆘 Support

For questions or support:
- Open an issue in the repository
- Check the documentation in each folder
- Review the API endpoints in `backend/routes/`
