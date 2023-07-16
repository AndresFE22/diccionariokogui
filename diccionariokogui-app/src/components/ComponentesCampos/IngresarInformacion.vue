<template>
    <div class="campos">
      <h1>Ingresar informacion</h1>
        <div class="form-container">
          <v-text-field v-model="informacion" label="Digite su informacion" class="text"></v-text-field>
          <v-text-field v-model="significado" label="Digite su significado" class="text"></v-text-field>
          <v-file-input v-model="imagen" label="Agregue una imagen" accept="image/*"></v-file-input>
          <v-btn @click="GuardarDatos">Guardar informacion</v-btn>
        </div>
    </div>
  </template>
  <style scoped>
  
  .campos {
      margin-top: 15px;
  }
  .form-container {
      height: 100%;
      width: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
  }
  .form-container .text {
      width: 50%;
  }
  
  
  @media (max-width: 600px) {
    .form-container .text {
      width: 70%;
    }
  }
  </style>
    
    <script>
  import axios from 'axios';


  export default {
    data() {
      return {
        informacion: '',
        significado: '',
        imagen: null,
      };
    },
    name: 'CampoI',
    methods: {

      GuardarDatos() {
        const formData = new FormData();
        formData.append('informacion', this.informacion);
        formData.append('significado', this.significado);
        formData.append('imagen', this.imagen);
        
        axios.post('http://localhost:5000/api/guardarinfo', formData)
        .then(response => {
            console.log(response.data);
            this.informacion = '';
            this.significado = '';
            this.imagen = null;
        })
        .catch(error => {
            console.error(error)
        })
    }
  }
  };
    
    </script>
    