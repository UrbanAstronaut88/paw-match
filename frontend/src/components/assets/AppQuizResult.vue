<script setup>
import AppHomeTag from "./AppHomeTag.vue";
import AppBreedStats from "./AppBreedStats.vue";
import AppPageLayout from "./AppPageLayout.vue";
import AppSplitContent from "./AppSplitContent.vue";
import { ref } from "vue";

defineProps({
  breedName: {
    type: String,
    required: true,
  },
  imageSrc: {
    type: String,
    required: true,
  },
  stats: {
    type: Array,
    required: true,
  },
  housingType: {
    type: String,
    required: true,
  },
});

defineEmits(["more-info", "retry"]);
</script>

<template>
  <div
    class="w-full col-span-12 grid grid-cols-12 gap-8 -mt-2 mb-8"
    :class="$attrs"
  >
    <div class="col-span-6 h-full">
      <img
        :src="imageSrc"
        :alt="breedName"
        class="w-full h-full max-h-141.5 object-cover rounded-3xl"
      />
    </div>

    <div class="col-span-6 flex flex-col items-start gap-8 py-2">
      <div class="flex flex-col gap-6">
        <h1 class="font-primary text-h1 text-gray-100">
          {{ breedName }}
        </h1>
        <p class="font-primary text-main text-gray-100">
          Характеристики породи
        </p>
      </div>

      <AppBreedStats :stats="stats" />

      <AppHomeTag :type="housingType" />

      <div class="flex items-center gap-4 mt-auto">
        <button class="btn btn-md btn-secondary" @click="$emit('more-info')">
          Більше про породу
        </button>
        <button class="btn btn-md btn-primary px-6" @click="$emit('retry')">
          Пройти ще раз
        </button>
      </div>
    </div>
  </div>
</template>
