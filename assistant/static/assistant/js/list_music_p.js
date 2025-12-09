const music = [
    { img: "/static/img_list_music/Captura de pantalla 2025-12-03 201315.png", name: "Everlong – Foo Fighters" },
    { img: "/static/img_list_music/Captura de pantalla 2025-12-03 201820.png", name: "Californication – Red Hot Chili Peppers" },
    { img: "/static/img_list_music/Captura de pantalla 2025-12-03 202120.png", name: "Electric Feel – MGMT" },
    { img: "/static/img_list_music/Captura de pantalla 2025-12-03 202545.png", name: "Unholy – Sam Smith & Kim Petras" },
    { img: "/static/img_list_music/Captura de pantalla 2025-12-03 202818.png", name: "Don't Start Now – Dua Lipa" },
    { img: "/static/img_list_music/Captura de pantalla 2025-12-03 203052.png", name: "Black Hole Sun – Soundgarden" },
    { img: "/static/img_list_music/Captura de pantalla 2025-12-03 203413.png", name: "Strobe – Deadmau5" },
    { img: "/static/img_list_music/Captura de pantalla 2025-12-03 203807.png", name: "Animals – Martin Garrix" }
];

const recent = [
    { img: "/static/img_list_music/Captura de pantalla 2025-12-03 204041.png", name: "Ojos Color Sol – Calle 13 ft. Silvio Rodríguez" },
    { img: "/static/img_list_music/Captura de pantalla 2025-12-03 204236.png", name: "Yonaguni – Bad Bunny" },
    { img: "/static/img_list_music/Captura de pantalla 2025-12-03 204345.png", name: "Caraluna – Bacilos" },
    { img: "/static/img_list_music/Captura de pantalla 2025-12-03 204742.png", name: "La Ingrata - Cafe Tacuba" }
];

const grid = document.getElementById("musicGrid");
const recentGrid = document.getElementById("recentGrid");

music.forEach(song => {
    grid.innerHTML += `
        <div class="song-card">
            <img src="${song.img}" alt="">
            <p>${song.name}</p>
        </div>
    `;
});

recent.forEach(song => {
    recentGrid.innerHTML += `
        <div class="song-card">
            <img src="${song.img}" alt="">
            <p>${song.name}</p>
        </div>
    `;
});
