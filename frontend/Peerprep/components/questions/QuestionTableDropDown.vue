<script setup lang="ts">
import type { Question } from '~/types/Question';
import { MoreHorizontal } from 'lucide-vue-next'

defineProps<{
    question: Question
}>()

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

                <DropdownMenuItem>Delete</DropdownMenuItem>
            </DropdownMenuContent>
        </DropdownMenu>
        <DialogContent>
            <div>
                {{ question.title }}
            </div>
        </DialogContent>
    </Dialog>
</template>