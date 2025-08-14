@echo off
echo Creating .env file with your Firebase credentials...
echo.

echo REACT_APP_FIREBASE_API_KEY=AIzaSyClNdQC4Pgkt2PKazlnyUiPnDxBqFSwTlE > .env
echo REACT_APP_FIREBASE_AUTH_DOMAIN=Forest-Fire-Detection.firebaseapp.com >> .env
echo REACT_APP_FIREBASE_PROJECT_ID=forest-fire-detection-cf1e8 >> .env
echo REACT_APP_FIREBASE_STORAGE_BUCKET=forest-fire-detection-cf1e8.appspot.com >> .env
echo REACT_APP_FIREBASE_MESSAGING_SENDER_ID=640519717396 >> .env
echo REACT_APP_FIREBASE_APP_ID=1:640519717396:web:9253a9e2bff3f482165d01 >> .env

echo.
echo .env file created successfully!
echo Your Firebase credentials are now secure and won't be committed to Git.
echo.
pause
