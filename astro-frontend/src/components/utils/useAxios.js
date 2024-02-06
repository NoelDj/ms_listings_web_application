import axios from "axios";
import jwt_decode from "jwt-decode";
import dayjs from "dayjs";
import { writable } from "svelte/store";

const baseURL = "http://localhost:8000/api";    

function useAxios() {
  const authTokens = writable(JSON.parse(localStorage.getItem("authTokens")) || {});

  const axiosInstance = axios.create({
    baseURL,
    headers: {
      Authorization: `Bearer ${authTokens.access || ""}`,
    },
  });

  const unsubscribe = authTokens.subscribe((value) => {
    axiosInstance.defaults.headers.common[
      "Authorization"
    ] = `Bearer ${value.access || ""}`;
  });

  axiosInstance.interceptors.request.use(async (req) => {
    const user = jwt_decode(authTokens.access || "");
    const isExpired = dayjs.unix(user.exp).diff(dayjs()) < 1;

    if (!isExpired) return req;

    try {
      const response = await axios.post(`${baseURL}/token/refresh`, {
        refresh: authTokens.refresh || "",
      });

      localStorage.setItem("authTokens", JSON.stringify(response.data));

      authTokens.set(response.data);

      req.headers.Authorization = `Bearer ${response.data.access}`;
      return req;
    } catch (error) {
      // Handle token refresh error
      console.error("Token refresh error:", error);
      throw error;
    }
  });

  return { axiosInstance, unsubscribe };
}

export default useAxios;