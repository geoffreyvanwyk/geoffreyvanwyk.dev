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
  mounted() {
    const nav = this.$refs.nav as HTMLElement
    const heightOfAppBar = 96
    const shouldBeFixed = window.innerHeight - nav.offsetTop > heightOfAppBar
    if (shouldBeFixed) {
      this.navClasses = this.navClasses.concat(['fixed', 'bottom-0'])
    }
  },
})
</script>
