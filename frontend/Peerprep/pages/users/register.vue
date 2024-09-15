<script setup>
const email = ref("")
const displayName = ref("")
const password = ref('');
const repeatPassword = ref('');
const passwordMismatch = computed(() => password.value !== repeatPassword.value);
const handleSubmit = () => {
    if (!passwordMismatch.value) {
        console.log('Email:', email.value);
        console.log('Password:', password.value);
    }

};
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
                    </div>

                    <!-- Repeat Password Field -->
                    <div class="grid gap-2">
                        <Label for="repeat-password">Repeat Password</Label>
                        <Input id="repeat-password" name="repeat-password" v-model="repeatPassword" type="password"
                            required autocomplete="new-password" />
                    </div>

                    <!-- Error Message -->
                    <p v-if="passwordMismatch" class="text-red-500">Passwords do not match</p>

                    <Button type="submit" class="w-full">
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