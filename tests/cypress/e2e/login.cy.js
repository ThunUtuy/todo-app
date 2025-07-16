describe('Loggin In', () => {
  //sign up with a test user first
  beforeEach(()=> {
    cy.request({
      method: 'POST',
      url: '/signup',
      form: true, // This tells Cypress to encode the body as x-www-form-urlencoded
      body: {
        username: 'testuser',
        password: 'test1234',
      }
    })

  })

  it('Load the login page', function (){
    const username = 'testuser'
    const password = 'test1234'

    cy.visit('/')
    cy.url().should('include', '/login')
    cy.get('input[name=username]').type(username)
    cy.get('input[name=password]').type(`${password}{enter}`)
    // we should be redirected to /index
    cy.url().should('include', '/index')
  })
})