<script setup>
import { computed } from "vue";
import AppQuizStepDivider from "./AppQuizStepDivider.vue";
import AppQuizButton from "./AppQuizButton.vue";

const props = defineProps({
  question: { type: Object, required: true },
  currentStep: { type: Number, required: true },
  totalSteps: { type: Number, required: true },
  isLast: { type: Boolean, required: true },
  modelValue: { type: [String, Number, Boolean], default: undefined }, // Поточна відповідь
});

const emit = defineEmits(["update:modelValue", "next"]);

const isAnswered = computed(() => props.modelValue !== undefined);

const currentAnswer = computed({
  get: () => props.modelValue,
  set: (newValue) => emit("update:modelValue", newValue),
});
</script>

<template>
  <div class="flex flex-col gap-10 mb-10">
    <div class="flex flex-col gap-4 w-75">
      <h1 class="font-primary text-h1 text-gray-100">Квіз: вибір породи</h1>
      <p class="font-primary text-secondary text-gray-100">
        Це допоможе зрозуміти, яка тварина підійде твоєму ритму життя.
      </p>
    </div>

    <div class="mx-auto w-full">
      <AppQuizStepDivider :current="currentStep + 1" :total="totalSteps" />
    </div>

    <div class="mx-auto w-full flex flex-col gap-8">
      <h2 class="font-primary text-h2 text-gray-100">
        {{ question.question }}
      </h2>

      <div :key="question.id" class="flex flex-col gap-4">
        <AppQuizButton
          v-for="option in question.options"
          :key="option.value"
          :label="option.label"
          :value="option.value"
          v-model="currentAnswer"
          :name="question.id"
        />
      </div>
    </div>

    <button
      class="btn btn-primary btn-big w-full"
      :disabled="!isAnswered"
      @click="emit('next')"
    >
      {{ isLast ? "Завершити" : "Продовжити" }}
    </button>
  </div>
</template>
