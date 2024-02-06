import { jwtDecode } from "jwt-decode";
import dayjs from "dayjs";


export async function load({ locals }) {
    const token = locals.token;

    let isExpired = true
    if (token == undefined) return { isExpired }
    //const isExpired = token == undefined ? { isExpired: true } : { isExpired: dayjs.unix(jwtDecode(token).exp).diff(dayjs()) < 1 };


    const decode = jwtDecode(token)
    isExpired = dayjs.unix(decode.exp).diff(dayjs()) < 1
    return { isExpired }
}


//export const load = async ({ locals }) => { isExpired: locals.token == undefined ? true : dayjs.unix(jwtDecode(locals.token).exp).diff(dayjs()) < 1 };

