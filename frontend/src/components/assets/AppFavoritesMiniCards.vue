<script setup>
import HeartIcon from "../../assets/icons/ph_heart-fill.svg";
import { ref, onMounted, computed } from "vue";
import { listFavorites, removeFavorite } from "../../api/breeds";
import { useAuthStore } from "../../stores/auth";
import { useRouter } from "vue-router";
import AppModal from "./AppModal.vue";

const authStore = useAuthStore();
const router = useRouter();

const favorites = ref([]);
const error = ref("");
const showAuthModal = ref(false);

const SLOTS = 3;

const displaySlots = computed(() => {
  const slots = [];
  for (let i = 0; i < SLOTS; i++) {
    slots.push(favorites.value[i] || null);
  }
  return slots;
});

onMounted(async () => {
  if (!authStore.isAuthenticated) return;

  try {
    const response = await listFavorites();
    favorites.value = response.results.slice(0, SLOTS).map((f) => ({
      id: f.breed.id,
      title: f.breed.name,
      img: f.breed.image || f.breed.image_url,
    }));
  } catch {
    error.value = "Не вдалось завантажити улюблені породи";
  }
});

async function removeLike(breedId, index) {
  if (!breedId) return;
  try {
    await removeFavorite(breedId);
    favorites.value.splice(index, 1);
  } catch {
    error.value = "Не вдалось видалити породу";
    setTimeout(() => {
      error.value = "";
    }, 3000);
  }
}

function handleHeartClick(favorite) {
  if (!authStore.isAuthenticated) {
    showAuthModal.value = true;
    return;
  }
  if (favorite) {
    const index = favorites.value.findIndex((f) => f.id === favorite.id);
    removeLike(favorite.id, index);
  }
}
</script>

<template>
  <div class="flex flex-col gap-2">
    <span v-if="error" class="font-primary text-secondary text-error">
      {{ error }}
    </span>

    <div class="grid grid-cols-3 gap-6 min-h-[168px]">
      <div
        v-for="(slot, index) in displaySlots"
        :key="index"
        class="flex flex-col gap-4"
      >
        <template v-if="slot">
          <img
            :src="slot.img"
            :alt="slot.title"
            class="rounded-xl w-full h-[131px] object-cover"
          />
          <div class="flex flex-row justify-between items-start">
            <h3
              class="text-gray-100 text-secondary font-primary flex-1 pr-2 line-clamp-2 break-words"
            >
              {{ slot.title }}
            </h3>
            <component
              :is="HeartIcon"
              class="size-4 cursor-pointer text-primary shrink-0 mt-1"
              @click="handleHeartClick(slot)"
            />
          </div>
        </template>

        <template v-else>
          <div class="rounded-xl w-full h-[168px] bg-gray-20" />
        </template>
      </div>
    </div>

    <AppModal
      v-if="showAuthModal"
      title="Увійдіть або створіть акаунт"
      description="Щоб користуватися функцією обраного та зберігати свої вподобання і ті ж кнопки"
      @close="showAuthModal = false"
    >
      <div class="flex gap-4">
        <button
          class="btn btn-primary btn-md flex-1"
          @click="router.push('/auth')"
        >
          Увійти
        </button>
        <button
          class="btn btn-secondary btn-md flex-1"
          @click="showAuthModal = false"
        >
          Скасувати
        </button>
      </div>
    </AppModal>
  </div>
</template>
