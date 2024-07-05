from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Functions.Funciones import funcionesGlobales
from Excel.Funciones_ex import Funexel

class paginaLogin:
    def __init__(self, driver):
        self.driver = driver

    def login(self):
        driver = self.driver
        gf = funcionesGlobales(driver)
        fe = Funexel(driver)
        gf.navegar("https://demoqa.com/text-box")
        ruta = "C://Users//USER//PycharmProjects//DataDriven//Datos.xlsx"
        filas = fe.getRowCount(ruta, "Hoja 1")

        for r in range(2, filas + 1):
            Full_Name = fe.readData(ruta, "Hoja 1", r, 1)
            Email = fe.readData(ruta, "Hoja 1", r, 2)
            Current_Addres = fe.readData(ruta, "Hoja 1", r, 3)
            Permanent_Addres = fe.readData(ruta, "Hoja 1", r, 4)

            gf.globalInput("//input[@id='userName']",Full_Name)
            gf.globalInput("//input[@id='userEmail']",Email)
            gf.globalInput("//textarea[@id='currentAddress']",Current_Addres)
            gf.globalInput("//textarea[@id='currentAddress']",Permanent_Addres)
            gf.clicInput("//button[@id='submit']")

            e = gf.Existe("//input[@id='userName']")
            if (e =="Existe"):
                print("El elemento se insertó correctamente")
                fe.writeData(ruta,"Hoja 1",r,5,"Checked")
            else:
                print("No se insertó correctamente")
                fe.writeData(ruta,"Hoja 1",r,5,"Error")
