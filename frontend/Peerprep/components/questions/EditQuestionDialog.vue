<script setup lang="ts">
import type { Question } from '~/types/Question';

const props = defineProps<{
  question: Question;
  refreshData: () => void;
}>();

const editedQuestion = ref({
  title: props.question.title,
  description: props.question.description,
  category: props.question.category,
  difficulty: props.question.difficulty,
  uid: props.question.uid,
});

const updateQuestion = async () => {
  try {
    const { data, error } = await useFetch(`http://localhost:5000/questions/${props.question.uid}`, {
      method: 'PUT',
      body: JSON.stringify(editedQuestion.value),
      headers: { 'Content-Type': 'application/json' }
    });
    
    if (error.value) {
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