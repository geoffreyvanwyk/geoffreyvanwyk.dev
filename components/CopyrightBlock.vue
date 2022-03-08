<template>
  <div>
    <span class="font-semibold text-gray-400">Copyright</span>
    <span class="text-lg font-semibold text-gray-400">&copy;</span>
    <span class="font-semibold text-white">{{ this.currentYear }}</span>
    <span class="font-semibold text-white">Geoffrey van Wyk</span>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
  data() {
    return {
      currentYear: new Date().toLocaleDateString('en-za', {
        year: 'numeric',
      } as Intl.DateTimeFormatOptions),
      navClasses: ['bg-gray-700', 'p-4', 'mt-2', 'w-full'],
    }
  },
})
</script>
