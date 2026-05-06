<script setup>
import { ref, computed } from "vue";
import AppInput from "../AppInput.vue";

defineProps({
  isLoading: { type: Boolean, default: false },
});

const emit = defineEmits(["next"]);

const name = ref("");
const surname = ref("");
const birthday = ref("");
const city = ref("");

const nameTouched = ref(false);
const surnameTouched = ref(false);
const birthdayTouched = ref(false);

const isBirthdayValid = computed(() => {
  const regex = /^\d{2}\.\d{2}\.\d{4}$/;
  if (!regex.test(birthday.value)) return false;
  const [day, month, year] = birthday.value.split(".").map(Number);
  const date = new Date(year, month - 1, day);
  return (
    date.getFullYear() === year &&
    date.getMonth() === month - 1 &&
    date.getDate() === day &&
    date < new Date()
  );
});

const handleBirthdayInput = (value) => {
  birthdayTouched.value = false;

  let cleaned = value.replace(/\D/g, "");

  let day = cleaned.slice(0, 2);
  let month = cleaned.slice(2, 4);
  let year = cleaned.slice(4, 8);

  if (day.length === 2) {
    const d = parseInt(day);
    if (d > 31) day = "31";
    if (d === 0 && day.length === 2) day = "01";
  }

  if (month.length === 2) {
    const m = parseInt(month);
    if (m > 12) month = "12";
    if (m === 0 && month.length === 2) month = "01";
  }

  let formatted = day;
  if (cleaned.length > 2) formatted += "." + month;
  if (cleaned.length > 4) formatted += "." + year;

  birthday.value = formatted;

  if (birthdayRef.value?.inputRef) {
    birthdayRef.value.inputRef.value = formatted;
  }
};

const isFormValid = computed(
  () => name.value && surname.value && isBirthdayValid.value,
);

const nameRef = ref(null);
const surnameRef = ref(null);
const birthdayRef = ref(null);
const cityRef = ref(null);

function handleSubmit() {
  if (!isFormValid.value) return;

  emit("next", {
    name: name.value,
    surname: surname.value,
    birthday: birthday.value,
    city: city.value,
  });
}

function handleEnter() {
  if (!name.value) {
    nameRef.value?.inputRef?.focus();
    return;
  }
  if (!surname.value) {
    surnameRef.value?.inputRef?.focus();
    return;
  }
  if (!isBirthdayValid.value) {
    birthdayRef.value?.inputRef?.focus();
    return;
  }
  handleSubmit();
}
</script>

<template>
  <div
    class="flex flex-col items-start gap-6"
    @keydown.enter.prevent="handleEnter"
  >
    <AppInput
      ref="nameRef"
      label="Трішки про тебе"
      placeholder="Ім'я"
      v-model="name"
      :error="nameTouched && !name ? 'Будь ласка, введіть ваше ім\'я' : ''"
      @blur="nameTouched = true"
      @update:model-value="nameTouched = false"
      autofocus
    />

    <AppInput
      ref="surnameRef"
      placeholder="Прізвище"
      v-model="surname"
      :error="
        surnameTouched && !surname ? 'Будь ласка, введіть ваше прізвище' : ''
      "
      @blur="surnameTouched = true"
      @update:model-value="surnameTouched = false"
    />

    <AppInput
      ref="birthdayRef"
      placeholder="ДД.ММ.РРРР"
      maxlength="10"
      inputmode="numeric"
      :model-value="birthday"
      :error="
        birthdayTouched && !isBirthdayValid
          ? 'Введіть коректну дату народження'
          : ''
      "
      @blur="birthdayTouched = true"
      @update:model-value="handleBirthdayInput"
    />

    <AppInput
      ref="cityRef"
      placeholder="Місто (необов'язково)"
      v-model="city"
    />

    <button
      class="btn btn-primary btn-md"
      :disabled="!isFormValid || isLoading"
      @click="handleSubmit"
    >
      {{ isLoading ? "Завантаження..." : "Продовжити" }}
    </button>
  </div>
</template>
