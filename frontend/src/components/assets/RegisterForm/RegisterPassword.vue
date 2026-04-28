<script setup>
import { ref, computed } from "vue";
import AppInput from "../AppInput.vue";

const emit = defineEmits(["next"]);

const password = ref("");

const isPasswordValid = computed(() => {
  const val = password.value;

  const hasMinLength = val.length >= 8;
  const hasUpperCase = /[A-Z]/.test(val);
  const hasNumber = /[0-9]/.test(val);
  const hasSpecial = /[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?№]/.test(val);

  return hasMinLength && hasUpperCase && hasNumber && hasSpecial;
});
</script>

<template>
  <div
    class="flex flex-col items-start gap-6"
    @keydown.enter.prevent="isPasswordValid && emit('next', password)"
  >
    <div class="flex flex-col gap-4">
      <AppInput
        label="Введіть пароль"
        placeholder="Пароль"
        type="password"
        v-model="password"
        autofocus
      />

      <span class="font-primary text-secondary text-gray-80"
        >Пароль повинен містити не менше 8 символів. Велику літеру, цифру та
        інші доступні символи (? % № ” !)</span
      >
    </div>
    <button
      class="btn btn-primary btn-md"
      :disabled="!isPasswordValid"
      @click="emit('next', password)"
    >
      Продовжити
    </button>
  </div>
</template>
