<template>
    <div class="campos">
      <h1>Ingresar oraciones</h1>
        <div class="form-container">
          <v-text-field v-model="oracion" label="Digite su oracion" class="text"></v-text-field>
          <v-text-field v-model="significado" label="Digite su significado" class="text"></v-text-field>
          <v-file-input v-model="imagen" label="Agregue una imagen" accept="image/*"></v-file-input>
          <v-btn @click="GuardarDatos">Guardar oracion</v-btn>
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
        oracion: '',
        significado: '',
        imagen: null,
      };
    },
    name: 'CampoO',
    methods: {

      GuardarDatos() {
        const formData = new FormData();
        formData.append('oracion', this.oracion);
        formData.append('significado', this.significado);
        formData.append('imagen', this.imagen);
        
        axios.post('http://localhost:5000/api/guardaroracion', formData)
        .then(response => {
            console.log(response.data);
            this.oracion = '';
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
    