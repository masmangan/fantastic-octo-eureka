const { defineConfig } = require("cypress");

module.exports = defineConfig({
  e2e: {
    // Adicione esta linha para resolver o aviso:
    supportFile: false,
    video: true,

    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
  },
});