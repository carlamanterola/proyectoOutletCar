document.querySelectorAll('.btn-verDetalle').forEach(boton => {
    boton.addEventListener('click', function (e) {
        e.preventDefault();

        this.textContent = 'Cargando...';

        setTimeout(() => {
            window.location.href = this.href;
        }, 1600);
    });
});

document.querySelectorAll('.btn-verDetalle').forEach(boton => {
    boton.addEventListener('click', function (e) {
        if (!confirm('¿Quieres ver los detalles de esta marca?')) {
            e.preventDefault();
        }
    });
});

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