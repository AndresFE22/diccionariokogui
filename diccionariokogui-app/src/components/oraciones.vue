<template>
  <div class="container">
    <h1>Oraciones</h1>
    <div class="search-container">
      <input v-model="busqueda" type="text" placeholder="Buscar oracion" @input="realizarBusqueda">
    </div>
    <div class="word-container">
      <ul class="word-list">
        <li v-for="oracion in oraciones" :key="oracion.oracion" class="word-item">
          <div class="word-box">
            <p class="word-text">{{ oracion.oracion }}</p>
            <div class="ver-mas-container">
              <transition name="fade">
                <button @click="verMas(oracion)" class="ver-mas-btn">{{ mostrarSignificado === oracion.significado ? 'Ver menos' : 'Ver más' }}</button>
              </transition>
            </div>
            <transition name="fade">
              <div v-if="mostrarSignificado === oracion.significado" class="significado">
                <p class="significado-text">Significado: {{ oracion.significado }}</p>
                <img v-if="oracion.imagen" :src="getImageUrl(oracion.imagen, oracion.formato)" :alt="oracion.oracion" class="imagen">
              </div>
            </transition>
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

.imagen {
  width: 400px; 
  height: auto; 
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
  background-color: rgb(151, 98, 0);
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

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s;
}

.fade-enter,
.fade-leave-to {
  opacity: 0;
}
</style>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      oraciones: [],
      mostrarSignificado: '',
      busqueda: '',
      oracionesOriginal: []
    };
  },
  name: 'oracionesC',
  mounted() {
    this.obtenerOraciones();
  },
  methods: {
    obtenerOraciones() {
      axios.get('http://localhost:5000/api/oraciones')
        .then(response => {
          this.oraciones = response.data;
          this.oracionesOriginal = [...response.data];
        })
        .catch(error => { 
          console.error(error);
        });
    },
    verMas(oracion) {
      if (this.mostrarSignificado === oracion.significado) {
        this.mostrarSignificado = '';
      } else {
        this.mostrarSignificado = oracion.significado;
      }
    },
    getImageUrl(imagenBase64, formato) {
      return `data:image/${formato};base64,${imagenBase64}`;
    },
    realizarBusqueda() {
      if (this.busqueda) {
        this.oraciones = this.oraciones.filter(oracion => oracion.oracion.toLowerCase().includes(this.busqueda.toLowerCase()));
      } else {
        this.oraciones = [...this.oracionesOriginal];
      } 
    },
    resetearBusqueda() {
      this.busqueda = '';
      this.realizarBusqueda();
    },
  }
};
</script>
