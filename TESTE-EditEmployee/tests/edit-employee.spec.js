const { test, expect } = require("@playwright/test");

test("Editar dados de um funcionário existente", async ({ page }) => {
	await page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login");

	await page.getByPlaceholder("Username").fill("Admin");
	await page.getByPlaceholder("Password").fill("admin123");
	await page.getByRole("button", { name: "Login" }).click();
	console.log("Login realizado com sucesso");

	await page.getByRole("link", { name: "PIM" }).click();
	console.log("Navegando para PIM");
	await page.getByRole("link", { name: "Employee List" }).click();
	console.log("Navegando para Employee List");

	const searchInputs = await page.locator('input[placeholder="Type for hints..."]');
	if (searchInputs) {
		console.log("Campo de busca encontrado");
	}
	await expect(searchInputs.first()).toBeVisible();
	await searchInputs.first().fill("Ranga");
	console.log("Campo de busca preenchido com 'Ranga'");

	await page.getByRole("button", { name: "Search" }).click();

	const row = page.locator('div.oxd-table-row:has-text("Ranga")');
	if ((await row.count()) > 0) {
		console.log("Linha com o nome 'Ranga' encontrada");
	}
	await expect(row).toBeVisible();

	await row.click();

	await expect(page.getByRole("heading", { name: "Personal Details" })).toBeVisible();

	const firstNameField = page.getByPlaceholder("First Name");
	if (await firstNameField.isVisible()) {
		console.log("Campo 'First Name' encontrado");
	}
	await expect(firstNameField).toBeVisible();
	await firstNameField.fill("RangaBraba");

	await page.getByRole("button", { name: "Save" }).click();

	const toast = page.locator(".oxd-toast-content");
	await toast.waitFor({ state: "visible", timeout: 5000 }).catch(() => {});

	const updatedFirstNameField = page.getByPlaceholder("First Name");
	await expect(updatedFirstNameField).toHaveValue("RangaEditado");
});
