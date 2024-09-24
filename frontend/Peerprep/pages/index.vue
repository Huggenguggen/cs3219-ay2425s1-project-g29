<script setup lang="ts">

import ComboBox from '@/components/ComboBox.vue'
const auth = useFirebaseAuth();
const user = useCurrentUser();
const runtimeConfig = useRuntimeConfig()


const leetcodeTopics = [
  { value: 'arrays', label: 'Arrays' },
  { value: 'strings', label: 'Strings' },
  { value: 'linked-lists', label: 'Linked Lists' },
  { value: 'binary-trees', label: 'Binary Trees' },
  { value: 'hash-tables', label: 'Hash Tables' },
  { value: 'dynamic-programming', label: 'Dynamic Programming' },
  { value: 'recursion', label: 'Recursion' },
  { value: 'binary-search', label: 'Binary Search' },
  { value: 'sorting', label: 'Sorting' },
  { value: 'two-pointers', label: 'Two Pointers' },
  { value: 'greedy', label: 'Greedy Algorithms' },
  { value: 'graphs', label: 'Graphs' },
  { value: 'backtracking', label: 'Backtracking' },
  { value: 'bit-manipulation', label: 'Bit Manipulation' },
  { value: 'math', label: 'Math' },
  { value: 'sliding-window', label: 'Sliding Window' },
  { value: 'stacks', label: 'Stacks' },
  { value: 'queues', label: 'Queues' },
  { value: 'heap-priority-queue', label: 'Heap / Priority Queue' },
  { value: 'trie', label: 'Trie' },
  { value: 'divide-and-conquer', label: 'Divide and Conquer' },
  { value: 'design', label: 'Design' },
  { value: 'union-find', label: 'Union Find' },
  { value: 'monotonic-stack', label: 'Monotonic Stack' },
  { value: 'tree-traversal', label: 'Tree Traversal' },
]

const difficulty = ref('easy')
const selectedTopic = ref(leetcodeTopics.length > 0 ? leetcodeTopics[0].value : '')
const isMatching = ref(false)
const noMatch = ref(false)
const matchTimeout = 30

async function handleSubmit() {
  console.log("selected difficulty", difficulty.value)
  console.log("selected topic", selectedTopic.value)
  $fetch(`${runtimeConfig.public.backendApiUrl}/matching/`, {
    method: 'POST',
    body: {
      difficulty: difficulty.value,
      topic: selectedTopic.value
    }
  })
}

</script>

<template>
  <div class="min-h-full w-full flex flex-col justify-center items-center">
    <Card class="w-[420px]">
      <CardHeader>
        <div class="flex justify-center font-bold text-xl">
          Matching
        </div>
      </CardHeader>
      <CardContent class="space-y-5">
        <form @submit.prevent="handleSubmit" class="space-y-6 px-4">
          <div class="flex items-center justify-between">
            <Label class="text-lg">Difficulty</Label>
            <Select v-model="difficulty">
              <SelectTrigger class="w-[200px] font-medium px-4">
                <SelectValue placeholder="Select a difficulty level" />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="easy">
                  Easy
                </SelectItem>
                <SelectItem value="medium">
                  Medium
                </SelectItem>
                <SelectItem value="hard">
                  Hard
                </SelectItem>
              </SelectContent>
            </Select>
          </div>

          <div class="flex items-center justify-between">
            <Label class="text-lg">Topic</Label>
            <ComboBox :data="leetcodeTopics" v-model="selectedTopic" />
          </div>

          <div class="flex justify-center w-full">
            <Button class="w-3/4 mt-3">
              Match
            </Button>
          </div>
        </form>
      </CardContent>
    </Card>
  </div>
</template>
