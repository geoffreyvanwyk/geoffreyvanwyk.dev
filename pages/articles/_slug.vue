<template>
  <article
    class="mx-auto prose prose-lg bg-white shadow-lg prose-gray-400 prose-h1:mb-2 prose-code:text-xs"
  >
    <ArticleImage :article="article" />

    <div class="px-4 pb-2">
      <TagList :tags="article.tags" />

      <h1 class="text-gray-800">{{ article.title }}</h1>

      <span class="text-sm uppercase">
        {{ formatDate(article.createdAt) }}
      </span>
      <span class="text-sm italic lowercase">by</span>
      <span class="text-sm uppercase">{{ article.author }}</span>

      <p class="lead">{{ article.description }}</p>

      <nuxt-content :document="article" />
    </div>
  </article>
</template>

<script lang="ts">
import Vue from 'vue'

export default Vue.extend({
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
