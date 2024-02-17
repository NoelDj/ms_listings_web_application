import { fail } from '@sveltejs/kit';

interface DataObject {
    [key: string]: { value: string; missing?: boolean; incorrect?: boolean };
}

export const actions = {
    login: async ({ request }: { request }) => {
        console.log('login');

        const data = await request.formData();
        const email = data.get('email');
        const password = data.get('password');

        const dataObject: DataObject = {
            email: { value: email || '' }, // Set value property regardless
            password: { value: password || '' }
        };

        if (!email) {
            console.log('no email');
            dataObject.email.missing = true; // Set missing property if email is missing
        }

        if (!password) {
            console.log('no password');
            dataObject.password.incorrect = true;
        }

        if (Object.values(dataObject).some(field => field.missing || field.incorrect)) {
            return fail(400, dataObject);
        }

        return { success: true };
    }
};
