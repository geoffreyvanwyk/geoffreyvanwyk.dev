<template>
  <PageWrapper>
    <AppBar />

    <article
      class="prose prose-lg prose-h1:mb-2 prose-img:rounded prose-code:text-xs mx-auto"
    >
      <img :src="article.img" :alt="article.alt" />

      <p class="text-sm uppercase">
        {{ formatDate(article.updatedAt) }}
        <span class="italic lowercase">by</span>
        {{ article.author }}
      </p>

      <h1>{{ article.title }}</h1>
      <tag-list :tags="article.tags" />
      <p class="lead">{{ article.description }}</p>

      <nuxt-content :document="article" />
    </article>

    <FooterBar />
  </PageWrapper>
</template>

<script lang="ts">
import Vue from 'vue'

import AppBar from '~/components/AppBar.vue'
import FooterBar from '~/components/FooterBar.vue'
import TagList from '~/components/TagList.vue'

export default Vue.extend({
  components: { AppBar, FooterBar, TagList },
  async asyncData({ $content, params }) {
    const article = await $content('articles', params.slug).fetch()

    return { article }
  },
  methods: {
    formatDate(date: string) {
      return new Date(date).toLocaleDateString('en-za', {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
      } as Intl.DateTimeFormatOptions)
    },
  },
})
</script>
