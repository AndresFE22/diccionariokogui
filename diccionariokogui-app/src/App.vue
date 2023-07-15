<template>
  <div id="app">
    <v-app>
    <v-app-bar app color="primary" dark v-if="!$route.meta.hideNav">
      <v-toolbar-title>Diccionario Kogui</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn icon to="/configuracion">
          <v-icon>mdi-cog</v-icon>
      </v-btn>
    </v-app-bar>
    <v-main class="text-center">
      <nav v-if="!$route.meta.hideNav">
        <div>
          <router-link to="/">
          Inicio
          </router-link>
        </div>
        <div>
          <router-link to="/palabras">
          palabras
          </router-link>
        </div>
        <div>
          <router-link to="/oraciones">
          oraciones
          </router-link>
        </div>
        <div>
          <router-link to="/informacion">
          informacion
          </router-link></div>
        <div>
          <router-link to="/mapa">
          mapa
          </router-link>
        </div>
      
    </nav>
    <transition name="slide" mode="out-in">
      <router-view></router-view>
    </transition>
    </v-main>
  </v-app>
  
  </div>
</template>



<style>
.slide-enter-active,
.slide-leave-active {
  transition: all 0.5s;
}

.slide-enter,
.slide-leave-to {
  opacity: 0;
  transform: translateX(-50px);
}

nav {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  background-color: rgb(233, 233, 233);
  height: 8%;
}

nav div {
  width: 100%;
  height: 100%;
  
}

mav div:hover {
  background-color: rgb(221, 221, 221);
}


</style>

<script>

</script>

