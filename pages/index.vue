<template>
  <app-bar></app-bar>
</template>

<script lang="ts">
import Vue from 'vue'
import AppBar from '~/components/AppBar.vue'

export default Vue.extend({
  components: { AppBar },
  name: 'IndexPage',
})
</script>
