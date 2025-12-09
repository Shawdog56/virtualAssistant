const exploreList = [
    { img: "/static/img_list_music/Captura de pantalla 2025-12-03 201820.png", name: "Música tranquila" },
    { img: "/static/img_list_music/Captura de pantalla 2025-12-03 202818.png", name: "Top mundial" },
    { img: "/static/img_list_music/Captura de pantalla 2025-12-03 204742.png", name: "Rock clásico" },
    { img: "/static/img_list_music/Captura de pantalla 2025-12-03 203807.png", name: "Electrónica 🔥" },
];

const exploreGrid = document.getElementById("exploreGrid");

exploreList.forEach(item => {
    exploreGrid.innerHTML += `
        <div class="song-card">
            <img src="/static/${item.img}" alt="">
            <p>${item.name}</p>
        </div>
    `;
});
