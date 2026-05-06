<script setup>
import AppInput from "./AppInput.vue";
import { ref, computed } from "vue";
import { useAuthStore } from "../../stores/auth";
import { useRouter } from "vue-router";

const authStore = useAuthStore();
const router = useRouter();

const email = ref("");
const password = ref("");

const emailRef = ref(null);
const passwordRef = ref(null);

const isEmailValid = computed(() =>
  /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value),
);

const isFormValid = computed(
  () => isEmailValid.value && password.value.length >= 8,
);

const emailTouched = ref(false);
const passwordTouched = ref(false);
const isLoading = ref(false);
const serverError = ref("");

async function handleLogin() {
  if (!isFormValid.value) return;

  isLoading.value = true;
  serverError.value = "";

  try {
    await authStore.handleLogin({
      email: email.value,
      password: password.value,
    });
    router.push("/");
  } catch (error) {
    serverError.value = "Невірна електронна адреса або пароль";
  } finally {
    isLoading.value = false;
  }
}

function handleEnter() {
  if (!email.value) return;
  if (!password.value) {
    passwordRef.value?.inputRef?.focus();
    return;
  }
  handleLogin();
}

function handleForgotPassword() {
  alert("Вибачте, але відновлення паролю буде додано потім");
}
</script>

<template>
  <div class="flex flex-col items-start" @keydown.enter.prevent="handleEnter">
    <div class="flex flex-col items-start gap-6">
      <AppInput
        label="Введіть свою електронну адресу"
        placeholder="abc123@email.com"
        v-model="email"
        :error="
          emailTouched && !isEmailValid ? 'Перевірте правильність адреси' : ''
        "
        @blur="emailTouched = true"
        @update:model-value="emailTouched = false"
        autofocus
        ref="emailRef"
      />

      <AppInput
        label="Введіть пароль"
        placeholder="Пароль"
        type="password"
        v-model="password"
        :error="
          passwordTouched && password.length < 8
            ? 'Пароль має бути не менше 8 символів'
            : ''
        "
        @blur="passwordTouched = true"
        @update:model-value="passwordTouched = false"
        ref="passwordRef"
      />

      <span v-if="serverError" class="font-primary text-secondary text-error">
        {{ serverError }}
      </span>
    </div>

    <button class="btn btn-tertiary mt-4" @click="handleForgotPassword">
      Забули пароль?
    </button>

    <button
      class="btn btn-primary btn-md mt-10"
      :disabled="!isFormValid || isLoading"
      @click="handleLogin"
    >
      {{ isLoading ? "Завантаження..." : "Продовжити" }}
    </button>
  </div>
</template>
