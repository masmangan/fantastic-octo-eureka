package dino;

import java.time.Duration;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import io.github.bonigarcia.wdm.WebDriverManager;

public class Seleniumscript {

	public static String testLogin(WebDriver driver, WebDriverWait wait) {
		String resultado = "";
		try {
			driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login");

			WebElement usernameField = wait.until(
					ExpectedConditions.visibilityOfElementLocated(By.cssSelector("input[placeholder='Username']")));
			usernameField.clear();
			usernameField.sendKeys("Admin");

			WebElement passwordField = wait.until(
					ExpectedConditions.visibilityOfElementLocated(By.cssSelector("input[placeholder='Password']")));
			passwordField.clear();
			passwordField.sendKeys("admin123");

			clickCss(driver, wait, "button.oxd-button.oxd-button--medium.oxd-button--main.orangehrm-login-button", "Entrar Site");
			
			wait.until(ExpectedConditions.presenceOfElementLocated(By.cssSelector("div.oxd-topbar-header-title")));
			System.out.println("Login realizado com sucesso!");
			
			WebElement dashboardTitle = wait.until(
					ExpectedConditions.visibilityOfElementLocated(By.xpath("//*[@id=\"app\"]/div[1]/div[1]/header/div[1]/div[1]/span/h6")));
			resultado = dashboardTitle.getText();
		} catch (Exception e) {
			System.out.println("Erro durante o login: " + e.getMessage());
			driver.quit();
			
		}
		return resultado;
	}

	public static int testQualification(WebDriver driver, WebDriverWait wait) {
		int resultado = 0;
		try {
			String path = "//*[@id=\"app\"]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a";
			clickXpath(driver, wait, path, "My Info");

			path = "//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[9]/a";
			clickXpath(driver, wait, path, "Qualification");
			String pathQuantidade = "//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[2]/div/span";
			WebElement itemQualification = wait.until(
					ExpectedConditions.visibilityOfElementLocated(By.xpath(pathQuantidade)));
			resultado = extrairNumero(itemQualification.getText());

			path = "//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/div/button";
			clickXpath(driver, wait, path, "ADD Work Experience");

			path = "//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input";
			fillInput(wait, path, "PUCRS","Compania");

			path = "//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input";
			fillInput(wait, path, "Gerente Admin","Cargo");

			path = "//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/div/div/i";
			clickXpath(driver, wait, path, "Caledario To");
			
			String cssSelector = ".oxd-calendar-header > button.oxd-icon-button > .bi-chevron-left.oxd-icon";
			clickCss(driver, wait,cssSelector, "Botão Mes Anterior");
			
			cssSelector = "div.oxd-calendar-date-wrapper:nth-of-type(19)";
			clickCss(driver, wait,cssSelector, "Botão Dia 19");
			
			
			path = "//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/div/div/i";
			clickXpath(driver, wait, path, "Calendario From");
			
			sleep(1000);
			
			cssSelector = ".--today.oxd-date-input-link";
			clickCss(driver, wait, cssSelector, "Botão Today");
			
			sleep(1000);
			
			path = "//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/form/div[4]/button[2]";
			clickXpath(driver, wait, path, "Save");
			
			System.out.println("Qualificação Adicionada com sucesso");
			
			itemQualification = wait.until(
					ExpectedConditions.visibilityOfElementLocated(By.xpath(pathQuantidade)));
			resultado = extrairNumero(itemQualification.getText()) - resultado;
		} catch (Exception e) {
			System.out.println("Erro durante Adição de Qualificação: " + e.getMessage());
			driver.quit();
		}
		return resultado;
	}
	
	public static void testEditUser(WebDriver driver, WebDriverWait wait) {
	    try {
	        String path = "//*[@id=\"app\"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a";
	        clickXpath(driver, wait, path, "Admin");

	        path = "//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[2]/div/div[6]/div/button[2]";
	        clickXpath(driver, wait, path, "Botão Editar");

	        path = "//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div";
	        clickXpath(driver, wait, path, "Dropdown User Role");
	        path = "//div[@role='listbox']/div[2]"; 
	        clickXpath(driver, wait, path, "Selecionar Admin");

	        path = "//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div";
	        clickXpath(driver, wait, path, "Dropdown Status");
	        path = "//div[@role='listbox']/div[3]"; 
	        clickXpath(driver, wait, path, "Selecionar Desabilitado");	
	       
	  
	        path = "//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[5]/div/div[2]/div/label/span/i"; 
	        clickXpath(driver, wait, path, "Trocar Senha");
	        
	        sleep(1000);
			
	        path = "//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input";
			fillInput(wait, path, "Teste123@!","Senha");
			
			path = "//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input";
			fillInput(wait, path, "Teste123@!","Confrimação Senha");

	        path = "//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]"; 
	        clickXpath(driver, wait, path, "Trocar Senha");
	        

			
	    } catch (Exception e) {
	        System.out.println("Erro ao adicionar usuário: " + e.getMessage());
	        driver.quit();
	    }
	}

	private static void clickCss(WebDriver driver, WebDriverWait wait,String cssSelector, String click) {
		System.out.println("clickCss: "+click);
		WebElement button = wait.until(ExpectedConditions.visibilityOfElementLocated(By.cssSelector(cssSelector)));
		button.click();
	}

	private static void clickXpath(WebDriver driver, WebDriverWait wait, String pathAddWork, String click) {
		System.out.println("clickXpath: "+click);
		wait.until(ExpectedConditions.presenceOfElementLocated(By.xpath(pathAddWork)));
		WebElement addWork = driver.findElement(By.xpath(pathAddWork));
		addWork.click();
	}

	private static void fillInput(WebDriverWait wait, String path, String text, String input) {
		System.out.println("fillInput: "+input);
		WebElement companyField = wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath(path)));
		companyField.clear();
		companyField.sendKeys(text);
	}

	private static void sleep(int time) {
		try {
			Thread.sleep(time);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
	}
	
	public static int extrairNumero(String texto) {
	    String numero = texto.replaceAll("\\D+", "");
	    return Integer.parseInt(numero);
	}

	public static void main(String[] args) {
		WebDriver driver = getDriver();
		WebDriverWait wait = getWait(driver);

		testLogin(driver, wait);
		testQualification(driver, wait);
		testEditUser(driver, wait);

		sleep(5000);

		closeDriver(driver);
	}

	public static void closeDriver(WebDriver driver) {
		if (driver != null) {
			driver.quit();
		}
	}

	public static WebDriverWait getWait(WebDriver driver) {
		WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(30));
		return wait;
	}

	public static WebDriver getDriver() {
		WebDriverManager.chromedriver().setup();
		WebDriver driver = new ChromeDriver();
		return driver;
	}

}
