<script setup>
import { ref, onMounted, computed } from "vue";
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

const savedProfile = ref(null);

const birthdayTouched = ref(false);

const passwordForm = ref({
  oldPassword: "",
  newPassword: "",
});

onMounted(async () => {
  try {
    const data = await me();
    const rawBirthday = data.profile?.birthday || "";
    let birthday = "";
    if (rawBirthday) {
      const [year, month, day] = rawBirthday.split("-");
      birthday = `${day}.${month}.${year}`;
    }

    profile.value = {
      name: data.profile?.name || "",
      surname: data.profile?.surname || "",
      birthday,
      city: data.profile?.city || "",
      avatar: data.profile?.avatar || null,
    };

    savedProfile.value = { ...profile.value };
  } catch (error) {
    console.error("Помилка завантаження профілю:", error);
  }
});

const avatarFile = ref(null);

function handleAvatarChange(event) {
  avatarFile.value = event.target.files[0];
  profile.value.avatar = URL.createObjectURL(avatarFile.value);
}

async function saveProfile() {
  isLoading.value = true;
  profileError.value = "";
  profileSuccess.value = "";

  try {
    const [day, month, year] = profile.value.birthday.split(".");
    const formattedBirthday = `${year}-${month}-${day}`;

    const formData = new FormData();
    formData.append("name", profile.value.name);
    formData.append("surname", profile.value.surname);
    formData.append("birthday", formattedBirthday);
    formData.append("city", profile.value.city);
    if (avatarFile.value) {
      formData.append("avatar", avatarFile.value);
    }

    await http.patch("/auth/me/", formData, {
      headers: { "Content-Type": "multipart/form-data" },
    });
    await authStore.fetchMe();
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
      new_password2: passwordForm.value.newPassword,
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

const isProfileChanged = computed(() => {
  if (!savedProfile.value) return false;
  return (
    profile.value.name !== savedProfile.value.name ||
    profile.value.surname !== savedProfile.value.surname ||
    profile.value.birthday !== savedProfile.value.birthday ||
    profile.value.city !== savedProfile.value.city ||
    avatarFile.value !== null
  );
});

const isPasswordFilled = computed(
  () =>
    passwordForm.value.oldPassword.length > 0 &&
    passwordForm.value.newPassword.length >= 8,
);

const isBirthdayValid = computed(() => {
  const regex = /^\d{2}\.\d{2}\.\d{4}$/;
  if (!regex.test(profile.value.birthday)) return false;
  const [day, month, year] = profile.value.birthday.split(".").map(Number);
  const date = new Date(year, month - 1, day);
  return (
    date.getFullYear() === year &&
    date.getMonth() === month - 1 &&
    date.getDate() === day &&
    date < new Date()
  );
});

const birthdayRef = ref(null);

function handleBirthdayInput(value) {
  birthdayTouched.value = false;
  let cleaned = value.replace(/\D/g, "");
  let day = cleaned.slice(0, 2);
  let month = cleaned.slice(2, 4);
  let year = cleaned.slice(4, 8);

  if (day.length === 2) {
    const d = parseInt(day);
    if (d > 31) day = "31";
    if (d === 0) day = "01";
  }
  if (month.length === 2) {
    const m = parseInt(month);
    if (m > 12) month = "12";
    if (m === 0) month = "01";
  }

  let formatted = day;
  if (cleaned.length > 2) formatted += "." + month;
  if (cleaned.length > 4) formatted += "." + year;

  profile.value.birthday = formatted;

  if (birthdayRef.value?.inputRef) {
    birthdayRef.value.inputRef.value = formatted;
  }
}
</script>

<template>
  <div
    class="grid grid-cols-12 gap-x-8 gap-y-10 items-start content-start pt-10"
  >
    <div class="col-start-5 col-span-4 row-start-2 flex flex-col gap-10 pb-20">
      <div class="flex flex-col gap-8">
        <h2 class="font-primary text-h1 text-gray-100 mb-4">Трішки про тебе</h2>

        <div class="flex justify-center">
          <div
            class="w-20.5 h-20.5 rounded-full overflow-hidden bg-gray-20 cursor-pointer"
            @click="$refs.avatarInput.click()"
          >
            <img
              v-if="profile.avatar"
              :src="profile.avatar"
              alt="avatar"
              class="w-full h-full object-cover"
            />
            <span v-else class="block w-full h-full bg-gray-20" />
          </div>
          <input
            ref="avatarInput"
            type="file"
            accept="image/*"
            class="hidden"
            @change="handleAvatarChange"
          />
        </div>

        <div class="flex flex-col gap-4">
          <AppInput placeholder="Ім'я" v-model="profile.name" />
          <AppInput placeholder="Прізвище" v-model="profile.surname" />
          <AppInput
            ref="birthdayRef"
            placeholder="ДД.ММ.РРРР"
            maxlength="10"
            inputmode="numeric"
            :model-value="profile.birthday"
            :error="
              birthdayTouched && !isBirthdayValid
                ? 'Введіть коректну дату народження'
                : ''
            "
            @blur="birthdayTouched = true"
            @update:model-value="handleBirthdayInput"
          />
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
          class="btn btn-md btn-primary self-start"
          :disabled="isLoading || !isProfileChanged"
          @click="saveProfile"
        >
          Зберегти
        </button>
      </div>

      <div class="flex flex-col gap-4">
        <h2 class="font-primary text-h3 text-gray-100">Введіть пароль</h2>

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
          class="btn btn-md btn-primary self-start mt-2"
          :disabled="!isPasswordFilled"
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
  </div>
</template>
