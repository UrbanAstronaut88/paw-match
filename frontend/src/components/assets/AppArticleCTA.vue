<script setup>
defineProps({
  title: {
    type: String,
    default: "Готові обрати собаку, яка підійде саме вам?",
  },
  description: {
    type: String,
    default:
      "Пройдіть короткий квіз і отримайте рекомендації порід, які підійдуть під ваш стиль життя.",
  },
  buttonText: {
    type: String,
    default: "Почати квіз",
  },
});

defineEmits(["start"]);
</script>

<template>
  <div class="flex flex-col items-start gap-8" :class="$attrs">
    <div class="flex flex-col gap-4">
      <h2 class="font-primary text-h2 text-gray-100">
        {{ title }}
      </h2>
      <p class="font-primary text-main text-gray-80">
        {{ description }}
      </p>
    </div>

    <button class="btn btn-sm btn-primary px-8 py-3" @click="$emit('start')">
      {{ buttonText }}
    </button>
  </div>
</template>
