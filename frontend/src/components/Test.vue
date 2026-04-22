<script setup>
import viteLogo from "../assets/vite.svg";
import heroImg from "../assets/hero.png";
import vueLogo from "../assets/vue.svg";
import AppPasswordInput from "./assets/AppPasswordInput.vue";
import AppOtpInput from "./assets/AppOtpInput.vue";
</script>

<template>
  <div class="input">
    <AppPasswordInput label="Введіть пароль" />
  </div>

  <div class="input">
    <AppPasswordInput
      class="input-success"
      label="Введіть пароль"
      disabled=""
    />
  </div>

  <div class="input">
    <AppPasswordInput class="input-success" label="Введіть пароль" />
  </div>

  <div class="input">
    <AppPasswordInput class="input-error" label="Введіть пароль" />
  </div>

  <div class="input">
    <AppOtpInput label="Код був надісланий на вашу адресу" />
  </div>

  <div class="input">
    <AppOtpInput
      class="input-success"
      label="Код був надісланий на вашу адресу"
      disabled=""
    />
  </div>

  <div class="input">
    <AppOtpInput
      class="input-success"
      label="Код був надісланий на вашу адресу"
    />
  </div>

  <div class="input">
    <AppOtpInput
      class="input-error"
      label="Код був надісланий на вашу адресу"
    />
  </div>
</template>

<style>
.input {
  padding: 15px;
}
</style>
