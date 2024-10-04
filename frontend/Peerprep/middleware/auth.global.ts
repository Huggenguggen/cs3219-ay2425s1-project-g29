export default defineNuxtRouteMiddleware(async (to, from) => {
    const user = await getCurrentUser();

    if (user) {
        const tokenResult = await user.getIdTokenResult(true);  // Force a Token Refresh
        const isAdmin = tokenResult.claims.admin === true;

        // Check if the route requires admin access
        if (to.meta.requiresAdmin && !isAdmin) {
            return navigateTo('/unauthorized');
        }

        // If logged in, but trying to access Login or Register page, redirect to Home
        if (to.path == "/users/login" || to.path == "/users/register") {
            return navigateTo("/");
        }
    } else {
        // If user is not logged in and the route rquires auth
        if (to.meta.requiresAuth !== false) {  // Assume requireAuth is true by default
            return navigateTo("/users/login");
        }
    }
});
