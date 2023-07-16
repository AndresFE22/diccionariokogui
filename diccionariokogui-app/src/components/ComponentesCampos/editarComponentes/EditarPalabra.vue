<template>
    <div>
      <h1>Tabla de Palabras</h1>
      <div class="container">
        <v-data-table :headers="headers" :items="palabras" item-key="id" class="tabla-palabras">
        <template slot="item" slot-scope="{ item }">
          <tr>
            <td>{{ item[0] }}</td>
            <td>{{ item[1] }}</td>
            <td>{{ item[2] }}</td>
            <td>
            <v-icon @click="openModal(item[0])">mdi-image</v-icon>
            </td>
            <td>
                <v-btn class="editar-button" @click="editarPalabra(item[0])">Editar</v-btn>
            </td>
            <td>
                <v-btn class="eliminar-button" @click="eliminarPalabra(item[0])">Eliminar</v-btn>
            </td>
          </tr>
        </template>
      </v-data-table>
      </div>
      <v-dialog v-model="modalOpen" max-width="500px">
      <v-card>
        <img :src="selectedImage" width="500px" />
      </v-card>
    </v-dialog>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        palabras: [],
        headers: [
          { text: 'ID', value: 'id' },
          { text: 'Palabra', value: 'palabra' },
          { text: 'Significado', value: 'significado' },
          { text: 'Imagen', value: 'significado'},
          { text: 'Editar', value: 'edit' },
          { text: 'Eliminar', value: 'delete'}
          
        ],
        modalOpen: false,
        selectedImage: '',
      };
    },
    mounted() {
      this.obtenerPalabras();
    },
    methods: {
      obtenerPalabras() {
        axios
          .get('http://localhost:5000/api/showtable')
          .then((response) => {
            this.palabras = response.data;
          })
          .catch((error) => {
            console.error(error);
          });
      },
      editarPalabra(id) {
        // Redirige a la vista de edición de palabras con el ID de la palabra
        this.$router.push(`editar-palabra/editar/${id}`);
      },
      eliminarPalabra(id) {
        // Realiza una solicitud al servidor para eliminar la palabra por su ID
        axios
          .delete(`http://localhost:5000/api/palabras/${id}`)
          .then((response) => {
            console.log(response.data);
            // Actualiza la lista de palabras después de eliminar
            this.obtenerPalabras();
          })
          .catch((error) => {
            console.error(error);
          });
      },

      openModal(id) {
      axios
        .get(`http://localhost:5000/api/palabras/${id}/image`)
        .then((response) => {
        
          this.selectedImage = this.getImageUrl(response.data.imagen_base64, response.data.formato_imagen);
          this.modalOpen = true;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    getImageUrl(imagenBase64, formato) {
  return `data:image/${formato};base64,${imagenBase64}`;
}

    },
  };
  </script>
  
  <style scoped>
  .tabla-palabras {
    margin-top: 15px;
    width: 100%;
  }
  
  .editar-button {
    color: #008cff;
    background-color: #1976d2;
  }
  
  .eliminar-button {
    color: #ff2020;
    background-color: #f44336;
  }
  </style>
  