//para desvanecer la pagina despacio
document.querySelectorAll('.btn-verDetalle').forEach(boton => {
    boton.addEventListener('click', function (e) {
        e.preventDefault();

        document.body.classList.add('fade-out');

        setTimeout(() => {
            window.location.href = this.href;
        }, 400);
    });
});

document.querySelectorAll('.btn-eliminar').forEach(btn => {
    btn.addEventListener('click', function (e) {
        e.preventDefault();

        if (!confirm('¿Quieres ver los detalles de esta marca?')) {
            e.preventDefault();
        }
    });
});

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