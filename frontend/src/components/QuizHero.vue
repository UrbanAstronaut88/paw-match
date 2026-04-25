<script setup>
import TargetIcon from "../assets/icons/ph_target-bold.svg";
import ClockIcon from "../assets/icons/ph_timer-bold.svg";
import PawIcon from "../assets/icons/ph_paw-print-bold.svg";

defineProps({
  title: {
    type: String,
    default: "Хто твій ідеальний улюбленець?",
  },
  description: {
    type: String,
    default: "Пройди короткий тест і дізнайся, яка порода підходить саме тобі",
  },
  image: {
    type: String,
    default: null,
  },
  features: {
    type: Array,
    default: () => [
      { icon: TargetIcon, label: "Розумний підбір" },
      { icon: ClockIcon, label: "Швидкий результат" },
      { icon: PawIcon, label: "15+ порід" },
    ],
  },
});
</script>

<template>
  <div class="quiz-hero">
    <div class="quiz-hero-header">
      <h1 class="quiz-hero-title">{{ title }}</h1>
      <p class="quiz-hero-description">{{ description }}</p>
    </div>

    <div class="quiz-hero-image-wrapper">
      <img v-if="image" :src="image" :alt="Pet" class="quiz-hero-image" />
      <div v-else class="quiz-hero-image-placeholder" />
    </div>

    <div class="quiz-hero-features">
      <div
        v-for="(feature, index) in features"
        :key="index"
        class="quiz-hero-feature"
      >
        <component :is="feature.icon" class="size-4 block" />

        <span class="quiz-hero-feature-label">{{ feature.label }}</span>
      </div>
    </div>

    <button class="btn btn-md btn-primary self-start">Почати квіз</button>
  </div>
</template>
