<script setup lang="ts">
import type { Question } from '~/types/Question';
import { MoreHorizontal } from 'lucide-vue-next'

const props = defineProps<{
    question: Question
}>()

const emit = defineEmits(['refresh']);

const deleteQuestion = async () => {
  try {
    const { error } = await useFetch(`http://localhost:5000/questions/${props.question.uid}`, {
      method: 'DELETE',
    });
    
    if (error.value) {
      console.error('Error deleting question:', error.value);
    } else {
      console.log('Deleted question successfully');
      emit('refresh');
    }
  } catch (err) {
    console.error('An error occurred while deleting the question:', err);
  }
};

</script>

<template>

    <Dialog>
        <DropdownMenu>
            <DropdownMenuTrigger as-child>
                <Button variant="ghost" class="w-8 h-8 p-0">
                    <span class="sr-only">Open menu</span>
                    <MoreHorizontal class="w-4 h-4" />
                </Button>
            </DropdownMenuTrigger>
            <DropdownMenuContent align="end">
                <DropdownMenuLabel>Actions</DropdownMenuLabel>
                <DialogTrigger as-child>
                    <DropdownMenuItem>Edit</DropdownMenuItem>
                </DialogTrigger>

                <DropdownMenuItem @click="deleteQuestion">Delete</DropdownMenuItem>
            </DropdownMenuContent>
        </DropdownMenu>
        <DialogContent>
            <div>
                {{ question.title }}
            </div>
        </DialogContent>
    </Dialog>
</template>