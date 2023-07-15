<template>
  <div>
    <nav class="campo-nav">
      <ul>
        <li><router-link to="/">Inicio</router-link></li>
        <li><router-link to="/Campos/ingresar-palabra">Palabras</router-link></li>
        <li><router-link to="/oraciones">Oraciones</router-link></li>
        <li><router-link to="/informacion">Información</router-link></li>
      </ul>
    </nav>
    <router-view></router-view></div>
</template>

<style scoped>
.campo-nav {
  background-color: #f0f0f0;
  padding: 10px;
}

.campo-nav ul {
  list-style-type: none;
  display: flex;
  justify-content: center;
}

.campo-nav li {
  margin-right: 10px;
}

.campo-nav a {
  text-decoration: none;
  color: #333;
  font-weight: bold;
  padding: 5px 10px;
}

.campo-nav a:hover {
  background-color: #ccc;
}
</style>

<script>
   export default {
  name: 'CamposL',

};
</script>
