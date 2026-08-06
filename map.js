import { db } from './firebase-config.js';
import { collection, onSnapshot } from "https://www.gstatic.com/firebasejs/10.9.0/firebase-firestore.js";

document.addEventListener("DOMContentLoaded", () => {
    // Solo inicializar si estamos en la página del dashboard (donde existe #map)
    const mapContainer = document.getElementById('map');
    if (!mapContainer) return;

    // Inicializar mapa centrado en España
    const map = L.map('map').setView([40.4168, -3.7038], 6); // Madrid, Zoom 6 para ver toda España

    // Usar CartoDB Positron por estética clara/oscura (muy Apple-like)
    L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
        subdomains: 'abcd',
        maxZoom: 20
    }).addTo(map);

    // Iconos personalizados
    const greenIcon = new L.Icon({
        iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-green.png',
        shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
        iconSize: [25, 41],
        iconAnchor: [12, 41],
        popupAnchor: [1, -34],
        shadowSize: [41, 41]
    });

    const redIcon = new L.Icon({
        iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-red.png',
        shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
        iconSize: [25, 41],
        iconAnchor: [12, 41],
        popupAnchor: [1, -34],
        shadowSize: [41, 41]
    });

    // Guardar marcadores actuales para poder actualizarlos en tiempo real
    let markers = {};

    // Escuchar la colección de tiendas en Firebase
    onSnapshot(collection(db, "stores"), (snapshot) => {
        snapshot.docChanges().forEach((change) => {
            const store = change.doc.data();
            const id = change.doc.id;
            
            if (change.type === "added" || change.type === "modified") {
                // Crear popup estético
                const popupContent = `
                    <div style="font-family: 'Inter', sans-serif; min-width: 150px;">
                        <strong style="display:block; margin-bottom: 4px; font-size: 14px; color: #111827;">${store.name}</strong>
                        <div style="font-size: 12px; color: #6b7280; margin-bottom: 8px;">${store.city} (${store.type})</div>
                        <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                            <span style="font-size: 13px;">Inventario:</span>
                            <span style="font-size: 13px; font-weight: 600; color: ${store.stockStatus < 75 ? '#ef4444' : '#10b981'}">${store.stockStatus}%</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                            <span style="font-size: 13px;">Incidencias:</span>
                            <span style="font-size: 13px; font-weight: 600; color: ${store.activeIncidents > 0 ? '#ef4444' : '#6b7280'}">${store.activeIncidents}</span>
                        </div>
                        <div style="display: flex; justify-content: space-between;">
                            <span style="font-size: 13px;">Ventas Hoy:</span>
                            <span style="font-size: 13px; font-weight: 600;">$${store.dailyRevenue.toLocaleString()}</span>
                        </div>
                    </div>
                `;

                // Elegir color del marcador
                const icon = store.activeIncidents > 0 ? redIcon : greenIcon;

                if (markers[id]) {
                    // Actualizar marcador existente
                    markers[id].setIcon(icon);
                    markers[id].setPopupContent(popupContent);
                } else {
                    // Crear nuevo marcador
                    const marker = L.marker([store.lat, store.lng], { icon: icon })
                        .addTo(map)
                        .bindPopup(popupContent);
                    markers[id] = marker;
                }
            }
            if (change.type === "removed") {
                if (markers[id]) {
                    map.removeLayer(markers[id]);
                    delete markers[id];
                }
            }
        });
    });
});
