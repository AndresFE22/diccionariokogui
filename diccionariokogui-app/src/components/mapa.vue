<template>
  <div class="margin">
    <h1>Mapa de acceso a Taiku</h1>
    <div class="map-container">
      <img src="../assets/mapa.png" alt="Mapa" class="map-image">
    </div>
  </div>
</template>

<style>

.margin {
  margin-top: 4%;
}

.imagen {
  width: 400px; 
  height: auto; 
}

.map-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 10%;
}

.map-image {
  max-width: 100%;
  max-height: 100%;
}

@media (max-width: 600px) {
  .margin {
  margin-top: 14%;
}
}
</style>

<script>
export default {
  name: 'VistaMapa',
};
</script>
