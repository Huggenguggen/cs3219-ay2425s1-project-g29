<script setup>

const user = useCurrentUser()
const router = useRouter()

onMounted(() => {
  watch(user, (currentUser, prevUser) => {
    if (prevUser && !currentUser) {
      return router.replace('/users/login')
    }
  })
}

)

</script>

<template>

  <NuxtLayout>
    <NuxtPage />
  </NuxtLayout>

</template>