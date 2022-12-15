$(async()=> {
  // Feliz 2023
  // todo lo que se ejecutara aqui, se hara luego de que el html este completo 
  // Bienvenidos a axios y REST
 
  const modal_ciudad_formulario = $('#modal_ciudad_formulario')
  const bt_ciudad_agregar = $('#bt_ciudad_agregar')
  const btn_nacionalidad_enviar = $('#btn_nacionalidad_enviar')
  const a_ciudad_trae_ciudad = $('#a_ciudad_trae_ciudad')
  const a_ciudad_limpiar_tabla = $('#a_ciudad_limpiar_tabla')
  try {
    
    // Traer las ciudades
    await traerCiudades()

    $('button[name="bt_ciudad_eliminar"]').on('click', () => {
      alert('Soy la forma mas larga de usarme')
      //funcion eliminar
    })

    // boton editar
    $('button[name="bt_ciudad_editar"]').on('click', function() {
      //funcion editar
      //console.log($(this).attr('id_ciudad'), $(this).attr('descri_ciudad'))
      const ciudad = { 
        id: $(this).attr('id_ciudad') 
        ,descripcion: $(this).attr('descri_ciudad')
      }

      $('#btn_nacionalidad_enviar').text('Editar').removeClass('btn-primary').addClass('btn-warning')
      //$('#btn_nacionalidad_enviar').removeClass('btn-primary')
      //$('#btn_nacionalidad_enviar').addClass('btn-warning')
      // seteando el modal
      $('#txt_id_ciudad').val(ciudad.id)
      $('#txt_ciudad').val(ciudad.descripcion)
      modal_ciudad_formulario.modal('show')
    })

    // asignando el evento al boton agregar
    bt_ciudad_agregar.on('click', () => {
      // activando el modal, mostrando
      // limpiar formulario
      $('#txt_id_ciudad').val('')
      $('#txt_ciudad').val('')
      modal_ciudad_formulario.modal('show')
    })

    btn_nacionalidad_enviar.on('click', async() => {

      //debugger
      // recolectar los datos que el usuario ha ingresado
      const id = $('#txt_id_ciudad').val()
      const descripcion = $('#txt_ciudad').val()
      if(descripcion && descripcion.trim()) {
        const ciudad = {
          id: id, descripcion: descripcion.toUpperCase()
        }
        try {
          // enviar la ciudad a mi servidor
          // destructuracion
          const { data } = await axios.post('/seguridad/ciudad/agregar_ciudad', ciudad)
          if(data.estado && data.estado !== 'error') {
            // cerrar el modal
            modal_ciudad_formulario.modal('hide')
            // limpiar formulario
            $('#txt_id_ciudad').val('')
            $('#txt_ciudad').val('')
            // mensaje exitoso
            Notiflix.Report.success('Correcto', 'Se ha guardado el registro', 'Salir')
            $("#tbody_ciudad").empty()//limpiar el tbody
            await traerCiudades()
            return
          }

          if(data.estado && data.estado === 'error') {
            // cerrar el modal
            modal_ciudad_formulario.modal('hide')
            // mensaje exitoso
            Notiflix.Report.warning('Cuidado', 'No se ha guardado el registro', 'Salir')
            console.error(data.mensaje)
            return
          }

          Notiflix.Report.warnign('Cuidado', 'No se ha guardado el registro', 'Salir')

          console.log(respuesta)
        } catch (error) {
          console.log(error)
        }
      } 
      console.log(id, descripcion)

    })

    a_ciudad_trae_ciudad.on('click', async()=> {
      const respuesta = await axios.get('/seguridad/ciudad/get_ciudades')
      console.log(respuesta.data)
      const lista_ciudades = respuesta.data
      const tbody = $('#tbody_ciudad')
      let contenido = ''
      lista_ciudades.forEach( item => {
        //console.log(item)
        contenido += `<tr>
                        <td>${item.descripcion}</td>
                      </tr>`
      })
      //console.log(contenido)
      tbody.html(contenido)
    })


  } catch (error) {
    console.error(error)
  }
})

// otra forma de trabajar el editar
/* window.editar_ciudad = (id, texto) => {
  alert(`editando elemento, ${id} - ${texto}`)
  //editar
} */
// onclick="editar_ciudad('${item.id}', '${item.descripcion}')"

const traerCiudades = async() => {
  try{
    const respuesta = await axios.get("/seguridad/ciudad/get_ciudades");
    console.log(respuesta.data);
    const lista_ciudades = respuesta.data;
    const tbody = $("#tbody_ciudad");
    let contenido = "";
    lista_ciudades.forEach((item) => {
      contenido += `<tr name="mi_tr">
                        <td>
                          <a href="">
                            ${item.descripcion}
                          </a>
                          </td>
                        <td class="d-flex justify-content-end">
                            <div class="btn-group" role="group" aria-label="Botones para accion">
                                <button type="button" name="bt_ciudad_editar" class="btn btn-outline-primary" id_ciudad="${item.id}" descri_ciudad="${item.descripcion}">Editar</button>
                                <button type="button" name="bt_ciudad_eliminar" class="btn btn-outline-danger">Eliminar</button>
                            </div>
                        </td>
                    </tr>`;
    });
    //console.log(contenido)
    tbody.html(contenido);
  } catch(error) {
    console.log(`El errorcillo se esta mostrando - ${error}`)
  }
}