<script setup>
import { ref, watch } from "vue";
import CheckIcon from "../../assets/icons/ph_check-bold.svg";
import AppCheckBox from "./AppCheckBox.vue";
import AppRadioButton from "./AppRadioButton.vue";

const props = defineProps({
  initialFilters: {
    type: Object,
    default: () => ({
      size: [],
      activity: [],
      care: [],
      housing: null,
      kids: null,
    }),
  },
});

const emit = defineEmits(["close", "apply"]);

const filters = ref({
  size: [...props.initialFilters.size],
  activity: [...props.initialFilters.activity],
  care: [...props.initialFilters.care],
  housing: props.initialFilters.housing,
  kids: props.initialFilters.kids,
});

watch(
  () => props.initialFilters,
  (newVal) => {
    filters.value = {
      size: [...newVal.size],
      activity: [...newVal.activity],
      care: [...newVal.care],
      housing: newVal.housing,
      kids: newVal.kids,
    };
  },
  { deep: true },
);

const sizeOptions = [
  { label: "Великий", value: "large" },
  { label: "Середній", value: "medium" },
  { label: "Малий", value: "small" },
];

const activityOptions = [
  { label: "Висока активність", value: "high" },
  { label: "Середня активність", value: "medium" },
  { label: "Низька активність", value: "low" },
];

const careOptions = [
  { label: "Легкий", value: "easy" },
  { label: "Середній", value: "medium" },
  { label: "Складний", value: "hard" },
];

const housingOptions = [
  { label: "Дім", value: "house" },
  { label: "Квартира", value: "apartment" },
];

const kidsOptions = [
  { label: "Є", value: "yes" },
  { label: "Немає", value: "no" },
];

function resetFilters() {
  filters.value = {
    size: [],
    activity: [],
    care: [],
    housing: null,
    kids: null,
  };
}

function applyFilters() {
  emit("apply", filters.value);
  emit("close");
}
</script>

<template>
  <div class="col-start-5 col-span-4 row-start-2 flex flex-col gap-8 pb-20">
    <div class="flex flex-col gap-3">
      <h1 class="font-primary text-h1 text-gray-100">Фільтри</h1>
      <p class="font-primary text-secondary text-gray-100">
        Оберіть параметри для підбору породи
      </p>
    </div>

    <div class="flex flex-col gap-4">
      <h3 class="font-primary text-h2 text-gray-100">Розмір</h3>
      <div class="flex flex-col bg-gray-10 rounded-[20px] overflow-hidden">
        <label
          v-for="opt in sizeOptions"
          :key="opt.value"
          class="flex justify-between items-center px-5 py-4 cursor-pointer hover:bg-gray-20 transition-colors"
        >
          <span class="font-primary text-main text-gray-100">{{
            opt.label
          }}</span>
          <AppCheckBox
            :value="opt.value"
            v-model="filters.size"
            :icon="CheckIcon"
          />
        </label>
      </div>
    </div>

    <div class="flex flex-col gap-4">
      <h3 class="font-primary text-h2 text-gray-100">Рівень активності</h3>
      <div class="flex flex-col bg-gray-10 rounded-[20px] overflow-hidden">
        <label
          v-for="opt in activityOptions"
          :key="opt.value"
          class="flex justify-between items-center px-5 py-4 cursor-pointer hover:bg-gray-20 transition-colors"
        >
          <span class="font-primary text-main text-gray-100">{{
            opt.label
          }}</span>
          <AppCheckBox
            :value="opt.value"
            v-model="filters.activity"
            :icon="CheckIcon"
          />
        </label>
      </div>
    </div>

    <div class="flex flex-col gap-4">
      <h3 class="font-primary text-h2 text-gray-100">Складність догляду</h3>
      <div class="flex flex-col bg-gray-10 rounded-[20px] overflow-hidden">
        <label
          v-for="opt in careOptions"
          :key="opt.value"
          class="flex justify-between items-center px-5 py-4 cursor-pointer hover:bg-gray-20 transition-colors"
        >
          <span class="font-primary text-main text-gray-100">{{
            opt.label
          }}</span>
          <AppCheckBox
            :value="opt.value"
            v-model="filters.care"
            :icon="CheckIcon"
          />
        </label>
      </div>
    </div>

    <div class="flex flex-col gap-4">
      <h3 class="font-primary text-h2 text-gray-100">Тип житла</h3>
      <div class="flex flex-col bg-gray-10 rounded-[20px] overflow-hidden">
        <label
          v-for="opt in housingOptions"
          :key="opt.value"
          class="flex justify-between items-center px-5 py-4 cursor-pointer hover:bg-gray-20 transition-colors"
        >
          <span class="font-primary text-main text-gray-100">{{
            opt.label
          }}</span>
          <AppRadioButton
            name="housingGroup"
            :value="opt.value"
            v-model="filters.housing"
          />
        </label>
      </div>
    </div>

    <div class="flex flex-col gap-4">
      <h3 class="font-primary text-h2 text-gray-100">Чи є діти?</h3>
      <div class="flex flex-col bg-gray-10 rounded-[20px] overflow-hidden">
        <label
          v-for="opt in kidsOptions"
          :key="opt.value"
          class="flex justify-between items-center px-5 py-4 cursor-pointer hover:bg-gray-20 transition-colors"
        >
          <span class="font-primary text-main text-gray-100">{{
            opt.label
          }}</span>
          <AppRadioButton
            name="kidsGroup"
            :value="opt.value"
            v-model="filters.kids"
          />
        </label>
      </div>
    </div>

    <div class="flex justify-center gap-4">
      <button class="btn btn-md btn-secondary" @click="resetFilters">
        Скинути
      </button>
      <button class="btn btn-md btn-primary" @click="applyFilters">
        Показати
      </button>
    </div>
  </div>
</template>
