<script setup>
import { signInWithPopup, GoogleAuthProvider } from 'firebase/auth'

const auth = useFirebaseAuth()
const router = useRouter()

function signInWithFirebase() {
  signInWithPopup(auth, new GoogleAuthProvider())
    .then(() => router.replace('/'))
}
</script>

<template>
  <div class="container vh-100 d-flex flex-column justify-content-center align-items-center">
    <!-- Logo Section -->
    <div class="mb-4">
      <img src="@/assets/PeerPrep.png" alt="Logo" class="logo-img" />
    </div>

    <!-- Text Section -->
    <div class="mb-4">
      <h2 class="text-center">Log in to continue</h2>
    </div>

    <!-- Login Button -->
    <div>
      <button @click="signInWithFirebase" class="btn btn-primary btn-lg">Sign in with Google</button>
    </div>
  </div>
</template>

<style scoped>
/* Style for the logo */
.logo-img {
  width: 100px; /* Adjust size as needed */
  height: auto;
}
</style>
