export default defineNuxtRouteMiddleware(async (to, from) => {
  const user = await getCurrentUser();

  if (user && (to.path == "/users/login" || to.path == "/users/register")) {
    return navigateTo("/");
  }

  if (!user && to.path != "/users/login" && to.path !== "/users/register") {
    return navigateTo("/users/login");
  }
});
