import os

new_stores_js = """import { db } from './firebase-config.js';
import { collection, onSnapshot } from "https://www.gstatic.com/firebasejs/10.9.0/firebase-firestore.js";

document.addEventListener("DOMContentLoaded", () => {
    const tbody = document.getElementById('stores-tbody');
    const searchInput = document.getElementById('search-store');
    const totalStores = document.getElementById('total-stores');
    
    // Pagination Controls
    const btnPrev = document.getElementById('btn-prev');
    const btnNext = document.getElementById('btn-next');
    const paginationInfo = document.getElementById('pagination-info');
    
    // Slide-over Controls
    const slideBackdrop = document.getElementById('slide-over-backdrop');
    const slidePanel = document.getElementById('slide-over-panel');
    const btnClosePanel = document.getElementById('btn-close-panel');
    
    let allStores = [];
    let filteredStores = [];
    let currentSort = { key: 'activeIncidents', dir: 'desc' };
    
    // Pagination state
    let currentPage = 1;
    const pageSize = 10;

    function renderTable() {
        if (!tbody) return;
        
        if (filteredStores.length === 0) {
            tbody.innerHTML = '<tr><td colspan="6" style="padding: 24px; text-align: center; color: var(--text-secondary);">No se encontraron tiendas.</td></tr>';
            if (totalStores) totalStores.innerText = '0';
            updatePaginationControls();
            return;
        }

        if (totalStores) totalStores.innerText = filteredStores.length;

        // Paginate
        const startIndex = (currentPage - 1) * pageSize;
        const endIndex = startIndex + pageSize;
        const pageStores = filteredStores.slice(startIndex, endIndex);

        tbody.innerHTML = pageStores.map(store => {
            const statusDot = store.activeIncidents > 0 
                ? '<div style="width: 10px; height: 10px; border-radius: 50%; background-color: #ef4444; box-shadow: 0 0 5px rgba(239, 68, 68, 0.5);"></div>'
                : '<div style="width: 10px; height: 10px; border-radius: 50%; background-color: #10b981; box-shadow: 0 0 5px rgba(16, 185, 129, 0.5);"></div>';
            
            const inventoryColor = store.stockStatus < 75 ? '#ef4444' : (store.stockStatus < 85 ? '#f59e0b' : '#10b981');
            const incidentsColor = store.activeIncidents > 0 ? '#ef4444' : '#6b7280';
            
            // Encode store data to pass to onclick handler safely
            const storeDataStr = encodeURIComponent(JSON.stringify(store));

            return `
                <tr style="border-bottom: 1px solid var(--border-color); transition: 0.2s; cursor: pointer;" class="store-row" onclick="window.openStoreDetails('${storeDataStr}')">
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
        
        updatePaginationControls();
    }
    
    function updatePaginationControls() {
        if (!paginationInfo) return;
        
        const total = filteredStores.length;
        if (total === 0) {
            paginationInfo.innerText = 'Mostrando 0-0 de 0';
            btnPrev.disabled = true;
            btnNext.disabled = true;
            return;
        }
        
        const startIndex = (currentPage - 1) * pageSize + 1;
        const endIndex = Math.min(startIndex + pageSize - 1, total);
        
        paginationInfo.innerText = `Mostrando ${startIndex}-${endIndex} de ${total}`;
        
        btnPrev.disabled = currentPage === 1;
        btnNext.disabled = endIndex >= total;
    }

    if (btnPrev) {
        btnPrev.addEventListener('click', () => {
            if (currentPage > 1) {
                currentPage--;
                renderTable();
            }
        });
    }
    
    if (btnNext) {
        btnNext.addEventListener('click', () => {
            if (currentPage * pageSize < filteredStores.length) {
                currentPage++;
                renderTable();
            }
        });
    }

    function sortData() {
        filteredStores.sort((a, b) => {
            let valA = a[currentSort.key];
            let valB = b[currentSort.key];

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
            currentSort.dir = (key === 'name') ? 'asc' : 'desc';
        }
        updateSortIndicators();
        applyFiltersAndSort();
    }
    
    function applyFiltersAndSort() {
        const searchTerm = searchInput ? searchInput.value.toLowerCase() : '';
        filteredStores = allStores.filter(store => 
            store.name.toLowerCase().includes(searchTerm) || 
            store.city.toLowerCase().includes(searchTerm) || 
            store.type.toLowerCase().includes(searchTerm)
        );
        sortData();
        currentPage = 1; // Reset pagination on new filter/sort
        renderTable();
    }

    const thName = document.getElementById('th-name');
    const thRevenue = document.getElementById('th-revenue');
    const thInventory = document.getElementById('th-inventory');
    const thIncidents = document.getElementById('th-incidents');

    if (thName) thName.addEventListener('click', () => handleSort('name'));
    if (thRevenue) thRevenue.addEventListener('click', () => handleSort('dailyRevenue'));
    if (thInventory) thInventory.addEventListener('click', () => handleSort('stockStatus'));
    if (thIncidents) thIncidents.addEventListener('click', () => handleSort('activeIncidents'));

    onSnapshot(collection(db, "stores"), (snapshot) => {
        allStores = snapshot.docs.map(doc => doc.data());
        applyFiltersAndSort();
    });

    if (searchInput) {
        searchInput.addEventListener('input', () => {
            applyFiltersAndSort();
        });
    }
    
    // CSS for row hover
    const style = document.createElement('style');
    style.innerHTML = `
        .store-row:hover { background-color: rgba(59, 130, 246, 0.05); }
    `;
    document.head.appendChild(style);

    // Slide-over logic
    window.openStoreDetails = function(storeDataStr) {
        const store = JSON.parse(decodeURIComponent(storeDataStr));
        
        document.getElementById('slide-store-name').innerText = store.name;
        document.getElementById('slide-store-id').innerText = '#' + store.id;
        document.getElementById('slide-store-city').innerText = store.city + ' (' + store.type + ')';
        
        // Mock manager
        const managers = ['Carlos Ruiz', 'Marta Gómez', 'Alejandro Sanz', 'Lucía Pérez', 'Javier Fernández'];
        const seed = store.name.length;
        document.getElementById('slide-store-manager').innerText = managers[seed % managers.length];
        
        document.getElementById('slide-store-revenue').innerText = '$' + store.dailyRevenue.toLocaleString();
        
        const invEl = document.getElementById('slide-store-inventory');
        invEl.innerText = store.stockStatus + '%';
        
        const invBox = document.getElementById('slide-inv-box');
        if (store.stockStatus < 75) {
            invEl.style.color = '#ef4444';
            invBox.style.background = 'rgba(239, 68, 68, 0.05)';
            invBox.style.borderColor = 'rgba(239, 68, 68, 0.2)';
            invBox.querySelector('div').style.color = '#ef4444';
        } else if (store.stockStatus < 85) {
            invEl.style.color = '#f59e0b';
            invBox.style.background = 'rgba(245, 158, 11, 0.05)';
            invBox.style.borderColor = 'rgba(245, 158, 11, 0.2)';
            invBox.querySelector('div').style.color = '#f59e0b';
        } else {
            invEl.style.color = 'var(--text-primary)';
            invBox.style.background = 'rgba(16, 185, 129, 0.05)';
            invBox.style.borderColor = 'rgba(16, 185, 129, 0.2)';
            invBox.querySelector('div').style.color = '#10b981';
        }
        
        const badge = document.getElementById('slide-store-incidents-badge');
        badge.innerText = store.activeIncidents;
        badge.style.background = store.activeIncidents > 0 ? '#ef4444' : '#10b981';
        
        const list = document.getElementById('slide-store-incidents-list');
        if (store.activeIncidents === 0) {
            list.innerHTML = '<span style="color: #10b981;">✓ Todo en orden. Sin incidencias reportadas hoy.</span>';
        } else {
            list.innerHTML = `
                <ul style="padding-left: 16px; margin: 0; color: #ef4444;">
                    <li style="margin-bottom: 8px;">Rotura de stock inminente detectada en top ventas.</li>
                    ${store.activeIncidents > 1 ? '<li style="margin-bottom: 8px;">Diferencia de caja detectada en TPV 2 vs Holded.</li>' : ''}
                    ${store.activeIncidents > 2 ? '<li>Falta de personal programada para el turno de tarde (Bizneo).</li>' : ''}
                </ul>
            `;
        }
        
        // Show panel
        slideBackdrop.style.opacity = '1';
        slideBackdrop.style.visibility = 'visible';
        slidePanel.style.right = '0';
    };
    
    function closePanel() {
        slideBackdrop.style.opacity = '0';
        slideBackdrop.style.visibility = 'hidden';
        slidePanel.style.right = '-100%';
    }
    
    if (btnClosePanel) btnClosePanel.addEventListener('click', closePanel);
    if (slideBackdrop) slideBackdrop.addEventListener('click', closePanel);
});
"""

with open("stores.js", "w", encoding="utf-8") as f:
    f.write(new_stores_js)

print("Updated stores.js")
