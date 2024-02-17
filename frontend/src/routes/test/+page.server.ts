import { fail } from '@sveltejs/kit';

interface DataObject {
    [key: string]: { value: string; missing?: boolean; incorrect?: boolean };
}

export const actions = {
    login: async ({ request }: { request }) => {

        const data = await request.formData()
        const email = data.get('email')
        const password = data.get('password')

        const dataObject: DataObject = {
            email: { value: email || '' },
            password: { value: password || '' }
        }

        if (!email) {
            dataObject.email.missing = true
        }

        if (!password) {
            dataObject.password.incorrect = true;
        }

        if (Object.values(dataObject).some(field => field.missing || field.incorrect)) {
            return fail(400, dataObject)
        }

        return { success: true }
    }
};
