import React, { useState, useRef } from 'react';
import './ImageUpload.css';

const ImageUpload = ({ onClassification, onLoading }) => {
  const [dragActive, setDragActive] = useState(false);
  const [selectedImage, setSelectedImage] = useState(null);
  const [previewUrl, setPreviewUrl] = useState(null);
  const fileInputRef = useRef(null);

  const handleDrag = (e) => {
    e.preventDefault();
    e.stopPropagation();
    if (e.type === "dragenter" || e.type === "dragover") {
      setDragActive(true);
    } else if (e.type === "dragleave") {
      setDragActive(false);
    }
  };

  const handleDrop = (e) => {
    e.preventDefault();
    e.stopPropagation();
    setDragActive(false);
    
    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      handleFile(e.dataTransfer.files[0]);
    }
  };

  const handleFileInput = (e) => {
    if (e.target.files && e.target.files[0]) {
      handleFile(e.target.files[0]);
    }
  };

  const handleFile = (file) => {
    if (file.type.startsWith('image/')) {
      setSelectedImage(file);
      const reader = new FileReader();
      reader.onload = (e) => {
        setPreviewUrl(e.target.result);
      };
      reader.readAsDataURL(file);
    } else {
      alert('Please select an image file.');
    }
  };

  const handleSubmit = async () => {
    if (!selectedImage) {
      alert('Please select an image first.');
      return;
    }

    onLoading(true);
    
    try {
      // Create FormData for file upload
      const formData = new FormData();
      formData.append('image', selectedImage);

      // Make API call to Flask backend
      const response = await fetch('http://localhost:5000/api/classify', {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const result = await response.json();
      
      // Pass the complete result including confidence to parent component
      onClassification({
        classification: result.classification,
        confidence: result.confidence,
        probabilities: result.probabilities,
        message: result.message,
        modelInfo: result.model_info
      });
      
    } catch (error) {
      console.error('Error classifying image:', error);
      alert('Error analyzing image. Please try again.');
    } finally {
      onLoading(false);
    }
  };

  const clearImage = () => {
    setSelectedImage(null);
    setPreviewUrl(null);
    onClassification(null);
  };

  return (
    <div className="image-upload-container">
      <div className="upload-section">
        <h2>Upload Forest Image</h2>
        <p>Drag and drop an image or click to browse</p>
        
        <div
          className={`upload-area ${dragActive ? 'drag-active' : ''} ${previewUrl ? 'has-image' : ''}`}
          onDragEnter={handleDrag}
          onDragLeave={handleDrag}
          onDragOver={handleDrag}
          onDrop={handleDrop}
          onClick={() => fileInputRef.current?.click()}
        >
          {previewUrl ? (
            <div className="image-preview">
              <img src={previewUrl} alt="Preview" />
              <div className="image-overlay">
                <button className="change-image-btn" onClick={(e) => e.stopPropagation()}>
                  Change Image
                </button>
              </div>
            </div>
          ) : (
            <div className="upload-placeholder">
              <div className="upload-icon">📷</div>
              <p>Click to select or drag image here</p>
              <span className="file-types">Supports: JPG, PNG, GIF</span>
            </div>
          )}
          
          <input
            ref={fileInputRef}
            type="file"
            accept="image/*"
            onChange={handleFileInput}
            style={{ display: 'none' }}
          />
        </div>

        {selectedImage && (
          <div className="file-info">
            <p><strong>Selected:</strong> {selectedImage.name}</p>
            <p><strong>Size:</strong> {(selectedImage.size / 1024 / 1024).toFixed(2)} MB</p>
          </div>
        )}

        <div className="action-buttons">
          {selectedImage && (
            <>
              <button className="analyze-btn" onClick={handleSubmit}>
                🔍 Analyze Image
              </button>
              <button className="clear-btn" onClick={clearImage}>
                🗑️ Clear
              </button>
            </>
          )}
        </div>
      </div>
    </div>
  );
};

export default ImageUpload;
