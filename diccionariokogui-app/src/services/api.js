import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://localhost:3000/',
  headers: {
    'Content-Type': 'application/json',
  },
});

// Enviar los datos de Campos al backend
export function guardarDatosCampos(datos) {
  return apiClient.post('/campos', datos);
}

// Obtener los datos de Campos desde el backend
export function obtenerDatosCampos() {
  return apiClient.get('/campos');
}
