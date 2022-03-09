<template>
  <nav :class="this.navClasses" ref="nav">
    <CopyrightBlock />
  </nav>
</template>

<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
  data() {
    return {
      navClasses: ['bg-gray-700', 'p-4', 'mt-2', 'w-full'],
    }
  },
})
</script>
