import { auth, db } from './firebase-config.js';
import { collection, addDoc, query, where, orderBy, onSnapshot, serverTimestamp } from "https://www.gstatic.com/firebasejs/10.9.0/firebase-firestore.js";

function renderComment(docData) {
    const time = docData.timestamp ? new Date(docData.timestamp.toDate()).toLocaleString() : 'Justo ahora';
    const isMe = auth.currentUser && auth.currentUser.email === docData.authorEmail;
    
    return `
        <div style="background: ${isMe ? 'var(--bg-card)' : '#f3f4f6'}; padding: 10px; border-radius: 8px; font-size: 14px; border: 1px solid ${isMe ? 'var(--border-color)' : '#e5e7eb'};">
            <div style="display: flex; justify-content: space-between; margin-bottom: 4px; font-size: 12px; color: var(--text-secondary);">
                <strong>${docData.authorName || docData.authorEmail}</strong>
                <span>${time}</span>
            </div>
            <div style="color: var(--text-primary); white-space: pre-wrap;">${docData.text}</div>
        </div>
    `;
}

function loadChatForPhase(phaseId) {
    const q = query(
        collection(db, "proposal_notes"),
        where("phase", "==", String(phaseId))
    );

    const messagesDiv = document.getElementById(`chat-messages-${phaseId}`);
    
    onSnapshot(q, (snapshot) => {
        let html = "";
        
        // Extraer a array para ordenar en memoria y evitar requerir Composite Index en Firebase
        let docs = [];
        snapshot.forEach((doc) => {
            docs.push(doc.data());
        });
        
        docs.sort((a, b) => {
            const timeA = a.timestamp ? a.timestamp.toMillis() : Date.now();
            const timeB = b.timestamp ? b.timestamp.toMillis() : Date.now();
            return timeA - timeB;
        });
        
        docs.forEach((data) => {
            html += renderComment(data);
        });
        
        if (messagesDiv) {
            messagesDiv.innerHTML = html || '<div style="color: var(--text-secondary); font-size: 13px; font-style: italic;">No hay notas todavía.</div>';
            messagesDiv.scrollTop = messagesDiv.scrollHeight;
        }
    });
}

function sendNote(phaseId) {
    const input = document.getElementById(`comment-${phaseId}`);
    const text = input.value.trim();
    
    if (!text) return;
    
    if (!auth.currentUser) {
        alert("Debes iniciar sesión para comentar.");
        return;
    }

    const btn = document.querySelector(`.btn-send-note[data-phase="${phaseId}"]`);
    btn.disabled = true;
    btn.innerHTML = '...';

    addDoc(collection(db, "proposal_notes"), {
        phase: String(phaseId),
        text: text,
        authorName: auth.currentUser.displayName,
        authorEmail: auth.currentUser.email,
        timestamp: serverTimestamp()
    }).then(() => {
        input.value = "";
        btn.disabled = false;
        btn.innerHTML = 'Enviar';
    }).catch((error) => {
        console.error("Error adding document: ", error);
        alert("Error al enviar la nota.");
        btn.disabled = false;
        btn.innerHTML = 'Enviar';
    });
}

// Setup when DOM is ready
document.addEventListener("DOMContentLoaded", () => {
    // Escuchar auth state para cargar chats solo cuando estemos seguros de que hay un usuario
    auth.onAuthStateChanged((user) => {
        if (user) {
            for (let i = 1; i <= 4; i++) {
                loadChatForPhase(i);
            }
        }
    });

    // Attach click events
    document.querySelectorAll('.btn-send-note').forEach(btn => {
        btn.addEventListener('click', (e) => {
            const phaseId = e.target.getAttribute('data-phase');
            sendNote(phaseId);
        });
    });
});
