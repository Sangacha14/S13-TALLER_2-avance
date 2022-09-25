class Venta{
    constructor() {
        this.items = {
            cliente : '',
            forma_pago : '',
            fecha : '',
            subtotal : 0.00,
            iva : 0.00,
            total : 0.00,
            articulos: []
        }
    }
    agregar(){
      console.log("agregando...")
    }
}
let $cboarticulo = document.querySelector('#cboArticulos')


document.getElementById("btnArticulos").addEventListener('click',() => {
    let art = $cboarticulo.options[$cboarticulo.selectedIndex].getAttribute('data-ajson')
    console.log(art)
})

