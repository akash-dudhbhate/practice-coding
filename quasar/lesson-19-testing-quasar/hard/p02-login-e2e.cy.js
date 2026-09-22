/**
 * LESSON 19 — Testing Quasar Apps
 * HARD P02 — Cypress Login Flow E2E
 * ============================================
 * CONCEPT: Cypress drives a real browser: cy.visit() loads a page,
 * cy.get('[data-test=...]').type()/click() interact, cy.url().should()
 * asserts navigation, .should('be.disabled'/'be.visible') checks state.
 *
 * PROBLEM: E2E the login flow: visit /login, valid credentials redirect
 * to /dashboard (dashboard-title visible), invalid credentials show an
 * error and stay on /login, logout returns to /login. Bonus: disabled
 * submit when empty; register-link navigation.
 *
 * TRY THIS: cy.visit('/login')
 * cy.get('[data-test="email"]').type('user@example.com')
 * cy.get('[data-test="submit"]').click()
 * cy.url().should('include', '/dashboard')
 *
 * EXPECTED OUTPUT: A describe('Login Flow') with its for the happy path,
 * the error path, and logout.
 *
 * CHECK: python3 check.py hard/p02
 */
// TODO: write your Cypress tests here
