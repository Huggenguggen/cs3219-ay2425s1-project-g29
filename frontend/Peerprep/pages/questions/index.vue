<script setup lang="ts">
import { columns } from '@/components/questions/columns'
import QuestionTable from '@/components/questions/QuestionTable.vue';
import type { Question } from '~/types/Question';
const data = ref<Question[]>([
    { id: 1, title: 'What is Vue?', description: 'A frontend framework.', category: 'JavaScript', complexity: 'easy' },
    { id: 2, title: 'Explain closures.', description: 'A function with lexical scope.', category: 'JavaScript', complexity: 'medium' },
]);

</script>

<template>
    <div class="container py-10 mx-auto">
        <QuestionTable :columns="columns" :data="data" />
    </div>
</template>