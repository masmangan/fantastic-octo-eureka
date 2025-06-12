import { test, expect } from "@playwright/test";

test.describe("Security Tests - Login Page", () => {
  const baseUrl =
    "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login";

  const maliciousInputs = [
    "' OR '1'='1", //SQL
    "'; DROP TABLE users; --",
    "' OR 1=1 --",
    "' OR 'a'='a",
    "' UNION SELECT NULL, NULL, NULL --",
    "' AND 1=(SELECT COUNT(*) FROM users) --",
    "admin' --",
    "admin' #",
    "' OR EXISTS(SELECT * FROM users) --",
    "') OR ('1'='1' --",
    "'; EXEC xp_cmdshell('dir'); --",
    "' OR SLEEP(5) --",
    "<script>alert('XSS')</script>",
    "\"><script>alert('XSS')</script>",
    "<img src=x onerror=alert('XSS')>",
    "\"><svg/onload=alert('XSS')>",
    "<body onload=alert('XSS')>",
    "<iframe src=\"javascript:alert('XSS')\"></iframe>",
  ];

  for (const input of maliciousInputs) {
    test(`Should reject malicious input: ${input}`, async ({ page }) => {
      await page.goto(baseUrl);

      await page.getByRole("textbox", { name: "Username" }).fill(input);
      await page.getByRole("textbox", { name: "Password" }).fill("anything");
      await page.getByRole("button", { name: "Login" }).click();

      const errorMsg = await page
        .locator(".oxd-alert-content-text")
        .textContent();

      expect(errorMsg?.toLowerCase()).toContain("invalid");
    });
  }
});
