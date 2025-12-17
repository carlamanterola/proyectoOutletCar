var sliderKm = document.getElementById("filtroKm");
var valorKm = document.getElementById("kmValor");
valorKm.innerHTML = sliderKm.value;

sliderKm.oninput = function() {
    valorKm.innerHTML = this.value;
}

var sliderPrecio = document.getElementById("filtroPrecio");
var valorPrecio = document.getElementById("precioValor");
valorPrecio.innerHTML = sliderPrecio.value;

sliderPrecio.oninput = function() {
    valorPrecio.innerHTML = this.value;
}


document.addEventListener("DOMContentLoaded", () => {

    const filtroNombre = document.getElementById("filtroNombre");
    const filtroMarca = document.getElementById("filtroMarca");
    const filtroCombustible = document.getElementById("filtroCombustible");
    const filtroKm = document.getElementById("filtroKm");
    const filtroPrecio = document.getElementById("filtroPrecio");
    const boton = document.getElementById("aplicarFiltros");

    const ofertas = document.querySelectorAll(".elemento");

    boton.addEventListener("click", () => {

        const nombre = filtroNombre.value.toLowerCase();
        const marca = filtroMarca.value.toLowerCase();
        const combustible = filtroCombustible.value.toLowerCase();
        const kmMax = parseInt(filtroKm.value) || Infinity;
        const precioMax = parseInt(filtroPrecio.value) || Infinity;

        ofertas.forEach(oferta => {
            const modelo = oferta.dataset.modelo;
            const marcaOferta = oferta.dataset.marca;
            const combustibleOferta = oferta.dataset.combustible;
            const kmOferta = parseInt(oferta.dataset.km);
            const precioOferta = parseInt(oferta.dataset.precio);

            let visible = true;

            if (nombre && !modelo.includes(nombre)) visible = false;
            if (marca && marcaOferta !== marca) visible = false;
            if (combustible && combustibleOferta !== combustible) visible = false;
            if (kmOferta > kmMax) visible = false;
            if (precioOferta > precioMax) visible = false;

            oferta.style.display = visible ? "flex" : "none";
        });
    });
});
