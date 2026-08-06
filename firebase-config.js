import { initializeApp } from "https://www.gstatic.com/firebasejs/10.9.0/firebase-app.js";
import { getAuth, GoogleAuthProvider } from "https://www.gstatic.com/firebasejs/10.9.0/firebase-auth.js";
import { getFirestore } from "https://www.gstatic.com/firebasejs/10.9.0/firebase-firestore.js";

const firebaseConfig = {
    apiKey: "AIzaSyCKO5io5QaNIQ5uGf4oJTVUurIcDWGAmks",
    authDomain: "save-store-brain.firebaseapp.com",
    projectId: "save-store-brain",
    storageBucket: "save-store-brain.firebasestorage.app",
    messagingSenderId: "361246282711",
    appId: "1:361246282711:web:487bf3d0eb667ca86af192",
    measurementId: "G-XBNPP9H8MK"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const provider = new GoogleAuthProvider();
const db = getFirestore(app);

export { auth, provider, db };
