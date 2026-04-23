<script setup>
import HouseIcon from "../../assets/icons/ph_house-simple-bold-16.svg";

defineProps({
  type: { type: String, default: "house" },
});

const types = {
  house: { label: "Дім" },
  apartment: { label: "Квартира" },
};
</script>

<template>
  <div
    class="flex items-center justify-center w-27.75 gap-1 px-2.5 py-2 rounded-btn bg-gray-10 font-primary text-secondary text-gray-100 shadow-card"
  >
    {{ types[type].label }}
    <component :is="HouseIcon" class="size-4 block" />
  </div>
</template>
