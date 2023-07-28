
import Vue from 'vue';
import App from './App.vue';
import VueRouter from 'vue-router';
import Vuetify from 'vuetify';
import 'vuetify/dist/vuetify.min.css';
import 'vuetify/dist/vuetify.css';
import palabras from './components/palabras.vue';
import oraciones from './components/oraciones.vue';
import informacion from './components/informacion.vue';
import mapa from './components/mapa.vue';
import configuracion from './components/configuracion.vue'
import campos from './components/Campos.vue'
import IngresarPalabra from './components/ComponentesCampos/IngresarPalabra'
import IngresarOracion from './components/ComponentesCampos/IngresarOracion'
import IngresarInformacion from './components/ComponentesCampos/IngresarInformacion'
import EditarPalabra from './components/ComponentesCampos/editarComponentes/EditarPalabra'
import CambiarPalabra from './components/ComponentesCampos/editarComponentes/editarpalabra/CambiarPalabra'
import EditarOracion from './components/ComponentesCampos/editarComponentes/EditarOracion'
import CambiarOracion from './components/ComponentesCampos/editarComponentes/editaroracion/CambiarOracion'
import EditarInfo from './components/ComponentesCampos/editarComponentes/EditarInfo'
import CambiarInfo from './components/ComponentesCampos/editarComponentes/editarinfo/CambiarInfo'
import ejemplo from './components/ejemplo.vue'
import '@mdi/font/css/materialdesignicons.css';


Vue.use(VueRouter);
Vue.use(Vuetify);


const router = new VueRouter({
  mode: 'history',
  routes: [
    { path: '/', component: palabras},
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
      },
      {
        path: 'ingresar-oracion',
        component: IngresarOracion,
        meta: { hideNav: true }
      },
      {
        path: 'ingresar-info',
        component: IngresarInformacion,
        meta: { hideNav: true }
      },

      {
        path: 'editar-palabra',
        component: EditarPalabra,
        meta: { hideNav: true }
      },

      {
        path: 'editar-palabra/editar/:id',
        component: CambiarPalabra,
        meta: { hideNav: true }
      },

      {
        path: 'editar-oracion',
        component: EditarOracion,
        meta: { hideNav: true }
      },

      {
        path: 'editar-oracion/editar/:id',
        component: CambiarOracion,
        meta: { hideNav: true }
      },

      {
        path: 'editar-info',
        component: EditarInfo,
        meta: { hideNav: true }
      },

      {
        path: 'editar-info/editar/:id',
        component: CambiarInfo,
        meta: { hideNav: true }
      },


      



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

