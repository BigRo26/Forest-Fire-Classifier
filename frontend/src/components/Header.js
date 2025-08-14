import React from 'react';
import { signOut } from 'firebase/auth';
import { auth } from '../firebase';
import './Header.css';

const Header = ({ user, onLogout }) => {
  const handleLogout = async () => {
    try {
      await signOut(auth);
      onLogout();
    } catch (error) {
      console.error('Error signing out:', error);
    }
  };

  return (
    <header className="header">
      <div className="header-content">
        <div className="header-left">
          <h1>🌲 Forest Fire Classifier</h1>
          <p>AI-powered forest fire detection using PyTorch</p>
        </div>
        {user && (
          <div className="header-right">
            <div className="user-info">
              <span className="user-email">{user.email}</span>
              <button onClick={handleLogout} className="logout-button">
                Logout
              </button>
            </div>
          </div>
        )}
      </div>
    </header>
  );
};

export default Header;
