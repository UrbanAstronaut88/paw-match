<script setup>
import { ref, computed } from "vue";

const props = defineProps({
  tabs: {
    type: Array,
    default: () => ["Вхід", "Реєстрація"],
  },
  modelValue: {
    type: Number,
    default: 0,
  },
});

const emit = defineEmits(["update:modelValue"]);

const activeIndex = computed({
  get: () => props.modelValue,
  set: (val) => emit("update:modelValue", val),
});
</script>

<template>
  <div class="relative flex w-75 h-10.5 bg-gray-20 rounded-btn">
    <div
      class="absolute h-full w-[calc(50%)] bg-primary rounded-btn pointer-events-none transition-transform duration-250 ease-in-out"
      :style="{ transform: `translateX(${activeIndex * 100}%)` }"
    />
    <button
      v-for="(tab, index) in tabs"
      :key="index"
      class="tab-switcher-item"
      :class="{ 'tab-switcher-item--active': activeIndex === index }"
      @click="activeIndex = index"
    >
      {{ tab }}
    </button>
  </div>
</template>
