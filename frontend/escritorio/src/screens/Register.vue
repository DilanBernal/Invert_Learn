<script setup>
import { ref } from 'vue';

const formState = ref({
  name: '',
  email: '',
  password: '',
  confirmPassword: '',
  preferredCurrency: 'USD',
});

const showPassword = ref(false);
const showConfirmPassword = ref(false);
const passwordMatch = ref(true);

const handleInputChange = (event) => {
  const { name, value } = event.target;
  formState.value[name] = value;
  if (name === 'password' || name === 'confirmPassword') {
    passwordMatch.value = formState.value.password === formState.value.confirmPassword;
  }
};

const togglePasswordVisibility = () => {
  showPassword.value = !showPassword.value;
};

const toggleConfirmPasswordVisibility = () => {
  showConfirmPassword.value = !showConfirmPassword.value;
};

const handleSubmit = (event) => {
  event.preventDefault();
  if (formState.value.password !== formState.value.confirmPassword) {
    passwordMatch.value = false;
    return;
  }
  passwordMatch.value = true;
  console.log('Form submitted:', formState.value);
  // Add your registration logic here
};
</script>

<template>
  <div class="container mt-5">
    <div class="row justify-content-center">
      <div class="col-md-6">
        <div class="card">
          <div class="card-body">
            <h3 class="card-title text-center mb-4">Register</h3>
            <form @submit="handleSubmit">
              <div class="mb-3">
                <label for="nameInput" class="form-label">Name</label>
                <input type="text" class="form-control" id="nameInput" name="name" :value="formState.name" @input="handleInputChange" required>
              </div>
              <div class="mb-3">
                <label for="emailInput" class="form-label">Email address</label>
                <input type="email" class="form-control" id="emailInput" name="email" :value="formState.email" @input="handleInputChange" required>
              </div>
              <div class="mb-3">
                <label for="passwordInput" class="form-label">Password</label>
                <div class="input-group">
                  <input :type="showPassword ? 'text' : 'password'" class="form-control" id="passwordInput" name="password" :value="formState.password" @input="handleInputChange" required>
                  <button class="btn btn-outline-secondary" type="button" @click="togglePasswordVisibility">
                    <i :class="showPassword ? 'bi bi-eye-slash' : 'bi bi-eye'"></i>
                  </button>
                </div>
              </div>
              <div class="mb-3">
                <label for="confirmPasswordInput" class="form-label">Confirm Password</label>
                <div class="input-group">
                  <input :type="showConfirmPassword ? 'text' : 'password'" class="form-control" id="confirmPasswordInput" name="confirmPassword" :value="formState.confirmPassword" @input="handleInputChange" required>
                  <button class="btn btn-outline-secondary" type="button" @click="toggleConfirmPasswordVisibility">
                    <i :class="showConfirmPassword ? 'bi bi-eye-slash' : 'bi bi-eye'"></i>
                  </button>
                </div>
                <div v-if="!passwordMatch" class="text-danger mt-2">Passwords do not match.</div>
              </div>
              <div class="mb-3">
                <label for="currencySelect" class="form-label">Preferred Currency</label>
                <select class="form-select" id="currencySelect" name="preferredCurrency" :value="formState.preferredCurrency" @change="handleInputChange">
                  <option value="USD">USD</option>
                  <option value="EUR">EUR</option>
                  <option value="COL">COL</option>
                  <!-- Add more currency options as needed -->
                </select>
              </div>
              <div class="d-grid gap-2">
                <button type="submit" class="btn btn-primary">Register</button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped></style>