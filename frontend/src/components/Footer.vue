<script setup>
import LinkedInIcon from "../assets/icons/ph_linkedin-logo.svg";
import BehanceIcon from "../assets/icons/ph_behance-logo.svg";
import InstagramIcon from "../assets/icons/ph_instagram-logo.svg";

defineProps({
  team: {
    type: Array,
    default: () => [
      "Андріана Романишин",
      "Ірина Кисіль",
      "Наталія Ровдич",
      "Владислава Михайлик",
      "Кирило Бондаренко",
      "Ярослав Гогуля",
    ],
  },
  socials: {
    type: Array,
    default: () => [
      { icon: "linkedin", href: "#" },
      { icon: "behance", href: "#" },
      { icon: "instagram", href: "#" },
    ],
  },
});

const socialIcons = {
  linkedin: LinkedInIcon,
  behance: BehanceIcon,
  instagram: InstagramIcon,
};
</script>

<template>
  <footer
    class="w-full rounded-2xl bg-white shadow-[0px_-6px_10px_rgba(0,0,0,0.05)]"
  >
    <div
      class="max-w-[1296px] mx-auto flex items-start justify-between m-auto gap-6 py-6"
    >
      <div class="flex flex-col gap-2 max-w-50">
        <span class="font-primary text-main text-gray-100">© 2026 Petly</span>
        <span class="font-primary text-small text-gray-80"
          >Розумний підбір улюбленця</span
        >
      </div>

      <div class="flex flex-col gap-2">
        <span class="font-primary text-main text-gray-100">Команда</span>
        <span class="font-primary text-small text-gray-80">
          {{ team.join(" · ") }}
        </span>
      </div>

      <div class="flex flex-col gap-3.25 min-w-30 items-end">
        <span class="font-primary text-main text-gray-100">Соцмережі</span>
        <div class="flex items-center gap-4">
          <a
            v-for="social in socials"
            :key="social.href"
            :href="social.href"
            target="_blank"
            class="app-footer-social-link text-gray-100 gap-"
          >
            <component :is="socialIcons[social.icon]" class="w-4 h-4" />
          </a>
        </div>
      </div>
    </div>
  </footer>
</template>
