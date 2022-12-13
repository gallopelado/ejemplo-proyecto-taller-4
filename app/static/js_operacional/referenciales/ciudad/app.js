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