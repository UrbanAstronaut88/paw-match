<script setup>
import ArrowLeftIcon from "../../assets/icons/icon_arrow-left.svg";

defineEmits(["back"]);
</script>

<template>
  <div
    class="grid grid-cols-12 gap-x-8 gap-y-10 items-start content-start pt-10"
  >
    <div class="col-span-2 row-start-1 flex items-center gap-4 self-start">
      <button class="btn btn-icon btn-icon-secondary" @click="$emit('back')">
        <ArrowLeftIcon class="size-6" />
      </button>
      <span class="font-primary text-main text-gray-80"> Назад </span>
    </div>

    <slot />
  </div>
</template>
