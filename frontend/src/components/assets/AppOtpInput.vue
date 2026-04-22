<script setup>
import { ref } from "vue";

defineOptions({ inheritAttrs: false });

defineProps({
  length: {
    type: Number,
    default: 4,
  },
  variant: {
    type: String,
    default: "",
  },
  label: {
    type: String,
    default: "",
  },
});

const emit = defineEmits(["update:modelValue"]);

const inputs = ref([]);
const values = ref(Array(4).fill(""));

function onInput(index, event) {
  const val = event.target.value.replace(/\D/g, "").slice(-1);

  values.value[index] = val;
  emit("update:modelValue", values.value.join(""));

  if (val && index < inputs.value.length - 1) {
    inputs.value[index + 1].focus();
  }
}

function onKeydown(index, event) {
  if (event.key === "Backspace" && !values.value[index] && index > 0) {
    inputs.value[index - 1].focus();
  }
}

function onPaste(event) {
  const paste = event.clipboardData
    .getData("text")
    .replace(/\D/g, "")
    .slice(0, 4);

  paste.split("").forEach((char, i) => {
    values.value[i] = char;
  });

  emit("update:modelValue", values.value.join(""));

  inputs.value[Math.min(paste.length, inputs.value.length - 1)].focus();

  event.preventDefault();
}
</script>

<template>
  <div class="flex flex-col gap-2">
    <span class="input-label" v-if="label">{{ label }}</span>
    <div class="flex gap-3">
      <input
        v-for="(_, index) in length"
        :key="index"
        :ref="(element) => (inputs[index] = element)"
        type="text"
        inputmode="numeric"
        maxlength="1"
        :value="values[index]"
        class="otp-input"
        :class="variant"
        v-bind="$attrs"
        @input="onInput(index, $event)"
        @keydown="onKeydown(index, $event)"
        @paste="onPaste"
      />
    </div>
  </div>
</template>
