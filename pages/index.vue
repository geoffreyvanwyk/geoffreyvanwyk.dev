<template>
  <PageWrapper>
    <AppBar />
    <FooterBar />
  </PageWrapper>
</template>

<script lang="ts">
import Vue from 'vue'

import AppBar from '~/components/AppBar.vue'
import FooterBar from '~/components/FooterBar.vue'
import PageWrapper from '~/components/PageWrapper.vue'

export default Vue.extend({
  components: { AppBar, FooterBar, PageWrapper },
  name: 'IndexPage',
})
</script>
