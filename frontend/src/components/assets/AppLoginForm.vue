<script setup>
import AppInput from "./AppInput.vue";
import { ref, computed } from "vue";

const email = ref("");
const password = ref("");

const emailRef = ref(null);
const passwordRef = ref(null);

const emit = defineEmits(["next"]);

const isEmailValid = computed(() =>
  /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value),
);

const isFormValid = computed(
  () => isEmailValid.value && password.value.length >= 8,
);

const emailTouched = ref(false);
const passwordTouched = ref(false);

function handleEnter() {
  if (!email.value) return;
  if (!password.value) {
    passwordRef.value?.inputRef?.focus();
    return;
  }
  if (isFormValid.value) {
    alert("✅ Усі перевірки пройдені успішно!\nДані відправляються далі.");
    emit("next", { email: email.value, password: password.value });
  }
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
    </div>

    <button class="btn btn-tertiary mt-4" @click="handleForgotPassword">
      Забули пароль?
    </button>

    <button
      class="btn btn-primary btn-md mt-10"
      :disabled="!isFormValid"
      @click="handleEnter"
    >
      Продовжити
    </button>
  </div>
</template>
