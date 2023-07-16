<template>
  <div class="container">
    <h1>Informacion</h1>
    <div class="search-container">
  <input v-model="busqueda" type="text" placeholder="Buscar informacion" @input="realizarBusqueda">
</div>
    <div class="word-container">
      <ul class="word-list">
        <li v-for="info in informacion" :key="info.info" class="word-item">
          <div class="word-box">
            <p class="word-text">{{ info.info }}</p>
            <div class="ver-mas-container">
              <button @click="verMas(info)" class="ver-mas-btn">{{ mostrarSignificado === info.significado ? 'Ver menos' : 'Ver más' }}</button>
            </div>
            <div v-if="mostrarSignificado === info.significado" class="significado">
              <p class="significado-text">Significado: {{ info.significado }}</p>
              <img v-if="info.imagen" :src="getImageUrl(info.imagen, info.formato)" :alt="info.info" class="imagen">
            </div>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  height: 100vh;
  margin-top: 4%;

}

.word-container {
  width: 80%;
  max-height: 80vh;
  overflow-y: scroll;
  border: 1px solid #ccc;
  padding: 20px;
}

.word-list {
  list-style-type: none;
  padding: 0;
}

.word-item {
  margin-bottom: 20px;
}

.word-box {
  background-color: #f0f0f0;
  padding: 10px;
  position: relative;
  border: 1px solid rgb(151, 98, 0);
  border-radius: 20px;
}

.word-text {
  font-weight: bold;
}

.ver-mas-container {
  position: absolute;
  top: 1%;
  right: 10px;
  transform: translateY(-50%);
}

.ver-mas-btn {
  background-color:rgb(151, 98, 0);
  color: rgb(255, 255, 255);
  font-weight: bold;
  padding: 5px 10px;
  border: none;
  cursor: pointer;
  border-radius: 20px;
}

.search-container {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

.search-container input {
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 16px;
  width: 400px;
}

/* Estilos para dispositivos móviles */
@media (max-width: 600px) {
  .ver-mas-btn {
    padding: 3px 8px;
    font-size: 12px;
  }
  .container {
  margin-top: 12%;
}
}

.significado {
  margin-top: 10px;
}

.significado-text {
  font-style: italic;
}
</style>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      informacion: [],
      mostrarSignificado: '',
      busqueda: '',
      InformacionOriginal: []
    };
  },
  name: 'infoC',
  mounted() {
    this.obtenerInformacion();
  },
  methods: {
    obtenerInformacion() {
      axios.get('http://localhost:5000/api/info')
        .then(response => {
          this.informacion = response.data;
          this.InformacionOriginal = [...response.data];
        })
        .catch(error => { 
          console.error(error);
        });
    },
    verMas(info) {
  if (this.mostrarSignificado === info.significado) {
    this.mostrarSignificado = '';
  } else {
    this.mostrarSignificado = info.significado;
  }
},
    getImageUrl(imagenBase64, formato) {
      return `data:image/${formato};base64,${imagenBase64}`;
    },
    realizarBusqueda() {
      if (this.busqueda) {
      this.informacion = this.informacion.filter(info => info.info.toLowerCase().includes(this.busqueda.toLowerCase()));
    } else {
      this.informacion = [...this.InformacionOriginal];
  } 
}, 
    resetearBusqueda() {
      this.busqueda= '',
      this.realizarBusqueda()

    },
  }
};
</script>
