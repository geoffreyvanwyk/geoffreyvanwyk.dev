<template>
  <div class="w-full h-screen flex flex-col">
    <PrimaryMenuRegion />
    <div class="px-4 flex-grow">
      <Nuxt />
    </div>
    <FooterRegion />
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
export default Vue.extend({})
</script>
