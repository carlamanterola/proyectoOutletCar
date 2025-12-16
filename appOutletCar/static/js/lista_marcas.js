document.querySelectorAll('.btn-verDetalle').forEach(btn => {
    btn.addEventListener('click', function (e) {
        e.preventDefault();

        const url = this.href;

        Swal.fire({
            title: '¿Estás seguro?',
            text: '¿Quieres ver los detalles de esta marca?',
            icon: 'question',
            showCancelButton: true,
            confirmButtonText: 'Sí, ver detalles',
            cancelButtonText: 'Cancelar',
            confirmButtonColor: 'green',
            cancelButtonColor: 'red'
        }).then((result) => {  // .then, cuando el usuario haya clickado en aceptar o cancelar
            if (result.isConfirmed) {
                
                document.body.classList.add('fade-out');
                setTimeout(() => {
                    window.location.href = this.href;
                }, 400);
                    }
        });
    });
});