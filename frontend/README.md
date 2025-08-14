# Foresty - Forest Fire Classifier

A modern React-based web application for detecting fire presence in forest images. The application features a beautiful light green theme and intuitive user interface for image upload and classification.

## Features

- 🌲 **Beautiful UI**: Light green theme with modern design
- 📷 **Image Upload**: Drag and drop or click to browse functionality
- 🔍 **Real-time Analysis**: Instant classification results
- 📱 **Responsive Design**: Works on all device sizes
- 🎨 **Modern Animations**: Smooth transitions and hover effects

## Screenshots

The application features:
- Header with "Foresty" title and forest/fire icons
- Image upload area with drag and drop support
- Preview of selected images
- Classification results with visual indicators
- Loading states and smooth animations

## Technology Stack

- **Frontend**: React 18
- **Styling**: CSS3 with modern features
- **Build Tool**: Create React App
- **Icons**: Emoji icons for visual appeal

## Getting Started

### Prerequisites

- Node.js (version 14 or higher)
- npm or yarn package manager

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd forest-fire-classifier
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm start
```

4. Open your browser and navigate to `http://localhost:3000`

### Building for Production

To create a production build:

```bash
npm run build
```

The build files will be created in the `build` folder.

## Usage

1. **Upload Image**: Click on the upload area or drag and drop an image file
2. **Preview**: View the selected image before analysis
3. **Analyze**: Click the "Analyze Image" button to classify the image
4. **Results**: View the classification result (Fire detected or No fire)
5. **Clear**: Use the clear button to remove the current image and start over

## Current Implementation

The current version includes:
- ✅ Complete React frontend with modern UI
- ✅ Image upload and preview functionality
- ✅ Drag and drop support
- ✅ Responsive design for mobile and desktop
- ✅ Light green theme throughout the application
- ✅ Mock classification system (random results)

## Future Enhancements

To make this a production-ready application, consider adding:
- 🔗 **Backend Integration**: Connect to a real ML model API
- 🖼️ **Image Processing**: Add image preprocessing capabilities
- 📊 **Confidence Scores**: Show classification confidence levels
- 📈 **Analytics**: Track usage and classification accuracy
- 🔐 **Authentication**: User accounts and history
- 📱 **Mobile App**: Native mobile application

## API Integration

To integrate with a real ML model, replace the mock classification in `ImageUpload.js`:

```javascript
// Replace this mock code:
setTimeout(() => {
  const randomResult = Math.random() > 0.5 ? 'fire' : 'no fire';
  onClassification(randomResult);
  onLoading(false);
}, 2000);

// With actual API call:
try {
  const formData = new FormData();
  formData.append('image', selectedImage);
  
  const response = await fetch('/api/classify', {
    method: 'POST',
    body: formData
  });
  
  const result = await response.json();
  onClassification(result.classification);
} catch (error) {
  console.error('Classification failed:', error);
  alert('Classification failed. Please try again.');
} finally {
  onLoading(false);
}
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

For questions or support, please open an issue in the repository.
