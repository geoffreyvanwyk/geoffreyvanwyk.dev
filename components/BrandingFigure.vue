<template>
  <figure class="flex">
    <NuxtLink to="/">
      <img
        src="~/assets/geoffreyvanwyk.jpg"
        alt="Profile photo of Geoffrey van Wyk"
        class="w-16 h-16 rounded-full ring-4 ring-white"
      />
    </NuxtLink>
    <figcaption
      class="pl-4 flex flex-col items-start justify-center font-semibold text-white"
    >
      <NuxtLink to="/"> Geoffrey van Wyk </NuxtLink>
      <div class="text-gray-400">Computer Programmer</div>
    </figcaption>
  </figure>
</template>

<script lang="ts">
import Vue from 'vue'

export default Vue.extend({})
</script>
