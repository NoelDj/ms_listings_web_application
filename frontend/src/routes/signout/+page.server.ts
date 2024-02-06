import { redirect } from '@sveltejs/kit';

export const actions = {
  default: async ({ cookies }) => {

    try {
        await cookies.delete("authToken", { path: '/' });
    } catch (err) {
        console.log("Error", err)
    }

    redirect(301, "/login")
  }
};