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

defineEmits(["click"]);
</script>

<template>
  <div class="article-section" :class="contentGap">
    <div class="article-section-header">
      <div class="article-section-header-text">
        <h1 class="article-section-title" :class="titleStyle">{{ title }}</h1>
        <p class="article-section-description" :class="descriptionStyle">
          {{ description }}
        </p>
      </div>
      <AppIconButton
        class="btn-primary shrink-0"
        :icon="ArrowRightIcon"
        @click="$emit('click')"
      />
    </div>

    <slot></slot>
  </div>
</template>
