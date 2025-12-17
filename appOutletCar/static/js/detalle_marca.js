//para desvanecer la pagina despacio

const filtroKm = document.getElementById('filtroKm');
filtroKm.addEventListener('input', () => {
    const maxKm = filtroKm.value;

    document.querySelectorAll('.cocheDetalle').forEach(coche => {
        const kmTexto = coche.querySelector('p:nth-of-type(2)').innerText;
        const km = parseInt(kmTexto.replace(/\D/g, ''));  // el \D  selecciona cualquier cosa que no sea un numero y sustituye por ''

        if (!maxKm || km <= maxKm) {
            coche.style.display = 'flex'; //se enseña
        } else {
            coche.style.display = 'none'; //se oculta
        }
    });
});