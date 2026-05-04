<script setup>
import { ref, watch } from "vue";
import { useRouter } from "vue-router";
import { useAuthStore } from "../../stores/auth";
import RegisterEmail from "./RegisterForm/RegisterEmail.vue";
import RegisterPassword from "./RegisterForm/RegisterPassword.vue";
import RegisterInfo from "./RegisterForm/RegisterInfo.vue";

const router = useRouter();
const authStore = useAuthStore();

const step = ref(1);
const isLoading = ref(false);
const serverError = ref("");

const formData = ref({
  email: "",
  password: "",
  name: "",
  surname: "",
  city: "",
  birthday: "",
});

function onEmailNext(email) {
  formData.value.email = email;
  step.value = 2;
}

function onPasswordNext(password) {
  formData.value.password = password;
  step.value = 3;
}

function formatBirthday(value) {
  if (!value) return "";
  const [day, month, year] = value.split(".");
  return `${year}-${month}-${day}`;
}

watch(
  formData,
  () => {
    serverError.value = "";
  },
  { deep: true },
);

async function onInfoNext(info) {
  formData.value = { ...formData.value, ...info };

  isLoading.value = true;
  serverError.value = "";

  try {
    await authStore.handleRegister({
      email: formData.value.email,
      password: formData.value.password,
      password2: formData.value.password,
      name: formData.value.name,
      surname: formData.value.surname,
      city: formData.value.city,
      birthday: formatBirthday(formData.value.birthday),
    });
    router.push("/");
  } catch (error) {
    const data = error.response?.data;
    if (data?.email) {
      serverError.value = "Користувач з цією електронною адресою вже існує";
    } else {
      serverError.value = "Щось пішло не так. Спробуйте ще раз.";
    }
    step.value = 1;
  } finally {
    isLoading.value = false;
  }
}
</script>

<template>
  <RegisterEmail
    v-if="step === 1"
    @next="onEmailNext"
    @input="serverError = ''"
  />
  <RegisterPassword v-else-if="step === 2" @next="onPasswordNext" />
  <RegisterInfo
    v-else-if="step === 3"
    :is-loading="isLoading"
    @next="onInfoNext"
  />

  <span v-if="serverError" class="font-primary text-secondary text-error mt-4">
    {{ serverError }}
  </span>
</template>
