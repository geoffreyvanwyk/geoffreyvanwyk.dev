<template>
  <ul class="flex items-center">
    <li
      v-for="menuItem in menuItems"
      :key="menuItem.label"
      class="text-gray-200 font-semibold capitalize"
    >
      <NuxtLink :to="menuItem.link">{{ menuItem.label }}</NuxtLink>
    </li>
  </ul>
</template>

<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
  data() {
    return {
      menuItems: [
        {
          label: 'Home',
          link: '/',
        },
      ],
    }
  },
})
</script>
