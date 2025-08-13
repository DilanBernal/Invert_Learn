<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useRouter, useRoute } from 'vue-router';

const router = useRouter();
const route = useRoute();

const formState = ref({
  name: '',
  email: '',
  preferredCurrency: '',
});

const loading = ref(true);
const error = ref(null);

// Obtener el ID del usuario desde los parámetros de la ruta
const userId = route.params.id;

const handleInputChange = (event) => {
  const { name, value } = event.target;
  formState.value[name] = value;
  
  // Convertir moneda a mayúsculas automáticamente
  if (name === 'preferredCurrency') {
    formState.value[name] = value.toUpperCase();
  }
};

const getUserById = async () => {
  try {
    loading.value = true;
    error.value = null;
    
    const response = await axios.get(`http://localhost:8000/usuario/${userId}`);
    const userData = response.data;
    
    console.log('Usuario obtenido:', response);
    
    // Cargar los datos del usuario en el formulario
    formState.value.name = userData.nombre || '';
    formState.value.email = userData.email || '';
    formState.value.preferredCurrency = userData.moneda_preferida || '';
    
  } catch (err) {
    console.error('Error al obtener el usuario:', err);
    error.value = 'Error al cargar los datos del usuario';
    
    if (err.response && err.response.status === 404) {
      error.value = 'Usuario no encontrado';
    }
  } finally {
    loading.value = false;
  }
};

const handleSubmit = async (event) => {
  event.preventDefault();
  
  try {
    const usuario = {
      nombre: formState.value.name,
      email: formState.value.email,
      moneda_preferida: formState.value.preferredCurrency,
    };
    
    console.log('Actualizando usuario:', usuario);
    
    const response = await axios.put(
      `http://localhost:8000/usuario/${userId}`,
      usuario
    );
    
    console.log('Usuario actualizado:', response);
    
    router.push('/users-list'); 
    
  } catch (err) {
    console.error('Error al actualizar el usuario:', err);
    
    if (err.response && err.response.status === 400) {
      alert("Error: " + err.response.data.detail);
      return;
    }
    
    if (err.response && err.response.status === 404) {
      alert("Error: Usuario no encontrado");
      return;
    }
    
    alert("Error al actualizar el usuario. Por favor intenta nuevamente.");
  }
};

const goBack = () => {
  router.back();
};

// Cargar datos del usuario al montar el componente
onMounted(() => {
  if (!userId) {
    error.value = 'ID de usuario no válido';
    loading.value = false;
    return;
  }
  getUserById();
});
</script>

<template>
  <div class="container mt-5">
    <div class="row justify-content-center">
      <div class="col-md-6">
        <div class="card">
          <div class="card-body">
            <div class="d-flex justify-content-between align-items-center mb-4">
              <h3 class="card-title mb-0">Editar Usuario</h3>
              <button class="btn btn-outline-secondary" @click="goBack">
                <i class="bi bi-arrow-left"></i> Volver
              </button>
            </div>

            <!-- Estado de carga -->
            <div v-if="loading" class="text-center">
              <div class="spinner-border text-primary" role="status">
                <span class="visually-hidden">Cargando...</span>
              </div>
              <p class="mt-2">Cargando datos del usuario...</p>
            </div>

            <!-- Estado de error -->
            <div v-else-if="error" class="alert alert-danger" role="alert">
              <i class="bi bi-exclamation-triangle"></i> {{ error }}
              <div class="mt-2">
                <button class="btn btn-outline-danger btn-sm" @click="getUserById">
                  <i class="bi bi-arrow-clockwise"></i> Reintentar
                </button>
              </div>
            </div>

            <!-- Formulario -->
            <form v-else @submit="handleSubmit">
              <div class="mb-3">
                <label for="nameInput" class="form-label">
                  <i class="bi bi-person"></i> Nombres y Apellidos
                </label>
                <input 
                  type="text" 
                  class="form-control" 
                  id="nameInput" 
                  name="name" 
                  :value="formState.name"
                  @input="handleInputChange" 
                  placeholder="Ingresa tu nombre completo"
                  required
                >
              </div>

              <div class="mb-3">
                <label for="emailInput" class="form-label">
                  <i class="bi bi-envelope"></i> Correo electrónico
                </label>
                <input 
                  type="email" 
                  class="form-control" 
                  id="emailInput" 
                  name="email" 
                  :value="formState.email"
                  @input="handleInputChange" 
                  placeholder="usuario@ejemplo.com"
                  required
                >
              </div>

              <div class="mb-3">
                <label for="currencyInput" class="form-label">
                  <i class="bi bi-currency-exchange"></i> Tipo de moneda preferida
                </label>
                <input 
                  type="text" 
                  class="form-control" 
                  id="currencyInput" 
                  name="preferredCurrency" 
                  :value="formState.preferredCurrency"
                  @input="handleInputChange" 
                  placeholder="COP, USD, EUR"
                  minlength="1"
                  maxlength="3"
                  required
                >
                <div class="form-text">
                  <i class="bi bi-info-circle"></i> Usa el código de 3 letras (ej: USD, EUR, COP)
                </div>
              </div>

              <div class="d-grid gap-2">
                <button type="submit" class="btn btn-primary">
                  <i class="bi bi-check-lg"></i> Actualizar Usuario
                </button>
                <button type="button" class="btn btn-outline-secondary" @click="goBack">
                  <i class="bi bi-x-lg"></i> Cancelar
                </button>
              </div>
            </form>

            <!-- Información adicional -->
            <div class="mt-3 text-muted small">
              <i class="bi bi-info-circle"></i> 
              Usuario ID: {{ userId }}
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.card {
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  border: none;
}

.form-control:focus {
  border-color: #0d6efd;
  box-shadow: 0 0 0 0.2rem rgba(13, 110, 253, 0.25);
}

.btn-primary {
  background: linear-gradient(135deg, #0d6efd 0%, #0a58ca 100%);
  border: none;
}

.btn-primary:hover {
  background: linear-gradient(135deg, #0a58ca 0%, #084298 100%);
}

.spinner-border {
  width: 2rem;
  height: 2rem;
}

.form-label {
  font-weight: 500;
  color: #495057;
}

.form-text {
  font-size: 0.875rem;
}
</style>