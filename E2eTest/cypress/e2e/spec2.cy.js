describe('Avaliar perfil', () => {
  it('Deve visitar site, realizar login, acessar a aba de performance e adicionar uma avaliação.', () => {
    cy.visit('https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index');
    cy.get('input[name="username"]').type('Admin');
    cy.wait(2000)
    cy.get('input[name="password"]').type('admin123');
    cy.get('button[type="submit"]').click();
    cy.wait(2000)
    cy.contains('Performance').click();
    cy.url().should('include', '/performance');
    cy.wait(2000)
    cy.contains('My Trackers').click();
    cy.wait(2000)
    cy.url().should('include', '/performance/viewMyPerformanceTrackerList');
    cy.wait(2000)
    cy.contains('View').click();
    cy.wait(2000)
    cy.get('.oxd-button').click();
    cy.wait(2000)
    cy.get('input[placeholder="Type here"]').first().type('Jorge');
    cy.get('textarea[placeholder="Type here"]').type('Muito ruim!');
    cy.contains('Negative').click();
    cy.contains('Save').click();
    cy.contains('Jorge').should('exist');
  });
});
