<script setup>
import { ref, computed } from "vue";
import AppInput from "../AppInput.vue";

defineProps({
  serverError: { type: String, default: "" },
});

const emit = defineEmits(["next", "input"]);

const email = ref("");
const emailTouched = ref(false);
const emailRef = ref(null);

const isEmailValid = computed(() =>
  /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value),
);
</script>

<template>
  <div
    class="flex flex-col items-start gap-6"
    @keydown.enter.prevent="isEmailValid && emit('next', email)"
  >
    <AppInput
      label="Введіть свою електронну адресу"
      placeholder="abc123@email.com"
      v-model="email"
      :error="
        emailTouched && !isEmailValid ? 'Перевірте правильність адреси' : ''
      "
      @blur="emailTouched = true"
      @update:model-value="
        emailTouched = false;
        emit('input');
      "
      autofocus
      ref="emailRef"
    />
    <button
      class="btn btn-primary btn-md"
      :disabled="!isEmailValid"
      @click="emit('next', email)"
    >
      Продовжити
    </button>
  </div>
</template>
