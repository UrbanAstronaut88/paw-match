<script setup>
defineProps({
  title: {
    type: String,
    required: true,
  },
  description: {
    type: String,
    required: true,
  },
  textColClass: {
    type: String,
    default: "col-span-4",
  },
});
</script>

<template>
  <div class="row-start-2 flex flex-col gap-4" :class="textColClass">
    <h1 class="font-primary text-h1 text-gray-100">{{ title }}</h1>
    <p class="font-primary text-secondary text-gray-100">
      {{ description }}
    </p>
  </div>

  <slot></slot>
</template>
