<script setup lang="ts">

import type { Question } from '~/types/Question';

const question = ref<Question>({
    title: "",
    description: "",
    category: "",
    difficulty: "easy",
});

const submitQuestion = () => {
    console.log("Submitted question:", question.value);
};
</script>

<template>
    <Dialog>
        <DialogTrigger as-child>
            <Button class="font-semibold text-md">
                Add Question
            </Button>
        </DialogTrigger>
        <DialogContent class="sm:max-w-[525px]">
            <DialogHeader>
                <DialogTitle>Add Question</DialogTitle>
                <DialogDescription>
                    Fill in the details of the new question
                </DialogDescription>
            </DialogHeader>
            <form @submit.prevent="submitQuestion" class="grid gap-5 py-4">
                <!-- Title -->
                <div class="grid grid-cols-4 items-center gap-4">
                    <Label for="title">Title</Label>
                    <Input id="title" v-model="question.title" placeholder="Enter question title" class="col-span-3"
                        required />
                </div>

                <div class="grid grid-cols-4 items-center gap-4">
                    <Label for="description">Description</Label>
                    <Textarea id="description" v-model="question.description" placeholder="Enter question description"
                        class="col-span-3 h-32" required />
                </div>

                <div class="grid grid-cols-4 items-center gap-4">
                    <Label for="category">Category</Label>
                    <Input id="category" v-model="question.category" placeholder="Enter question category"
                        class="col-span-3" required />
                </div>

                <div class="grid grid-cols-4 items-center gap-4">
                    <Label for="difficulty">Difficulty</Label>
                    <Select id="difficulty" v-model="question.difficulty">
                        <SelectTrigger class="col-span-3">
                            <SelectValue placeholder="Select a timezone" />
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

                <Button type="submit" class="mt-4">
                    Submit
                </Button>
            </form>
        </DialogContent>
    </Dialog>
</template>