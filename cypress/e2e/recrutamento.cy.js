describe('Jornada de Cadastro de Candidato no OrangeHRM', () => {

  beforeEach(() => {
    cy.visit('https://opensource-demo.orangehrmlive.com/');
    cy.get('input[name="username"]').type('Admin');
    cy.get('input[name="password"]').type('admin123');
    cy.get('button[type="submit"]').click();
    cy.wait(2000); 
    cy.contains('Recruitment').click();
    cy.wait(1500); 
  });

  // REC-001: Caminho Feliz
  it('Deve cadastrar um novo candidato com sucesso', () => {
    cy.contains('button', 'Add').click();
    cy.wait(1500); 

    const timestamp = Date.now();
    cy.get('input[name="firstName"]').type(`Candidato_${timestamp}`);
    cy.wait(500);
    cy.get('input[name="lastName"]').type('Teste');
    cy.wait(500);
    cy.get('.oxd-select-text--after').click();
    cy.contains('.oxd-select-option', 'Software Engineer').click();
    cy.get('.oxd-input-group:contains("Email")').find('input').type(`candidato_${timestamp}@teste.com`);
    cy.wait(2500);
    
    cy.get('button[type="submit"]').click();

    cy.contains('Successfully Saved', { timeout: 10000 }).should('be.visible');

    cy.wait(2000); 
  });

  // REC-002: testando "Required"
  it('Deve exibir uma mensagem de erro ao tentar salvar sem e-mail', () => {
    cy.contains('button', 'Add').click();
    cy.wait(1000); 
    cy.get('input[name="firstName"]').type('Candidato');
    cy.wait(500);
    cy.get('input[name="lastName"]').type('SemEmail');
    cy.wait(2000);
    cy.get('button[type="submit"]').click();
    cy.wait(2500); 
    cy.contains('Required').should('be.visible');
  });
});