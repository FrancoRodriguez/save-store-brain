import { auth } from './firebase-config.js';
import { onAuthStateChanged, signOut } from "https://www.gstatic.com/firebasejs/10.9.0/firebase-auth.js";

const ALLOWED_EMAILS = [
    "rodriguezcfranco@gmail.com",
    "rdgbalassi@gmail.com",
    "franco.rodriguez@petscreening.com"
];

// Comprobar estado de autenticación en cada carga de página
onAuthStateChanged(auth, (user) => {
    const isLoginPage = window.location.pathname.endsWith('login.html');

    if (user) {
        // Usuario logueado
        if (ALLOWED_EMAILS.includes(user.email)) {
            // Email válido
            if (isLoginPage) {
                // Si está en login y es válido, redirigir al index
                window.location.href = 'index.html';
            }
            // Si está en otra página, dejarlo pasar.
        } else {
            // Email NO válido
            alert("Acceso denegado: Tu correo electrónico (" + user.email + ") no está autorizado para ver esta maqueta.");
            signOut(auth).then(() => {
                if (!isLoginPage) {
                    window.location.href = 'login.html';
                }
            });
        }
    } else {
        // No hay usuario logueado
        if (!isLoginPage) {
            window.location.href = 'login.html';
        }
    }
});

// Exponer la función de logout globalmente si se necesita en un botón
window.logout = () => {
    signOut(auth);
};
