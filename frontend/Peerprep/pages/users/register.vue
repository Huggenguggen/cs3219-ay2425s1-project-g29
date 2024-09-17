<script setup>
import { createUserWithEmailAndPassword } from 'firebase/auth';

const auth = useFirebaseAuth()
const router = useRouter()

const email = ref('')
const displayName = ref('')
const password = ref('');
const repeatPassword = ref('');
const firebaseErrorMessage = ref('');

// Computed properties
const emailNotValid = computed(() => {
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return (!emailPattern.test(email.value) && email.value != "");
});

const passwordRequirementNotMet = computed(() => {
    const passwordValue = password.value || '';  // Ensure that passwordValue is a string
    const passwordLengthNotSatisfied = password.value.length < 6;
    return passwordLengthNotSatisfied && (passwordValue != "");
});

const passwordMismatch = computed(() => {
    return password.value !== repeatPassword.value && repeatPassword.value != "";
});

const allFieldsNotValid = computed(() => {
    var valuesNotValid = (emailNotValid.value || passwordRequirementNotMet.value || passwordMismatch.value);
    var valuesEmpty = email.value == "" || displayName.value == "" || password.value == "" || repeatPassword.value == "";

    return valuesNotValid || valuesEmpty;
});

// Submit button function
const handleSubmit = () => {
    if (!passwordMismatch.value) {
        register()
            .then(() => router.replace('/'))
            .catch((error) => {
                var errorCode = error.code;
                if (errorCode == 'auth/email-already-in-use') {
                    firebaseErrorMessage.value = "Account with that email already exists.";
                } else if (errorCode == 'auth/invalid-email') {
                    firebaseErrorMessage.value = "Email address is not valid.";
                } else if (errorCode == 'auth/weak-password') {
                    firebaseErrorMessage.value = "The password is not strong enough.";
                } else {
                    firebaseErrorMessage.value = "Unknown Firebase Error: " + error.message
                }
            });
    }
};

// Register user with Firebase
const register = async () => {
    await createUserWithEmailAndPassword(auth, email.value, password.value);
}
</script>

<template>
    <div class="min-h-full w-full flex items-center justify-center">
        <Card class="w-[380px]">
            <CardHeader>
                <CardTitle class="text-xl">
                    Sign Up
                </CardTitle>
                <CardDescription>
                    Enter your information to create an account
                </CardDescription>

            </CardHeader>
            <CardContent class="space-y-5">
                <form @submit.prevent="handleSubmit" class="space-y-5">
                    <div class="grid gap-2">
                        <Label for="email">Email</Label>
                        <Input id="email" name="email" v-model="email" type="email" placeholder="m@example.com" required
                            autocomplete="email" />
                        <p v-if="emailNotValid" class="text-red-500 text-sm">Incorrect email format</p>
                    </div>


                    <div class="grid gap-2">
                        <Label for="displayName">Display Name</Label>
                        <Input id="displayName" name="displayName" v-model="displayName" type="text" placeholder=""
                            required />
                    </div>

                    <div class="grid gap-2">
                        <Label for="password">Password</Label>
                        <Input id="password" name="password" v-model="password" type="password" required
                            autocomplete="new-password" />
                        <p v-if="passwordRequirementNotMet" class="text-red-500 text-sm">Password should be at least 6
                            characters</p>
                    </div>

                    <!-- Repeat Password Field -->
                    <div class="grid gap-2">
                        <Label for="repeat-password">Repeat Password</Label>
                        <Input id="repeat-password" name="repeat-password" v-model="repeatPassword" type="password"
                            required autocomplete="new-password" />
                        <p v-if="passwordMismatch" class="text-red-500 text-sm">Passwords do not match</p>
                    </div>

                    <!-- Error Message -->
                    <p v-if="firebaseErrorMessage" class="text-red-500">{{ firebaseErrorMessage }}</p>

                    <Button type="submit" class="w-full" :disabled="allFieldsNotValid">
                        Create an account
                    </Button>
                </form>

                <div class="mt-4 text-center text-sm">
                    Already have an account?
                    <NuxtLink to="/users/login" class="underline">
                        Sign in
                    </NuxtLink>
                </div>
            </CardContent>
        </Card>
    </div>
</template>