<script setup>
import { signOut } from 'firebase/auth';

const auth = useFirebaseAuth();
const user = useCurrentUser();

function handleSignOut() {
  signOut(auth)
}
</script>

<template>
  <div class="min-h-full w-full flex flex-col justify-center items-center">
    <img src="@/assets/PeerPrep.png" alt="Logo" class="w-24" />
    <div class="flex flex-col gap-y-4">

      <h1 class="text-center">Welcome to PeerPrep, {{ user?.displayName }}</h1>
      <Button>Match</Button>
    </div>
  </div>
</template>
