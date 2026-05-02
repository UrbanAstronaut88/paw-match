<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import { useAuthStore } from "../../stores/auth";
import RegisterEmail from "./RegisterForm/RegisterEmail.vue";
import RegisterOtp from "./RegisterForm/RegisterOtp.vue";
import RegisterPassword from "./RegisterForm/RegisterPassword.vue";
import RegisterInfo from "./RegisterForm/RegisterInfo.vue";

const router = useRouter();
const authStore = useAuthStore();

const step = ref(1);
const isLoading = ref(false);
const serverError = ref("");

const formData = ref({
  email: "",
  otp: "",
  password: "",
  name: "",
  lastName: "",
  birthday: "",
});

function onEmailNext(email) {
  formData.value.email = email;
  step.value = 2;
}

function onOtpNext(otp) {
  formData.value.otp = otp;
  step.value = 3;
}

function onPasswordNext(password) {
  formData.value.password = password;
  step.value = 4;
}

async function onInfoNext(info) {
  formData.value = { ...formData.value, ...info };

  isLoading.value = true;
  serverError.value = "";

  try {
    await authStore.handleRegister({
      email: formData.value.email,
      password: formData.value.password,
      first_name: formData.value.name,
      last_name: formData.value.lastName,
      birthday: formData.value.birthday,
      otp: formData.value.otp,
    });
    router.push("/");
  } catch (error) {
    serverError.value = "Щось пішло не так. Спробуйте ще раз.";
    step.value = 1;
  } finally {
    isLoading.value = false;
  }
}
</script>

<template>
  <RegisterEmail v-if="step === 1" @next="onEmailNext" />
  <RegisterOtp v-else-if="step === 2" @next="onOtpNext" />
  <RegisterPassword v-else-if="step === 3" @next="onPasswordNext" />
  <RegisterInfo
    v-else-if="step === 4"
    :is-loading="isLoading"
    @next="onInfoNext"
  />

  <span v-if="serverError" class="font-primary text-secondary text-error mt-4">
    {{ serverError }}
  </span>
</template>
