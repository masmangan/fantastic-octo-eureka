package dino;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.support.ui.WebDriverWait;

public class TestSelenium {
	@Test
	@DisplayName("Teste Login")
	void testLogin() {
		WebDriver driver = Seleniumscript.getDriver();
		WebDriverWait wait = Seleniumscript.getWait(driver);
		Assertions.assertEquals("Dashboard", Seleniumscript.testLogin(driver, wait));
		Seleniumscript.closeDriver(driver);
	}
	
	@Test
	@DisplayName("Teste Qualificação")
	void testQualification() {
		WebDriver driver = Seleniumscript.getDriver();
		WebDriverWait wait = Seleniumscript.getWait(driver);
		Seleniumscript.testLogin(driver, wait);
		
		Assertions.assertEquals( 1, Seleniumscript.testQualification(driver, wait));
		Seleniumscript.closeDriver(driver);
	}
}
