<script setup>
import { ref } from "vue";
import RegisterEmail from "./RegisterForm/RegisterEmail.vue";
import RegisterOtp from "./RegisterForm/RegisterOtp.vue";
import RegisterPassword from "./RegisterForm/RegisterPassword.vue";
import RegisterInfo from "./RegisterForm/RegisterInfo.vue";

const step = ref(1);

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

function onInfoNext(info) {
  formData.value = { ...formData.value, ...info };
  // send data to server
  console.log("Реєстрація:", formData.value);
}
</script>

<template>
  <RegisterEmail v-if="step === 1" @next="onEmailNext" />
  <RegisterOtp v-else-if="step === 2" @next="onOtpNext" />
  <RegisterPassword v-else-if="step === 3" @next="onPasswordNext" />
  <RegisterInfo v-else-if="step === 4" @next="onInfoNext" />
</template>
