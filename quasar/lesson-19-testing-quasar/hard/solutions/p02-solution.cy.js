// Cypress E2E tests for login flow
// Run: cypress run --spec hard/p02-solution.cy.js

describe('Login Flow E2E', () => {
  beforeEach(() => {
    cy.visit('/login')
  })

  it('logs in with valid credentials and redirects to dashboard', () => {
    cy.get('[data-test="email"]').type('user@example.com')
    cy.get('[data-test="password"]').type('correctpassword')
    cy.get('[data-test="submit"]').click()

    // Verify redirect to dashboard
    cy.url().should('include', '/dashboard')
    cy.get('[data-test="dashboard-title"]').should('contain', 'Dashboard')
  })

  it('shows error for invalid credentials', () => {
    cy.get('[data-test="email"]').type('user@example.com')
    cy.get('[data-test="password"]').type('wrongpassword')
    cy.get('[data-test="submit"]').click()

    // Verify error message appears
    cy.get('[data-test="error"]').should('be.visible')
    cy.get('[data-test="error"]').should('contain', 'Invalid credentials')
    // Verify we stay on login page
    cy.url().should('include', '/login')
  })

  it('logout redirects to login page', () => {
    // Login first
    cy.get('[data-test="email"]').type('user@example.com')
    cy.get('[data-test="password"]').type('correctpassword')
    cy.get('[data-test="submit"]').click()
    cy.url().should('include', '/dashboard')

    // Logout
    cy.get('[data-test="logout"]').click()

    // Verify redirect to login
    cy.url().should('include', '/login')
  })

  it('submit button is disabled when fields are empty', () => {
    cy.get('[data-test="submit"]').should('be.disabled')
  })

  it('navigates to register page from login', () => {
    cy.get('[data-test="register-link"]').click()
    cy.url().should('include', '/register')
  })
})
