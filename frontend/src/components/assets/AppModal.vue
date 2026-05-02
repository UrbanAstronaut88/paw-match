<script setup>
defineProps({
  title: { type: String, default: "" },
  description: { type: String, default: "" },
});

const emit = defineEmits(["close"]);
</script>

<template>
  <Teleport to="body">
    <div
      class="fixed inset-0 z-50 flex items-center justify-center bg-gray-100/40 backdrop-blur-sm"
      @click.self="emit('close')"
    >
      <div
        class="bg-white rounded-3xl p-8 flex flex-col gap-6 max-w-[480px] w-full mx-6 shadow-card"
      >
        <div class="flex flex-col gap-2">
          <h2 class="font-primary text-h2 text-gray-100">{{ title }}</h2>
          <p class="font-primary text-secondary text-gray-80">
            {{ description }}
          </p>
        </div>

        <slot />
      </div>
    </div>
  </Teleport>
</template>
