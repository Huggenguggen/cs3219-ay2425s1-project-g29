<script setup lang="ts">
import { columns } from '@/components/questions/columns'
import QuestionTable from '@/components/questions/QuestionTable.vue';
import type { Question } from '~/types/Question';

const { data, status, error, refresh } = await useFetch('http://localhost:5000/questions')
const questions = ref<Question[]>([]);

watchEffect(() => {
  if (data.value) {
    questions.value = data.value.map((question, index) => ({
      id: index + 1,
      title: question.title,
      description: question.description,
      category: question.category,
      difficulty: question.difficulty,
      uid: question.id
    }))
  }
})

</script>

<template>
  <div class="container py-10 mx-auto">
    <QuestionTable :columns="columns" :data="questions" :refresh-data="refresh" />
  </div>
</template>