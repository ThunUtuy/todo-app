describe('template spec', function () {
    //sign up with a test user first
  beforeEach(function () {
    cy.fixture('users').then((users) => {
    this.currentUser = users.testUser
  })

  })

  it('Load the login page', function (){
    const { username, password } = this.currentUser
    cy.login(username, password)

    cy.request({
      method: 'POST',
      url: '/delete',
      form: true, // This tells Cypress to encode the body as x-www-form-urlencoded
      body: {
        task_id: '-1',
      }
    })

    cy.visit('/create')
    cy.get('input[name=title]').type('test task')
    cy.get('input[name=due_date]').type('2025-12-31')
    cy.get('textarea[name=notes]').type(`test notes`)
    cy.get('form').submit()
    // we should be redirected to /index
    cy.url().should('include', '/index')
    cy.contains('test task')
  })
})