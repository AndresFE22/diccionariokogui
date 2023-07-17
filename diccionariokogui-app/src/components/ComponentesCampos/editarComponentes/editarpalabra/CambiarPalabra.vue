<template>
    <div class="campos">
      <h1>editar palabras</h1>
        <div class="form-container">
          <v-text-field v-model="nuevaPalabra" label="Digite su palabra" class="text"></v-text-field>
          <v-text-field v-model="nuevoSignificado" label="Digite su significado" class="text"></v-text-field>
          <v-btn @click="editarPalabra">Editar información</v-btn>
          <br>
          <router-link to="/Campos/editar-palabra"><v-btn>Regresar</v-btn></router-link>
          
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
      nuevaPalabra: '',
      nuevoSignificado: ''
    };
  },
  
  methods: {
    editarPalabra() {
      const id = this.$route.params.id;

      const datos = {
        palabra: this.nuevaPalabra,
        significado: this.nuevoSignificado
      };

      axios.put(`http://localhost:5000/api/palabras/${id}`, datos)
        .then(response => {
          console.log(response.data);
          this.nuevaPalabra = '';
          this.nuevoSignificado = '';
        })
        .catch(error => {
          console.error(error);
        });
    }
  }
};
    </script>
    