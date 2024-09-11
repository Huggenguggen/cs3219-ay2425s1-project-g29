<script setup>
import { signOut } from 'firebase/auth';

const auth = useFirebaseAuth();
const user = useCurrentUser();

function handleSignOut() {
  signOut(auth)
}
</script>

<template>
  <div class="container vh-100 d-flex flex-column justify-content-between align-items-center">
    <!-- Logo Section -->
    <div class="mt-3">
      <img src="@/assets/PeerPrep.png" alt="Logo" class="logo-img" />
    </div>

    <!-- Welcome Bar -->
    <div class="mt-5">
      <h1 class="text-center">Welcome to PeerPrep, {{ user.display_name }}</h1>
    </div>

    <!-- Logout Button -->
    <div class="mt-3">
      <button @click="handleSignOut" class="btn btn-secondary btn-lg">Logout</button>
    </div>

    <!-- Match Button positioned higher -->
    <div class="d-flex justify-content-center align-items-center flex-grow-1 w-100">
      <button class="btn btn-primary btn-lg w-50">Match</button>
    </div>
  </div>
</template>


<style scoped>
/* Style for the logo */
.logo-img {
  width: 100px; /* Adjust size as needed */
  height: auto;
}

/* Adjust the container's flex settings */
.flex-grow-1 {
  flex-grow: 1; /* Makes the button section grow to take available space */
}

.w-50 {
  width: 50% !important; /* Ensures the button takes up 50% width of the container */
}
</style>