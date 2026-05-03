<script setup>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import AppPageLayout from "./assets/AppPageLayout.vue";
import AppInput from "./assets/AppInput.vue";
import { useAuthStore } from "../stores/auth";
import { me, changePassword } from "../api/auth";
import { http } from "../api/http";

const router = useRouter();
const authStore = useAuthStore();

const isLoading = ref(false);
const profileError = ref("");
const profileSuccess = ref("");
const passwordError = ref("");
const passwordSuccess = ref("");

const profile = ref({
  name: "",
  surname: "",
  birthday: "",
  city: "",
  avatar: null,
});

const passwordForm = ref({
  oldPassword: "",
  newPassword: "",
});

onMounted(async () => {
  try {
    const data = await me();
    profile.value = {
      name: data.profile?.name || "",
      surname: data.profile?.surname || "",
      birthday: data.profile?.birthday || "",
      city: data.profile?.city || "",
      avatar: data.profile?.avatar || null,
    };
  } catch (error) {
    console.error("Помилка завантаження профілю:", error);
  }
});

async function saveProfile() {
  isLoading.value = true;
  profileError.value = "";
  profileSuccess.value = "";

  try {
    await http.patch("/auth/me/", {
      profile: {
        name: profile.value.name,
        surname: profile.value.surname,
        birthday: profile.value.birthday,
        city: profile.value.city,
      },
    });
    profileSuccess.value = "Збережено";
  } catch (error) {
    profileError.value = "Помилка збереження";
  } finally {
    isLoading.value = false;
  }
}

async function savePassword() {
  passwordError.value = "";
  passwordSuccess.value = "";

  if (passwordForm.value.newPassword.length < 8) {
    passwordError.value = "Пароль має бути не менше 8 символів";
    return;
  }

  try {
    await changePassword({
      old_password: passwordForm.value.oldPassword,
      new_password: passwordForm.value.newPassword,
    });
    passwordSuccess.value = "Пароль змінено";
    passwordForm.value = { oldPassword: "", newPassword: "" };
  } catch (error) {
    passwordError.value = "Невірний старий пароль";
  }
}

async function handleLogout() {
  await authStore.handleLogout();
  router.push("/");
}
</script>

<template>
  <AppPageLayout @back="router.back()">
    <div class="col-start-5 col-span-4 row-start-2 flex flex-col gap-10 pb-20">
      <div class="flex flex-col gap-6">
        <h2 class="font-primary text-h2 text-gray-100">Трішки про тебе</h2>

        <div class="flex justify-center">
          <div class="w-16 h-16 rounded-full overflow-hidden bg-gray-20">
            <img
              v-if="profile.avatar"
              :src="profile.avatar"
              alt="avatar"
              class="w-full h-full object-cover"
            />
            <span v-else class="block w-full h-full bg-gray-20" />
          </div>
        </div>

        <div class="flex flex-col gap-4">
          <AppInput placeholder="Ім'я" v-model="profile.name" />
          <AppInput placeholder="Прізвище" v-model="profile.surname" />
          <AppInput placeholder="ДД.ММ.РРРР" v-model="profile.birthday" />
          <AppInput placeholder="Місто" v-model="profile.city" />
        </div>

        <span
          v-if="profileError"
          class="font-primary text-secondary text-error"
          >{{ profileError }}</span
        >
        <span
          v-if="profileSuccess"
          class="font-primary text-secondary text-success"
          >{{ profileSuccess }}</span
        >

        <button
          class="btn btn-md btn-secondary self-start"
          :disabled="isLoading"
          @click="saveProfile"
        >
          Зберегти
        </button>
      </div>

      <div class="flex flex-col gap-6">
        <h2 class="font-primary text-h2 text-gray-100">Введіть пароль</h2>

        <div class="flex flex-col gap-4">
          <AppInput
            placeholder="Старий пароль"
            type="password"
            v-model="passwordForm.oldPassword"
          />
          <AppInput
            placeholder="Новий пароль"
            type="password"
            v-model="passwordForm.newPassword"
          />
        </div>

        <span
          v-if="passwordError"
          class="font-primary text-secondary text-error"
          >{{ passwordError }}</span
        >
        <span
          v-if="passwordSuccess"
          class="font-primary text-secondary text-success"
          >{{ passwordSuccess }}</span
        >

        <button
          class="btn btn-md btn-secondary self-start"
          @click="savePassword"
        >
          Зберегти
        </button>
      </div>

      <div class="flex flex-col gap-4">
        <h2 class="font-primary text-h2 text-gray-100">Вийти з акаунту?</h2>
        <button
          class="btn btn-md btn-secondary self-start"
          @click="handleLogout"
        >
          Вийти
        </button>
      </div>
    </div>
  </AppPageLayout>
</template>
