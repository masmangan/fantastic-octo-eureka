describe('Visualizar perfil', () => {
  it('Deve visitar site, realizar login e acessar a aba de perfil', () => {
    cy.visit('https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index');
    cy.get('input[name="username"]').type('Admin');
    cy.wait(2000)
    cy.get('input[name="password"]').type('admin123');
    cy.get('button[type="submit"]').click();
    cy.wait(2000)
    cy.contains('My Info').click();
    cy.wait(2000)
    cy.url().should('include', '/pim/viewPersonalDetails');
    cy.get('h6').should('contain', 'Personal Details');
    cy.wait(2000)
  });
});
