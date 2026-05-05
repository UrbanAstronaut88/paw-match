<script setup>
import { ref, computed, watch } from "vue";
import { useRouter } from "vue-router";
import ArrowLeftIcon from "../../assets/icons/icon_arrow-left.svg";
import AppQuizForm from "./AppQuizForm.vue";
import questions from "../../assets/data/quiz_questions.json";
import AppSplitContent from "./AppSplitContent.vue";
import AppQuizResult from "./AppQuizResult.vue";
import AppPageLayout from "./AppPageLayout.vue";
import { getBreed, matchBreeds } from "../../api/breeds";

const emit = defineEmits(["submit"]);
const router = useRouter();

const savedState = JSON.parse(localStorage.getItem("petQuizState")) || {};

const quizStatus = ref(savedState.quizStatus || "answering");
const currentStep = ref(savedState.currentStep || 0);
const answers = ref(savedState.answers || {});
const resultData = ref(savedState.resultData || null);
const quizError = ref("");

watch(
  [quizStatus, currentStep, answers],
  () => {
    localStorage.setItem(
      "petQuizState",
      JSON.stringify({
        quizStatus: quizStatus.value,
        currentStep: currentStep.value,
        answers: answers.value,
        resultData: resultData.value,
      }),
    );
  },
  { deep: true },
);

const currentQuestion = computed(() => questions[currentStep.value]);
const isLast = computed(() => currentStep.value === questions.length - 1);

function next() {
  if (answers.value[currentQuestion.value.id] === undefined) return;

  if (isLast.value) {
    submit();
  } else {
    currentStep.value++;
  }
}

function back() {
  if (quizStatus.value !== "answering") {
    handleRetry();
    return;
  }

  if (currentStep.value > 0) {
    currentStep.value--;
  } else {
    router.back();
  }
}

async function submit() {
  const payload = Object.fromEntries(
    questions
      .filter((q) => q.field !== null)
      .map((q) => [q.field, answers.value[q.id]]),
  );

  quizStatus.value = "loading";

  try {
    const matches = await matchBreeds(payload);
    const bestMatch = matches[0];

    const breed = await getBreed(bestMatch.id);

    resultData.value = {
      id: breed.id,
      name: breed.name,
      image: breed.image || breed.image_url,
      housing: breed.traits.housing_type.value,
      stats: [
        {
          value: breed.traits.size.value,
        },
        {
          value: breed.traits.energy.value,
        },
        {
          value: breed.traits.grooming.value,
        },
        {
          value: breed.traits.kids_friendly.value,
        },
      ],
    };

    quizStatus.value = "result";
  } catch (error) {
    quizStatus.value = "answering";
    quizError.value = "Щось пішло не так. Спробуйте ще раз.";
  }
}

function handleMoreInfo() {
  if (resultData.value && resultData.value.id) {
    router.push(`/breed/${resultData.value.id}`);
  }
}

function handleRetry() {
  answers.value = {};
  currentStep.value = 0;
  resultData.value = null;
  quizStatus.value = "answering";
}
</script>

<template>
  <AppPageLayout @back="back">
    <AppQuizForm
      v-if="quizStatus === 'answering'"
      class="col-start-5 col-span-4 row-start-2"
      :question="currentQuestion"
      :current-step="currentStep"
      :total-steps="questions.length"
      :is-last="isLast"
      v-model="answers[currentQuestion.id]"
      @next="next"
    />

    <div
      v-if="quizError && quizStatus === 'answering'"
      class="col-start-5 col-span-4 row-start-3 font-primary text-secondary text-error"
    >
      {{ quizError }}
    </div>

    <AppSplitContent
      v-else-if="quizStatus === 'loading'"
      title="Підбираємо улюбленця..."
      description="Це допоможе зрозуміти, яка тварина підійде твоєму ритму життя."
    >
      <img
        src="../../assets/quiz_dog.png"
        alt="Собака"
        class="w-full col-span-12 object-cover rounded-2xl mb-8 -mt-2"
      />
    </AppSplitContent>

    <AppSplitContent
      v-else-if="quizStatus === 'result' && resultData"
      title="Твій результат готовий!"
      description="Ми підібрали улюбленця, який найкраще відповідає твоїм відповідям"
    >
      <AppQuizResult
        :breed-name="resultData.name || resultData.title"
        :image-src="resultData.image"
        :stats="resultData.stats"
        :housing-type="resultData.housing"
        @more-info="handleMoreInfo"
        @retry="handleRetry"
      />
    </AppSplitContent>
  </AppPageLayout>
</template>
