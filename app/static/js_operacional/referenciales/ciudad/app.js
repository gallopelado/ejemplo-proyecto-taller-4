$(async()=> {
  // todo lo que se ejecutara aqui, se hara luego de que el html este completo 
  // Bienvenidos a axios y REST
  // lag
  try {
    // El browser tiene la esperanza de que todo ira bien
    // async/await
    const respuesta = await axios.get('/seguridad/ciudad/get_ciudades')
    console.log(respuesta.data)
  } catch (error) {
    console.error(error)
  }
})