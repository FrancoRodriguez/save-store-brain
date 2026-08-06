import { auth, db } from './firebase-config.js';
import { collection, addDoc, updateDoc, deleteDoc, doc, query, where, onSnapshot, serverTimestamp } from "https://www.gstatic.com/firebasejs/10.9.0/firebase-firestore.js";

// Variable global para rastrear si estamos editando una nota
window.editingNoteId = null;

function renderComment(docData, docId) {
    const time = docData.timestamp ? new Date(docData.timestamp.toMillis()).toLocaleString() : 'Justo ahora';
    const isMe = auth.currentUser && auth.currentUser.email === docData.authorEmail;
    
    // Si es mi nota, muestro un botón de editar y otro de borrar
    const editButton = isMe ? 
        `<button onclick="window.startEditNote('${docId}', '${docData.phase}')" style="background:none; border:none; color: var(--primary-color); cursor: pointer; font-size: 12px; text-decoration: underline;">Editar</button>` : '';
    const deleteButton = isMe ?
        `<button onclick="window.deleteNote('${docId}', '${docData.phase}')" style="background:none; border:none; color: #ef4444; cursor: pointer; font-size: 12px; text-decoration: underline;">Borrar</button>` : '';

    return `
        <div style="background: ${isMe ? 'var(--bg-card)' : '#f3f4f6'}; padding: 10px; border-radius: 8px; font-size: 14px; border: 1px solid ${isMe ? 'var(--border-color)' : '#e5e7eb'}; margin-bottom: 8px;" id="note-${docId}">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px; font-size: 12px; color: var(--text-secondary);">
                <strong>${docData.authorName || docData.authorEmail}</strong>
                <div style="display: flex; gap: 8px; align-items: center;">
                    ${editButton}
                    ${deleteButton}
                    <span>${time}</span>
                </div>
            </div>
            <div id="text-${docId}" style="color: var(--text-primary); white-space: pre-wrap;">${docData.text}</div>
        </div>
    `;
}

// Función global para borrar con modal personalizado
window.deleteNote = (docId, phaseId) => {
    // Crear el overlay del modal
    const overlay = document.createElement('div');
    overlay.style.position = 'fixed';
    overlay.style.top = '0';
    overlay.style.left = '0';
    overlay.style.width = '100%';
    overlay.style.height = '100%';
    overlay.style.backgroundColor = 'rgba(0, 0, 0, 0.5)';
    overlay.style.display = 'flex';
    overlay.style.justifyContent = 'center';
    overlay.style.alignItems = 'center';
    overlay.style.zIndex = '9999';
    overlay.style.fontFamily = "'Inter', sans-serif";

    // Crear la caja del modal
    const modal = document.createElement('div');
    modal.style.backgroundColor = 'var(--bg-card)';
    modal.style.padding = '24px';
    modal.style.borderRadius = '12px';
    modal.style.boxShadow = '0 10px 25px rgba(0, 0, 0, 0.2)';
    modal.style.maxWidth = '400px';
    modal.style.width = '90%';
    modal.style.border = '1px solid var(--border-color)';

    // Contenido
    modal.innerHTML = `
        <h3 style="margin-top: 0; margin-bottom: 12px; color: var(--text-primary); font-size: 18px;">Confirmar borrado</h3>
        <p style="margin-bottom: 24px; color: var(--text-secondary); font-size: 14px; line-height: 1.5;">¿Estás seguro de que quieres borrar esta nota? Esta acción no se puede deshacer.</p>
        <div style="display: flex; justify-content: flex-end; gap: 12px;">
            <button id="cancel-btn" style="padding: 8px 16px; border-radius: 8px; border: 1px solid var(--border-color); background: transparent; color: var(--text-primary); cursor: pointer; font-weight: 500;">Cancelar</button>
            <button id="confirm-btn" style="padding: 8px 16px; border-radius: 8px; border: none; background: #ef4444; color: white; cursor: pointer; font-weight: 600;">Sí, Borrar</button>
        </div>
    `;

    overlay.appendChild(modal);
    document.body.appendChild(overlay);

    // Eventos
    document.getElementById('cancel-btn').addEventListener('click', () => {
        document.body.removeChild(overlay);
    });

    document.getElementById('confirm-btn').addEventListener('click', () => {
        document.body.removeChild(overlay);
        deleteDoc(doc(db, "proposal_notes", docId)).then(() => {
            if (window.editingNoteId === docId) {
                cancelEdit(phaseId);
            }
        }).catch((error) => {
            console.error("Error deleting document: ", error);
            alert("Error al borrar la nota.");
        });
    });
};

