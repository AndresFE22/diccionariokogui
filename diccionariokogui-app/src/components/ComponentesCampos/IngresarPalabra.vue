<template>
    <div class="campos">
      <h1>Ingresar palabras</h1>
        <div class="form-container">
          <v-text-field v-model="palabra" label="Digite su palabra" class="text"></v-text-field>
          <v-text-field v-model="significado" label="Digite su significado" class="text"></v-text-field>
          <v-file-input v-model="imagen" label="Agregue una imagen" accept="image/*"></v-file-input>
          <v-btn @click="GuardarDatos">Guardar palabra</v-btn>
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
        palabra: '',
        significado: '',
        imagen: null,
      };
    },
    name: 'CampoL',
    methods: {

      GuardarDatos() {
        const formData = new FormData();
        formData.append('palabra', this.palabra);
        formData.append('significado', this.significado);
        formData.append('imagen', this.imagen);
        
        axios.post('http://localhost:5000/api/guardarpalabras', formData)
        .then(response => {
            console.log(response.data);
            this.palabra = '';
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
    