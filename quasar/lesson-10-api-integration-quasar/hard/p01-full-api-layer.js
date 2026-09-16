/**
 * LESSON 10 — API Integration in Quasar
 * HARD P01 — Complete API Layer
 * ============================================
 * CONCEPT: Production API layers bundle four things: a configured axios
 * instance, request/response interceptors (auth header + logging), a
 * centralized error handler, and per-resource service objects. On 401 you
 * attempt a token refresh once (_retry flag) then re-issue the request.
 *
 * PROBLEM: Export `userService` and `postService` (getAll/getById/create/
 * update/remove against the api instance), a default `api` axios instance
 * (baseURL + timeout), request interceptor adding Bearer token + logging,
 * response interceptor logging + calling handleError + refresh-on-401
 * logic, and a `handleError` that classifies response/request/setup errors.
 *
 * TRY THIS: if (error.response?.status === 401 && !originalRequest._retry) {
 *   originalRequest._retry = true; ... refresh ...; return api(originalRequest) }
 *
 * EXPECTED OUTPUT: Services return parsed data; 401 triggers a refresh then
 * a retry; all errors funnel through handleError.
 *
 * CHECK: python3 check.py hard/p01
 */
// TODO: write your API layer here
