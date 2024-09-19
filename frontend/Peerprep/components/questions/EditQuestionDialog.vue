<script setup lang="ts">

import type { Question } from '~/types/Question';
import { useToast } from '@/components/ui/toast/use-toast';

const props = defineProps<{
  question: Question;
  refreshData: () => void;
}>();

const { toast } = useToast();

const editedQuestion = ref({
  title: props.question.title,
  description: props.question.description,
  category: props.question.category,
  difficulty: props.question.difficulty,
});

const updateQuestion = async () => {
  try {
    const category_arr = editedQuestion.value.category.split(',').map(cat => cat.trim());

    const { data, error } = await useFetch(`http://localhost:5000/questions/${props.question.id}`, {
        method: 'PUT',
        body: JSON.stringify({
            title: editedQuestion.value.title,
            description: editedQuestion.value.description,
            category: category_arr, // Send category as an array
            difficulty: editedQuestion.value.difficulty
        }),
        headers: { 'Content-Type': 'application/json' }
    });
    
    if (error.value) {
      const errorMessage = await error.value?.data;
      toast({
          title: "Error updating question:",
          description: errorMessage.error,  // Use the error message from the backend
      });
      console.error("Error updating question:", error.value);
    } else {
      console.log("Updated question successfully:", data.value);
      props.refreshData();
    }
  } catch (err) {
    console.error("An error occurred while updating the question:", err);
  }
};
</script>

<template>
  <DialogContent class="sm:max-w-[525px]">
    <DialogHeader>
      <DialogTitle>Edit Question</DialogTitle>
      <DialogDescription>
        Update the details of the question
      </DialogDescription>
    </DialogHeader>
    <form @submit.prevent="updateQuestion" class="grid gap-5 py-4">
      <!-- Title -->
      <div class="grid grid-cols-4 items-center gap-4">
        <Label for="title">Title</Label>
        <Input id="title" v-model="editedQuestion.title" placeholder="Enter question title" class="col-span-3" required />
      </div>

      <div class="grid grid-cols-4 items-center gap-4">
        <Label for="description">Description</Label>
        <Textarea id="description" v-model="editedQuestion.description" placeholder="Enter question description"
          class="col-span-3 h-32" required />
      </div>

      <div class="grid grid-cols-4 items-center gap-4">
        <Label for="category">Category</Label>
        <Input id="category" v-model="editedQuestion.category" placeholder="Enter question category" class="col-span-3" required />
      </div>

      <div class="grid grid-cols-4 items-center gap-4">
        <Label for="difficulty">Difficulty</Label>
        <Select id="difficulty" v-model="editedQuestion.difficulty">
          <SelectTrigger class="col-span-3">
            <SelectValue placeholder="Select a difficulty" />
          </SelectTrigger>
          <SelectContent>
            <SelectGroup>
              <SelectItem value="easy">Easy</SelectItem>
              <SelectItem value="medium">Medium</SelectItem>
              <SelectItem value="hard">Hard</SelectItem>
            </SelectGroup>
          </SelectContent>
        </Select>
      </div>
      <DialogClose>
        <Button type="submit" class="mt-4">
          Update
        </Button>
      </DialogClose>
    </form>
  </DialogContent>
</template>