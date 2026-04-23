<script setup>
import AppIconButton from "./assets/AppIconButton.vue";
import ArrowRightIcon from "../assets/icons/icon_arrow-right.svg";

defineProps({
  title: {
    type: String,
    required: true,
  },
  description: {
    type: String,
    required: true,
  },
  contentGap: { type: String, default: "gap-8" },
  titleStyle: { type: String, default: "text-h1 font-primary text-gray-100" },
  descriptionStyle: {
    type: String,
    default: "text-main font-primary text-gray-100",
  },
});
</script>

<template>
  <div class="article-section" :class="gap">
    <div class="article-section-header">
      <div class="article-section-header-text">
        <h2 class="article-section-title" :class="titleStyle">{{ title }}</h2>
        <p class="article-section-description" :class="descriptionStyle">
          {{ description }}
        </p>
      </div>
      <AppIconButton class="btn-primary shrink-0" :icon="ArrowRightIcon" />
    </div>

    <slot></slot>
  </div>
</template>
