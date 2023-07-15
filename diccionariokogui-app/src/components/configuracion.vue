<template>
  <div>
    <h1>Inicio de sesión</h1>
    <v-form @submit="login">
      <v-text-field v-model="username" label="Nombre de usuario"></v-text-field>
      <v-text-field v-model="password" label="Contraseña" type="password"></v-text-field>
      <v-btn type="submit">Iniciar sesión</v-btn>
    </v-form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      password: '',
    };
  },
  methods: {
  login() {
    if (this.username === 'usuario' && this.password === 'contraseña') {
      this.$router.push('/Campos');
    } else {
      // Mostrar mensaje de error de inicio de sesión
    }
  },
},
  name: 'ConfigLogin'
};
</script>
