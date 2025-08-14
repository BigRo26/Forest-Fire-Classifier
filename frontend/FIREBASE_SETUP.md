# Firebase Authentication Setup

This guide will help you set up Firebase Authentication for the Forest Fire Classifier application.

## Step 1: Create a Firebase Project

1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Click "Create a project" or select an existing project
3. Enter a project name (e.g., "forest-fire-classifier")
4. Follow the setup wizard (you can disable Google Analytics if not needed)

## Step 2: Enable Authentication

1. In your Firebase project console, click on "Authentication" in the left sidebar
2. Click "Get started"
3. Go to the "Sign-in method" tab
4. Enable "Email/Password" authentication
5. Click "Save"

## Step 3: Get Firebase Configuration

1. In your Firebase project console, click on the gear icon (⚙️) next to "Project Overview"
2. Select "Project settings"
3. Scroll down to "Your apps" section
4. Click the web icon (</>)
5. Register your app with a nickname (e.g., "forest-fire-classifier-web")
6. Copy the Firebase configuration object

## Step 4: Set Up Environment Variables (SECURE METHOD)

1. **Create a `.env` file** in your `frontend` directory:
   ```bash
   # In the frontend folder, create a file named .env
   touch .env  # On Windows: echo. > .env
   ```

2. **Add your Firebase credentials** to the `.env` file:
   ```env
   REACT_APP_FIREBASE_API_KEY=your-actual-api-key
   REACT_APP_FIREBASE_AUTH_DOMAIN=your-project.firebaseapp.com
   REACT_APP_FIREBASE_PROJECT_ID=your-actual-project-id
   REACT_APP_FIREBASE_STORAGE_BUCKET=your-project.appspot.com
   REACT_APP_FIREBASE_MESSAGING_SENDER_ID=your-actual-messaging-sender-id
   REACT_APP_FIREBASE_APP_ID=your-actual-app-id
   ```

3. **Important**: The `.env` file is already in `.gitignore`, so it won't be committed to Git

## Step 5: Install Dependencies

Run the following command in your frontend directory:

```bash
npm install
```

## Step 6: Test the Application

1. Start your frontend application: `npm start`
2. You should now see a login screen
3. Create a new account or sign in with existing credentials
4. After authentication, you'll be redirected to the main application

## Security Features

- **Environment Variables**: Firebase credentials are stored in `.env` file (not committed to Git)
- **Git Protection**: `.gitignore` prevents sensitive files from being uploaded
- **Example File**: `env.example` shows the required format without real credentials

## Features

- **User Registration**: New users can create accounts with email/password
- **User Login**: Existing users can sign in
- **Protected Routes**: The main application is only accessible to authenticated users
- **User Session Management**: Automatic login state persistence
- **Logout Functionality**: Users can sign out from the header

## Security Notes

- Firebase handles all authentication securely
- Passwords are never stored in plain text
- User sessions are managed by Firebase Auth
- The backend API remains unchanged and doesn't require authentication (you can add this later if needed)
- **Your Firebase credentials are now secure and won't be exposed in your GitHub repository**

## Troubleshooting

- **"Firebase: Error (auth/invalid-api-key)"**: Check that your `.env` file exists and has correct values
- **"Firebase: Error (auth/operation-not-allowed)"**: Make sure Email/Password authentication is enabled in Firebase Console
- **"Firebase: Error (auth/network-request-failed)"**: Check your internet connection and Firebase project status
- **"process.env.REACT_APP_FIREBASE_API_KEY is undefined"**: Make sure your `.env` file is in the `frontend` directory and has the correct variable names

## Next Steps

After setting up authentication, you might want to:
1. Add password reset functionality
2. Implement email verification
3. Add social authentication (Google, Facebook, etc.)
4. Secure your backend API with Firebase Auth tokens
5. Add user profile management

## For GitHub Deployment

When you push to GitHub:
1. ✅ Your `.env` file will NOT be uploaded (protected by `.gitignore`)
2. ✅ Only `env.example` will be visible (safe to share)
3. ✅ Other developers can copy `env.example` to `.env` and add their own credentials
4. ✅ Your Firebase project remains secure
