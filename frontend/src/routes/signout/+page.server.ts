import { redirect } from '@sveltejs/kit';

export const actions = {
  default: async ({ cookies }) => {

    try {
        await cookies.delete("authToken", { path: '/', secure: false });
    } catch (err) {
        console.log("Error", err)
    }

    redirect(301, "/login")
  }
};