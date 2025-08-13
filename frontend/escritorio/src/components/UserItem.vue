<template>
  <div class="card mb-3">
    <div class="card-body d-flex justify-content-between align-items-center">
      <div>
        <h5 class="card-title">ID: {{ user.usuario_id }}</h5>
        <p class="card-text"><strong>Nombre:</strong> {{ user.nombre }}</p>
        <p class="card-text"><strong>Email:</strong> {{ user.email }}</p>
        <p class="card-text">
          <strong>Moneda Preferida:</strong> {{ user.moneda_preferida }}
        </p>
      </div>
      <div class="btn-group" role="group">
        <button
          class="btn btn-danger"
          data-bs-toggle="tooltip"
          data-bs-placement="top"
          title="Eliminar Usuario"
          @click="$emit('delete-user', user.usuario_id)"
        >
          <i class="bi bi-trash"></i>
        </button>
        <button
          class="btn btn-primary"
          data-bs-toggle="tooltip"
          data-bs-placement="top"
          title="Editar Usuario"
          @click="$emit('edit-user', user.usuario_id)"
        >
          <i class="bi bi-pencil"></i>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    user: {
      type: Object,
      required: true,
    },
  },
  emits: ["delete-user", "edit-user"],
};
</script>

<style scoped>
.btn-group .btn {
  transition: transform 0.2s ease-in-out;
}

.btn-group .btn:hover {
  transform: scale(1.1);
}
</style>