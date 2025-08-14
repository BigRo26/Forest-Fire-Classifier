import React, { useState, useEffect } from 'react';
import { onAuthStateChanged } from 'firebase/auth';
import { auth } from './firebase';
import './App.css';
import ImageUpload from './components/ImageUpload';
import Header from './components/Header';
import Login from './components/Login';

function App() {
  const [classification, setClassification] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [user, setUser] = useState(null);
  const [authLoading, setAuthLoading] = useState(true);

  useEffect(() => {
    const unsubscribe = onAuthStateChanged(auth, (user) => {
      setUser(user);
      setAuthLoading(false);
    });

    return () => unsubscribe();
  }, []);

  const handleClassification = (result) => {
    setClassification(result);
  };

  const handleLoading = (loading) => {
    setIsLoading(loading);
  };

  const handleLogout = () => {
    setUser(null);
    setClassification(null);
  };

  if (authLoading) {
    return (
      <div className="loading-container">
        <div className="loading-spinner"></div>
        <p>Loading...</p>
      </div>
    );
  }

  if (!user) {
    return <Login onLogin={() => setUser(auth.currentUser)} />;
  }

  return (
    <div className="App">
      <Header user={user} onLogout={handleLogout} />
      <main className="main-content">
        <ImageUpload 
          onClassification={handleClassification}
          onLoading={handleLoading}
        />
        {isLoading && (
          <div className="loading-container">
            <div className="loading-spinner"></div>
            <p>Analyzing image with PyTorch model...</p>
          </div>
        )}
        {classification && (
          <div className={`result-container ${classification.classification === 'fire' ? 'fire-result' : 'no-fire-result'}`}>
            <h3>Classification Result:</h3>
            <div className="result-badge">
              {classification.classification === 'fire' ? '🔥 FIRE DETECTED' : '🌲 NO FIRE'}
            </div>
            
            {/* Confidence Display */}
            <div className="confidence-section">
              <h4>Confidence Score</h4>
              <div className="confidence-bar">
                <div 
                  className="confidence-fill" 
                  style={{ 
                    width: `${(classification.confidence * 100)}%`,
                    backgroundColor: classification.classification === 'fire' ? '#ff4444' : '#44aa44'
                  }}
                ></div>
                <span className="confidence-text">{Math.round(classification.confidence * 100)}%</span>
              </div>
            </div>

            {/* Detailed Probabilities */}
            {classification.probabilities && (
              <div className="probabilities-section">
                <h4>Class Probabilities</h4>
                <div className="probability-item">
                  <span className="probability-label">🔥 Fire:</span>
                  <span className="probability-value">{Math.round(classification.probabilities.fire * 100)}%</span>
                </div>
                <div className="probability-item">
                  <span className="probability-label">🌲 No Fire:</span>
                  <span className="probability-value">{Math.round(classification.probabilities.no_fire * 100)}%</span>
                </div>
              </div>
            )}

            {/* Model Information */}
            {classification.modelInfo && (
              <div className="model-info">
                <h4>Model Details</h4>
                <p><strong>Architecture:</strong> {classification.modelInfo.architecture}</p>
                <p><strong>Framework:</strong> {classification.modelInfo.framework}</p>
                <p><strong>Weights:</strong> {classification.modelInfo.weights}</p>
              </div>
            )}

            <p className="result-description">
              {classification.message}
            </p>
          </div>
        )}
      </main>
    </div>
  );
}

export default App;
