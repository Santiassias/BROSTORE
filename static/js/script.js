// Lista de productos simulada
const productos = [
    {
        nombre: "Camisa Blanca",
        descripcion: "Camisa de algodón 100%",
        precio: 25.99,
        imagen: "https://via.placeholder.com/300x200?text=Camisa"
    },
    {
        nombre: "Pantalón Jeans",
        descripcion: "Jeans azul clásico",
        precio: 40.50,
        imagen: "https://via.placeholder.com/300x200?text=Jeans"
    },
    {
        nombre: "Zapatillas",
        descripcion: "Zapatillas deportivas unisex",
        precio: 65.00,
        imagen: "https://via.placeholder.com/300x200?text=Zapatillas"
    },
    {
        nombre: "Chaqueta",
        descripcion: "Chaqueta impermeable ligera",
        precio: 80.00,
        imagen: "https://via.placeholder.com/300x200?text=Chaqueta"
    }
];

// Función para renderizar productos
function cargarProductos() {
    const contenedor = document.getElementById("productos");
    productos.forEach(producto => {
        const div = document.createElement("div");
        div.className = "producto";
        div.innerHTML = `
            <img src="${producto.imagen}" alt="${producto.nombre}">
            <div class="contenido">
                <h3>${producto.nombre}</h3>
                <p>${producto.descripcion}</p>
                <p class="precio">$${producto.precio.toFixed(2)}</p>
                <button onclick="agregarAlCarrito('${producto.nombre}')">Agregar al carrito</button>
            </div>
        `;
        contenedor.appendChild(div);
    });
}

// Acción del botón
function agregarAlCarrito(nombre) {
    alert(`"${nombre}" fue agregado al carrito.`);
}

document.addEventListener("DOMContentLoaded", cargarProductos);
