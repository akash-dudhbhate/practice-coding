/**
 * LESSON 10 — API Integration in Quasar
 * EASY P02 — Axios Instance with Interceptors
 * ============================================
 * CONCEPT: axios.create() makes a pre-configured client (baseURL, timeout,
 * headers). interceptors.request.use() runs before every call — perfect for
 * injecting an auth token from localStorage.
 *
 * PROBLEM: Export an axios instance with baseURL, timeout, a request
 * interceptor adding `Authorization: Bearer <token>` from localStorage
 * ('auth_token'), and a response interceptor that warns on 401.
 *
 * TRY THIS: const api = axios.create({ baseURL: 'https://jsonplaceholder.typicode.com', timeout: 10000 });
 * api.interceptors.request.use(config => { config.headers.Authorization = `Bearer ${token}`; return config })
 *
 * EXPECTED OUTPUT: `import api from './p02-...'` gives a client that sends
 * the token automatically and flags 401 responses.
 *
 * CHECK: python3 check.py easy/p02
 */
// TODO: write your axios instance here
