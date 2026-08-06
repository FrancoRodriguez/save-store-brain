import { auth, db } from './firebase-config.js';
import { collection, addDoc, getDocs, writeBatch, doc } from "https://www.gstatic.com/firebasejs/10.9.0/firebase-firestore.js";

async function seedStores() {
    if (!auth.currentUser) {
        alert("Debes iniciar sesión para migrar los datos.");
        return;
    }

    const btn = document.getElementById('btn-seed');
    if (btn) {
        btn.disabled = true;
        btn.innerHTML = "Migrando... (No cerrar)";
    }

    try {
        // 1. Fetch local stores.json
        const response = await fetch('stores.json');
        const stores = await response.json();

        // 2. Check if already seeded to avoid duplicates
        const snapshot = await getDocs(collection(db, "stores"));
        if (!snapshot.empty) {
            alert("Las tiendas ya existen en la base de datos de Firebase. Borra la colección 'stores' si quieres volver a migrar.");
            if (btn) {
                btn.disabled = false;
                btn.innerHTML = "Migrar Tiendas a Firebase";
            }
            return;
        }

        // 3. Batch write (Firestore batch limits to 500 ops, we have 42 so it's fine)
        const batch = writeBatch(db);
        
        stores.forEach((store) => {
            const docRef = doc(collection(db, "stores")); // auto-generate ID
            batch.set(docRef, store);
        });

        await batch.commit();
        
        alert(`¡Éxito! Se han migrado ${stores.length} tiendas a Firebase.`);
        
        // Hide button after success
        if (btn) btn.style.display = 'none';
        
    } catch (error) {
        console.error("Error seeding stores:", error);
        alert("Error al migrar los datos: " + error.message);
        if (btn) {
            btn.disabled = false;
            btn.innerHTML = "Reintentar Migración";
        }
    }
}

window.seedStores = seedStores;
