<template>
  <div class="fondo">
    <div class="cont">
      <div class="conttitle">
      <div class="titles">
        <h1 class="title"><h1>Diccionario Kogui</h1></h1>
      </div>
      <div class="desc">
        <h4><p class="description">Aquí puedes buscar información sobre la cultura Kogui</p></h4>
      </div>
    </div>
    <div class="buttons">
      <router-link to="/palabras" class="button">Palabras</router-link>
      <router-link to="/oraciones" class="button">Oraciones</router-link>
      <router-link to="/informacion" class="button">Información</router-link>
      <router-link to="/mapa" class="button">Mapa</router-link>
    </div>
    </div>
  </div>
</template>

<style scoped>


.cont {
  display: flex;
  flex-direction: column;
}
.conttitle {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  width: 100%;
  height: auto;
  margin-top: 5%;
}

.title {
  font-size: 1000pt;
  font-weight: bold;
  color: black;
  margin-bottom: 10%;
}




.button {
  padding: 10px 20px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin-top: 10%;
}
.button:hover {
  background-color: #45a049;
}
.button:active {
  background-color: #3e8e41;
}

.fondo {
  background-image: url('../assets/fondo.jpg');
  background-size: cover;
  background-position: center;
  height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.buttons {
  display: flex;
  flex-direction: column;
  justify-content: center;
}
</style>

<script>
export default {
  name: 'HomePage',
};
</script>
