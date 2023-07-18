<template>
  <div id="app">
    <v-app>
      <v-app-bar app v-if="!$route.meta.hideNav">
        <img src="./assets/UNICOR.png" alt="" class="imgunicor">
        <v-spacer></v-spacer>
        <v-toolbar-title style="font-weight: bold;">DICCIONARIO LENGUA KOGUI</v-toolbar-title>
        <v-spacer></v-spacer>
        <img src="./assets/gicafs.jpeg" alt="" class="imggicafs">
        <v-spacer></v-spacer>
        <img src="./assets/lexicon.png" alt="" class="imggicafs">
        <v-spacer></v-spacer>
        <v-btn icon to="/configuracion">
          <v-icon>mdi-account</v-icon>
        </v-btn>
      </v-app-bar>
      <v-main class="text-center">
        <nav v-if="!$route.meta.hideNav" class="nav-container">
          <div :class="{'active': isActive('/palabras')}">
            <router-link
              to="/palabras"
              class="nav-link"
              :class="{ 'active': isActive('/palabras') }"
            >
              <span class="nav-link-text"><h4>Palabras</h4></span>
            </router-link>
          </div>
          <div :class="{'active': isActive('/oraciones')}">
            <router-link
              to="/oraciones"
              class="nav-link"
              :class="{ 'active': isActive('/oraciones') }"
            >
              <span class="nav-link-text"><h4>Oraciones</h4></span>
            </router-link>
          </div>
          <div :class="{'active': isActive('/informacion')}">
            <router-link
              to="/informacion"
              class="nav-link"
              :class="{ 'active': isActive('/informacion') }"
            >
              <span class="nav-link-text"><h4>Información</h4></span>
            </router-link>
          </div>
          <div :class="{'active': isActive('/mapa')}">
            <router-link
              to="/mapa"
              class="nav-link"
              :class="{ 'active': isActive('/mapa') }"
            >
              <span class="nav-link-text"><h4>Mapa</h4></span>
            </router-link>
          </div>
        </nav>
        <transition name="slide" mode="out-in">
          <router-view>
          </router-view>
        </transition>
      </v-main>
    </v-app>
  </div>
</template>

<style scoped>
.slide-enter-active,
.slide-leave-active {
  transition: all 0.5s;
}

.slide-enter,
.slide-leave-to {
  opacity: 0;
  transform: translateX(-50px);
}

.imgunicor {
  width: 2%;
}


.imggicafs {
  width: 6%;
}


nav {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: rgb(255, 255, 255);
  position: fixed;
  top: 64px; /* Ajusta la altura según el tamaño del app bar */
  left: 0;
  right: 0;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

nav div {
  flex: 1;
  height: 100%;
}

.nav-container {
  display: flex;
  flex-wrap: wrap;
}

.nav-link {
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 18px;
  padding: 10px;
  cursor: pointer;
  transition: background-color 0.3s;
  text-decoration: none;
  flex-basis: 20%; /* Ajustar según el número de enlaces */
  box-sizing: border-box;
}

.nav-link-text {
  text-decoration: none;
  color: rgba(0, 0, 0, 0.486);
}

.nav-link:hover {
  background-color: rgba(97, 26, 26, 0.26);
}

.active .nav-link-text {
  color: rgb(151, 98, 0); 
}

.active .nav-link {
  background-color: #e4e4e4; 
}

@media (max-width: 600px) {
  .nav-link {
    flex-basis: 50%; 
  }
  .imgunicor {
    width: 7%;
  }

  .imggicafs {
    width: 14%;
  }
}
</style>

<script>
export default {
  methods: {
    isActive(route) {
      return this.$route.path === route;
    }
  }
};
</script>
