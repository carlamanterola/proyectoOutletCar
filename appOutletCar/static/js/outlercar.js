document.addEventListener("DOMContentLoaded", () => {
    const tabla = document.querySelector("#tabla-coches");
    if (!tabla) return;

    const tbody = tabla.querySelector("tbody");
    const url = tabla.dataset.url;

    fetch(url)
        .then(res => res.json())
        .then(coches => {
            tbody.innerHTML = "";

            if (coches.length === 0) {
                tbody.innerHTML = `
                    <tr>
                        <td colspan="3">No hay coches disponibles</td>
                    </tr>`;
                return;
            }

            coches.forEach(coche => {
                const fila = document.createElement("tr");

                const fotoHTML = coche.foto
                    ? `<a href="/appOutletCar/ofertas/${coche.oferta_id}/">
                           <img src="${coche.foto}" alt="Foto coche" style="width:140px;border-radius:8px;">
                       </a>`
                    : "Sin foto";

                fila.innerHTML = `
                    <td>${coche.marca_nombre}</td>
                    <td>${coche.modelo}</td>
                    <td>${fotoHTML}</td>
                    <td>${coche.precio} €</td>
                `;

                tbody.appendChild(fila);
            });
        })
        .catch(err => {
            console.error(err);
            tbody.innerHTML = `
                <tr>
                    <td colspan="3">Error al cargar los coches</td>
                </tr>`;
        });
});
