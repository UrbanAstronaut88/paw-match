<script setup>
defineProps({
  icon: {
    type: Object,
    required: true,
  },
});
</script>

<template>
  <button class="btn btn-icon" v-bind="$attrs">
    <component :is="icon" class="size-6 block" />
  </button>
</template>
