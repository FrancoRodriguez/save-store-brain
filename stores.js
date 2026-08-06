import { db } from './firebase-config.js';
import { collection, onSnapshot } from "https://www.gstatic.com/firebasejs/10.9.0/firebase-firestore.js";

document.addEventListener("DOMContentLoaded", () => {
    const tbody = document.getElementById('stores-tbody');
    const searchInput = document.getElementById('search-store');
    const totalStores = document.getElementById('total-stores');
    
    let allStores = [];

    function renderTable(stores) {
        if (!tbody) return;
        
        if (stores.length === 0) {
            tbody.innerHTML = '<tr><td colspan="6" style="padding: 24px; text-align: center; color: var(--text-secondary);">No se encontraron tiendas.</td></tr>';
            if (totalStores) totalStores.innerText = '0';
            return;
        }

        if (totalStores) totalStores.innerText = stores.length;

        tbody.innerHTML = stores.map(store => {
            const statusDot = store.activeIncidents > 0 
                ? '<div style="width: 10px; height: 10px; border-radius: 50%; background-color: #ef4444; box-shadow: 0 0 5px rgba(239, 68, 68, 0.5);"></div>'
                : '<div style="width: 10px; height: 10px; border-radius: 50%; background-color: #10b981; box-shadow: 0 0 5px rgba(16, 185, 129, 0.5);"></div>';
            
            const inventoryColor = store.stockStatus < 75 ? '#ef4444' : (store.stockStatus < 85 ? '#f59e0b' : '#10b981');
            const incidentsColor = store.activeIncidents > 0 ? '#ef4444' : '#6b7280';

            return `
                <tr style="border-bottom: 1px solid var(--border-color); transition: 0.2s;">
                    <td style="padding: 16px; width: 60px;">${statusDot}</td>
                    <td style="padding: 16px; color: var(--text-primary); font-weight: 500;">
                        ${store.name}
                        <div style="font-size: 12px; color: var(--text-secondary); font-weight: normal; margin-top: 2px;">#${store.id}</div>
                    </td>
                    <td style="padding: 16px; color: var(--text-secondary);">
                        ${store.city}
                        <div style="font-size: 12px; margin-top: 2px;">${store.type}</div>
                    </td>
                    <td style="padding: 16px; font-weight: 600; color: var(--text-primary);">
                        $${store.dailyRevenue.toLocaleString()}
                    </td>
                    <td style="padding: 16px; font-weight: 600; color: ${inventoryColor};">
                        ${store.stockStatus}%
                    </td>
                    <td style="padding: 16px; font-weight: ${store.activeIncidents > 0 ? '600' : 'normal'}; color: ${incidentsColor};">
                        ${store.activeIncidents} ${store.activeIncidents === 1 ? 'incidencia' : 'incidencias'}
                    </td>
                </tr>
            `;
        }).join('');
    }

    let currentSort = { key: 'activeIncidents', dir: 'desc' };

    function sortData(stores) {
        return stores.sort((a, b) => {
            let valA = a[currentSort.key];
            let valB = b[currentSort.key];

            // Si ordenamos por incidencias, mantener orden secundario por nombre
            if (currentSort.key === 'activeIncidents' && valA === valB) {
                return currentSort.dir === 'desc' 
                    ? a.name.localeCompare(b.name) 
                    : b.name.localeCompare(a.name);
            }

            if (typeof valA === 'string') {
                return currentSort.dir === 'asc' 
                    ? valA.localeCompare(valB) 
                    : valB.localeCompare(valA);
            } else {
                return currentSort.dir === 'asc' ? valA - valB : valB - valA;
            }
        });
    }

    function updateSortIndicators() {
        const headers = {
            'name': document.getElementById('th-name'),
            'dailyRevenue': document.getElementById('th-revenue'),
            'stockStatus': document.getElementById('th-inventory'),
            'activeIncidents': document.getElementById('th-incidents')
        };

        for (const [key, th] of Object.entries(headers)) {
            if (!th) continue;
            const span = th.querySelector('span');
            if (key === currentSort.key) {
                span.innerText = currentSort.dir === 'asc' ? ' ▲' : ' ▼';
            } else {
                span.innerText = '';
            }
        }
    }

    function handleSort(key) {
        if (currentSort.key === key) {
            currentSort.dir = currentSort.dir === 'asc' ? 'desc' : 'asc';
        } else {
            currentSort.key = key;
            currentSort.dir = (key === 'name') ? 'asc' : 'desc'; // Default text to asc, numbers to desc
        }
        updateSortIndicators();
        
        // Refilter and re-render
        const searchTerm = searchInput ? searchInput.value.toLowerCase() : '';
        const filtered = allStores.filter(store => 
            store.name.toLowerCase().includes(searchTerm) || 
            store.city.toLowerCase().includes(searchTerm) || 
            store.type.toLowerCase().includes(searchTerm)
        );
        renderTable(sortData(filtered));
    }

    // Attach event listeners to headers
    const thName = document.getElementById('th-name');
    const thRevenue = document.getElementById('th-revenue');
    const thInventory = document.getElementById('th-inventory');
    const thIncidents = document.getElementById('th-incidents');

    if (thName) thName.addEventListener('click', () => handleSort('name'));
    if (thRevenue) thRevenue.addEventListener('click', () => handleSort('dailyRevenue'));
    if (thInventory) thInventory.addEventListener('click', () => handleSort('stockStatus'));
    if (thIncidents) thIncidents.addEventListener('click', () => handleSort('activeIncidents'));

    // Escuchar cambios en Firestore
    onSnapshot(collection(db, "stores"), (snapshot) => {
        allStores = snapshot.docs.map(doc => doc.data());
        
        const searchTerm = searchInput ? searchInput.value.toLowerCase() : '';
        const filtered = allStores.filter(store => 
            store.name.toLowerCase().includes(searchTerm) || 
            store.city.toLowerCase().includes(searchTerm) || 
            store.type.toLowerCase().includes(searchTerm)
        );
        
        renderTable(sortData(filtered));
    });

    // Búsqueda en tiempo real
    if (searchInput) {
        searchInput.addEventListener('input', (e) => {
            const searchTerm = e.target.value.toLowerCase();
            const filtered = allStores.filter(store => 
                store.name.toLowerCase().includes(searchTerm) || 
                store.city.toLowerCase().includes(searchTerm) || 
                store.type.toLowerCase().includes(searchTerm)
            );
            renderTable(sortData(filtered));
        });
    }
});
