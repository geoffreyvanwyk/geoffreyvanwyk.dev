<template>
  <nav :class="this.navClasses" ref="nav">
    <span class="text-gray-400 font-semibold">Copyright</span>
    <span class="text-gray-400 text-lg font-semibold">&copy;</span>
    <span class="text-white font-semibold">{{ this.currentYear }}</span>
    <span class="text-white font-semibold">Geoffrey van Wyk</span>
  </nav>
</template>

<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
  data() {
    return {
      currentYear: new Date().toLocaleDateString('en-za', {
        year: 'numeric',
      } as Intl.DateTimeFormatOptions),
      navClasses: ['bg-gray-700', 'p-4', 'w-full'],
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
