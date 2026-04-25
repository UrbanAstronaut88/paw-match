<script setup>
defineProps({
  current: { type: Number, required: true },
  total: { type: Number, required: true },
});
</script>

<template>
  <div class="flex items-center gap-4 w-102.5">
    <div class="flex-1 h-px bg-gray-30" />
    <span class="font-primary text-secondary text-gray-100 shrink-0">
      Питання {{ current }} з {{ total }}
    </span>
    <div class="flex-1 h-px bg-gray-30" />
  </div>
</template>
