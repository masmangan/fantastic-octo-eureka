describe('Jornada: Solicitar Licença no OrangeHRM', () => {
  it('faz login, acessa a aba Leave e solicita uma licença', () => {

    cy.visit('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')


    cy.get('input[name="username"]', { timeout: 10000 }).should('be.visible').type('Admin')
    cy.get('input[name="password"]').should('be.visible').type('admin123')
    cy.get('button[type="submit"]').click()


    cy.url().should('include', '/dashboard')
    cy.get('.oxd-userdropdown-tab').should('be.visible')


    cy.get('a[href="/web/index.php/leave/viewLeaveModule"]')
      .should('be.visible')
      .click()


    cy.contains('Apply', { timeout: 10000 })
      .should('be.visible')
      .click()


    cy.get('body').then($body => {
      if ($body.find('.oxd-select-text').length > 0) {
        cy.get('.oxd-select-text').first().click()
        cy.contains('.oxd-select-option', 'CAN - Personal').click()

        
        cy.get('input[placeholder="yyyy-mm-dd"]').eq(0).type('2025-06-10')
        cy.get('input[placeholder="yyyy-mm-dd"]').eq(1).type('2025-06-10')

        
        cy.get('textarea[placeholder="Add Comment"]').type('Solicitação de licença para assuntos pessoais')

       
        cy.get('button[type="submit"]').click()

        
        cy.contains('Successfully Submitted', { timeout: 10000 }).should('exist')
        
        
        cy.url().should('include', '/leave/viewLeaveModule')
      } else {
        cy.log('Nenhum tipo de licença disponível para solicitar.')
      }
    })
  })
})
