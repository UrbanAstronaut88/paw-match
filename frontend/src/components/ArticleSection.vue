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
  containerPadding: { type: String, default: "p-8" },
  headerGap: { type: String, default: 'gap-4' },
  alignment: { type: String, default: ' ' },
  titleStyle: { type: String, default: "text-h1 font-primary text-gray-100" },
  descriptionStyle: {
    type: String,
    default: "text-main font-primary text-gray-80",
  },
});

defineEmits(["click"]);
</script>

<template>
  <div
    class="flex flex-col justify-between rounded-2xl bg-gray-10 w-158"
    :class="[contentGap, containerPadding]"
  >
    <div class="flex justify-between" :class="alignment">
      <div class="flex flex-col" :class="headerGap">
        <h1 :class="[titleStyle]">{{ title }}</h1>
        <p :class="descriptionStyle">
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
