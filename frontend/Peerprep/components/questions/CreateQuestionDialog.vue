<script setup lang="ts">

import type { Question } from '~/types/Question';
import { useToast } from '@/components/ui/toast/use-toast';

const props = defineProps<{ refreshData: () => void }>();

const { toast } = useToast();

const question = ref<Question>({
    title: "",
    description: "",
    category: "",
    difficulty: "easy",
});

const submitQuestion = async () => {
    try {
        const category_arr = question.value.category.split(',').map(cat => cat.trim());
        
        const { data, error } = await useFetch('http://localhost:5000/questions', {
            method: 'POST',
            body: JSON.stringify({
                title: question.value.title,
                description: question.value.description,
                category: category_arr, // Send category as an array
                difficulty: question.value.difficulty
            }),
            headers: { 'Content-Type': 'application/json' }
        });
        
        if (error.value) {
            const errorMessage = await error.value?.data;  
            toast({
                title: "Error submitting question:",
                description: errorMessage.error,  // Use the error message from the backend
            });
            console.error("Error submitting question:", errorMessage.error);
        } else {
            console.log("Submitted question successfully:", data.value);
            props.refreshData();
        }
    } catch (err) {
        console.error("An error occurred while submitting the question:", err);
    }
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
                    <Input id="category" v-model="question.category" placeholder="Enter categories separated by commas"
                        class="col-span-3" required />
                </div>

                <div class="grid grid-cols-4 items-center gap-4">
                    <Label for="difficulty">Difficulty</Label>
                    <Select id="difficulty" v-model="question.difficulty">
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
                        Submit
                    </Button>
                </DialogClose>
            </form>
        </DialogContent>
    </Dialog>
</template>