// Función global para iniciar la edición
window.startEditNote = (docId, phaseId) => {
    window.editingNoteId = docId;
    const currentText = document.getElementById(`text-${docId}`).innerText;
    
    const input = document.getElementById(`comment-${phaseId}`);
    input.value = currentText;
    input.focus();
    
    const btn = document.querySelector(`.btn-send-note[data-phase="${phaseId}"]`);
    btn.innerHTML = 'Actualizar';
    btn.style.background = '#f59e0b'; // Naranja para indicar edición
};

// Cancelar edición (si el usuario borra todo el texto, por ejemplo)
function cancelEdit(phaseId) {
    window.editingNoteId = null;
    const btn = document.querySelector(`.btn-send-note[data-phase="${phaseId}"]`);
    btn.innerHTML = 'Enviar';
    btn.style.background = '#3b82f6';
    document.getElementById(`comment-${phaseId}`).value = "";
}

function loadChatForPhase(phaseId) {
    const q = query(
        collection(db, "proposal_notes"),
        where("phase", "==", String(phaseId))
    );

    const messagesDiv = document.getElementById(`chat-messages-${phaseId}`);
    
    onSnapshot(q, (snapshot) => {
        let html = "";
        
        let docs = [];
        snapshot.forEach((docSnap) => {
            docs.push({ id: docSnap.id, data: docSnap.data() });
        });
        
        docs.sort((a, b) => {
            const timeA = a.data.timestamp ? a.data.timestamp.toMillis() : Date.now();
            const timeB = b.data.timestamp ? b.data.timestamp.toMillis() : Date.now();
            return timeA - timeB;
        });
        
        docs.forEach((item) => {
            html += renderComment(item.data, item.id);
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
    
    if (!text) {
        if (window.editingNoteId) cancelEdit(phaseId);
        return;
    }
    
    if (!auth.currentUser) {
        alert("Debes iniciar sesión para comentar.");
        return;
    }

    const btn = document.querySelector(`.btn-send-note[data-phase="${phaseId}"]`);
    btn.disabled = true;
    btn.innerHTML = '...';

    if (window.editingNoteId) {
        // ACTUALIZAR NOTA EXISTENTE
        const docRef = doc(db, "proposal_notes", window.editingNoteId);
        updateDoc(docRef, {
            text: text,
            updatedAt: serverTimestamp() // Mantenemos el timestamp original para el orden, guardamos updatedAt por si acaso
        }).then(() => {
            cancelEdit(phaseId);
            btn.disabled = false;
        }).catch((error) => {
            console.error("Error updating document: ", error);
            alert("Error al actualizar la nota.");
            btn.disabled = false;
        });
    } else {
        // CREAR NUEVA NOTA
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
}

document.addEventListener("DOMContentLoaded", () => {
    auth.onAuthStateChanged((user) => {
        if (user) {
            for (let i = 1; i <= 4; i++) {
                loadChatForPhase(i);
            }
        }
    });

    document.querySelectorAll('.btn-send-note').forEach(btn => {
        btn.addEventListener('click', (e) => {
            const phaseId = e.target.getAttribute('data-phase');
            sendNote(phaseId);
        });
    });
});
