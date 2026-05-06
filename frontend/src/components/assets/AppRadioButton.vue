<script setup>
const props = defineProps({
  value: { type: [String, Number], required: true },
  name: { type: String, required: true },
  modelValue: { type: [String, Number], default: null },
});

const emit = defineEmits(["update:modelValue"]);
</script>

<template>
  <div class="flex items-center cursor-pointer">
    <input
      type="radio"
      :name="name"
      :value="value"
      :checked="modelValue === value"
      class="form-input-hidden"
      @change="emit('update:modelValue', value)"
    />
    <div class="radio"></div>
  </div>
</template>
