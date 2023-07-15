
import Vue from 'vue';
import App from './App.vue';
import VueRouter from 'vue-router';
import Vuetify from 'vuetify';
import VueSocketIO from 'vue-socket.io';
import SocketIO from 'socket.io-client';
import 'vuetify/dist/vuetify.min.css';
import 'vuetify/dist/vuetify.css';
import Home from './components/Home.vue';
import palabras from './components/palabras.vue';
import oraciones from './components/oraciones.vue';
import informacion from './components/informacion.vue';
import mapa from './components/mapa.vue';
import configuracion from './components/configuracion.vue'
import campos from './components/Campos.vue'
import IngresarPalabra from './components/ComponentesCampos/IngresarPalabra'
import ejemplo from './components/ejemplo.vue'
import '@mdi/font/css/materialdesignicons.css';


Vue.use(VueRouter);
Vue.use(Vuetify);
Vue.use(new VueSocketIO ( { 
  debug: true,
  connection: SocketIO('http://localhost:5000'), 
}));

const router = new VueRouter({
  mode: 'history',
  routes: [
    { path: '/', component: Home },
    { path: '/palabras', component: palabras },
    { path: '/oraciones', component: oraciones },
    { path: '/informacion', component: informacion },
    { path: '/mapa', component: mapa },
    {path: '/configuracion', component: configuracion },
    {path: '/Campos', component: campos,  meta: { hideNav: true },
    children: [
      {
        path: 'ingresar-palabra',
        component: IngresarPalabra,
        meta: { hideNav: true }
      }
    ]
  },
    {path: '/ejemplo', component: ejemplo}

    // Agrega más rutas para cada vista adicional que desees tener
  ],
});



const vuetify = new Vuetify();

new Vue({
  router,
  vuetify,
  render: h => h(App),
}).$mount('#app');

