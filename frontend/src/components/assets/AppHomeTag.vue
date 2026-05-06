<script setup>
import { computed } from "vue";
import HouseIcon from "../../assets/icons/ph_house-simple-bold-16.svg";

const props = defineProps({
  type: { type: String, default: "house" },
});

const types = {
  house: { label: "Дім" },
  apartment: { label: "Квартира" },
  "apartment/house": { label: "Квартира/Дім" },
};

const normalizedType = computed(() => props.type?.toLowerCase());
</script>

<template>
  <div
    class="flex items-center justify-center w-fit min-w-27.75 gap-1 px-2.5 py-2 rounded-btn bg-gray-10 font-primary text-secondary text-gray-100 shadow-card"
  >
    {{ types[normalizedType]?.label }}
    <component :is="HouseIcon" class="size-4 block" />
  </div>
</template>
