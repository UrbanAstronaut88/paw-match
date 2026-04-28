<script setup>
import EyeIcon from "../../assets/icons/ph_eye-bold.svg";
import EyeOffIcon from "../../assets/icons/ph_eye-closed-bold.svg";
import { ref, computed, onMounted, watch } from "vue";

defineOptions({ inheritAttrs: false });

const props = defineProps({
  label: { type: String, default: "" },
  placeholder: { type: String, default: "" },
  icon: { type: Object, default: null },
  type: { type: String, default: "text" },
  error: { type: String, default: "" },
  modelValue: { type: String, default: "" },
  autofocus: { type: Boolean, default: false },
});

const inputRef = ref(null);
defineExpose({ inputRef });

onMounted(() => {
  if (props.autofocus) inputRef.value?.focus();
});

const emit = defineEmits(["update:modelValue", "blur"]);

const showPassword = ref(false);

const inputType = computed(() => {
  if (props.type === "password")
    return showPassword.value ? "text" : "password";
  return props.type;
});
</script>

<template>
  <div class="flex flex-col gap-4">
    <span v-if="label" class="input-label">{{ label }}</span>

    <div class="input-wrapper" v-bind="$attrs">
      <input
        class="input"
        ref="inputRef"
        :autofocus="autofocus"
        :type="inputType"
        :placeholder="placeholder"
        :value="props.modelValue"
        @input="emit('update:modelValue', $event.target.value)"
        @blur="emit('blur', $event)"
        v-bind="$attrs"
      />

      <button
        v-if="type === 'password'"
        type="button"
        @click="showPassword = !showPassword"
      >
        <EyeOffIcon v-if="showPassword" class="cursor-pointer" />
        <EyeIcon v-else class="cursor-pointer" />
      </button>

      <component v-else-if="icon" :is="icon" class="text-gray-100 shrink-0" />
    </div>

    <span v-if="error" class="font-primary text-secondary text-error">{{
      error
    }}</span>
  </div>
</template>
