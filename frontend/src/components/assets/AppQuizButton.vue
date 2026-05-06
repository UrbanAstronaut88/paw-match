<!-- AppRadioCard.vue -->
<script setup>
import AppRadioButton from "./AppRadioButton.vue";

defineOptions({ inheritAttrs: false });

defineProps({
  label: { type: String, required: true },
  value: { type: [String, Number], required: true },
  modelValue: { type: [String, Number], default: null },
});

const emit = defineEmits(["update:modelValue"]);
</script>

<template>
  <label
    class="flex items-center justify-between px-4 py-2.5 h-[52px] w-[410px] rounded-btn bg-gray-10 cursor-pointer border border-transparent transition-all"
    :class="modelValue === value ? 'border-primary' : 'hover:border-gray-20'"
  >
    <span class="font-primary text-main text-gray-100">{{ label }}</span>

    <AppRadioButton
      :value="value"
      :name="$attrs.name"
      :checked="modelValue === value"
      @change="emit('update:modelValue', value)"
    />
  </label>
</template>
