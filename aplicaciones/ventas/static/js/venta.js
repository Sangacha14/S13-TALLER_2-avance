class Venta{
    constructor(iva,save) {
        this.save=save
        this.iva = iva
        this.items = {
            cliente : '',
            forma_pago : '',
            fecha : '',
            subtotal : 0,
            iva : 0,
            total : 0,
            articulos: []
        }
    }
     editar(detalle){
         this.items.articulos = detalle.map(item => {
            item.id = item.id
            item.descripcion=item.descripcion
            item.cantidad = parseFloat(item.cantidad)
            item.precio = parseFloat(item.precio)
            item.subtotal = parseFloat(item.subtotal)
            item.iva = parseFloat(item.iva)
            item.total = parseFloat(item.total)
            return item
       })
       this.totales()
       this.presentar()
     }
     agregar(articulo){
       let cantidad = parseFloat(articulo.cantidad)
       let precio =  articulo.precio
       let subtotal = parseFloat ((cantidad*precio).toFixed(2))
       let iva = articulo.coniva ? parseFloat((subtotal*this.iva).toFixed(2)): 0
       let art = {
         id:articulo.id,
         descripcion:articulo.descripcion,
         precio,
         cantidad,
         subtotal,
         iva,
         total:subtotal+iva
       }
       let enc=false
       this.items.articulos = this.items.articulos = this.items.articulos.map(item => {
          if (item.id == articulo.id) {
            item.cantidad += art.cantidad
            item.subtotal += art.subtotal
            item.iva += art.iva
            item.total += art.subtotal + art.iva
            enc=true
          }
          return item
       })
       if (!enc) {
         this.items.articulos = [
           ...this.items.articulos,
           art
         ]
       }
      //console.log(this.items.articulos)
      this.totales()
      this.presentar()
    }
     presentar() {
       let detalle = document.getElementById('detalle')
       detalle.innerHTML=""
       this.items.articulos.forEach((articulo) => {
          detalle.innerHTML +=  `<tr>
            <td>${articulo.id}</td>
            <td>${articulo.descripcion}</td>
            <td>${articulo.precio}</td>
            <td>${articulo.cantidad}</td>
            <td>${articulo.subtotal.toFixed(2)}</td>
            <td>${articulo.iva.toFixed(2)}</td>
            <td>${articulo.total.toFixed(2)}</td>
            <td><button data-id="${articulo.id}" class="btn btn-danger itemdelete" >❌</button></td>
           </tr>`
        });
     }
     totales(){
            this.items.subtotal = 0;
            this.items.iva = 0;
            this.items.total = 0;
            this.items.articulos.forEach(item => {
                this.items.iva += item.iva;
                this.items.subtotal += item.subtotal;
                this.items.total += item.total;
            })
            document.getElementById('id_subtotal').value= this.items.subtotal.toFixed(2);
            document.getElementById('id_iva').value= this.items.iva.toFixed(2);
            document.getElementById('id_total').value= this.items.total.toFixed(2);
     }
     eliminar(id){
      console.log("eliminando ",id)
      this.items.articulos=this.items.articulos.filter(item => item.id != id)
      this.totales()
      this.presentar()
     }
     registrar(){
      if (this.items.articulos.length > 0 && this.items.total > 0) {
        this.items.fecha = document.getElementById('id_fecha').value
        this.items.cliente = document.getElementById('id_cliente').value
        this.items.forma_pago = document.getElementById('id_forma_pago').value
        this.items.action=document.querySelector('[name=action]').value
        console.log(this.items)
        let csrf = document.querySelector('[name=csrfmiddlewaretoken]').value
        console.log(csrf)
        const grabarVenta = async (url) => {
          console.log(url)
        try {
            const res = await fetch(url,
           {
                method: 'POST',
                headers: {
                'X-Requested-With': 'XMLHttpRequest',
                'Content-Type': 'application/json',
                'X-CSRFToken': csrf,
                },
                body: JSON.stringify(this.items)
               });
            const post = await res.json();
              console.log(post.grabar);
              alert("Factura grabada Satisfactoriamente")

          } catch (error) {
              console.log("error=>",error);
              alert(error)
          }
        };
        grabarVenta(this.save);

      }
      else{
          alert("no hay datos")
      }
     }
// fin de la clase
}
document.addEventListener("DOMContentLoaded", e => {
   console.log("Pagina cargada")

   let iva = parseFloat(ivas)
   let venta = new Venta(iva,save)

   if (document.querySelector('[name=action]').value== 'add') {
     document.getElementById('id_cliente').value=1
   }else{
     venta.editar(detfac)
   }
   //delegacion de eventos: el objeto que origina el evento coincide con el metodo matches() ejcuta el codigo
   document.addEventListener('click',(e) => {
        if (e.target.matches("#btnArticulos")){
          console.warn(e.target)
        let $cboarticulo = document.querySelector('#cboArticulos')
        let art = $cboarticulo.options[$cboarticulo.selectedIndex].getAttribute('data-ajson')
        let articulo = JSON.parse(art)
        articulo.id = parseInt(articulo.id)
        articulo.precio = parseFloat(articulo.precio)
        articulo.coniva = articulo.coniva=='True' ? true: false
        articulo.cantidad=document.getElementById('idCantidad').value
        //console.log(articulo)
        articulo.descripcion=$cboarticulo.options[$cboarticulo.selectedIndex].textContent.trim()
        venta.agregar(articulo)
      }else{
         if (e.target.matches(".itemdelete")){
           //console.log(e.target.getAttribute('data-id')
           console.log(e.target)
           venta.eliminar(e.target.dataset.id)
         }else{
            if (e.target.matches("#btnGrabar")){
              e.preventDefault()
              //alert("Grabando...")
              venta.registrar()


            }
         }
      }
   })
});




