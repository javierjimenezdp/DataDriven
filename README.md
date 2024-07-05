# DataDriven

# Automatización con Selenium y Python

Este proyecto está enfocado en la automatización de pruebas utilizando Selenium WebDriver y Python. Utiliza la metodología Page Object para mejorar la mantenibilidad y reusabilidad del código en la automatización de flujos de trabajo específicos, como el login en una aplicación web.

## Autor

- **Autor**: Javier Jiménez
- **Rol**: QA Analyst
- **Contacto**: 
  - Email: [ing.javierdavidjp@gmail.com](mailto:ing.javierdavidjp@gmail.com)
  - LinkedIn: [Javier Jiménez on LinkedIn](https://www.linkedin.com/in/javierjim%C3%A9nez1021/)

## Requisitos del Sistema

- Python 3.x
- Selenium WebDriver
- Navegador web compatible (por ejemplo, Chrome, Firefox)

## Instalación

1. **Instalación de Python**:
   - Descargar e instalar Python desde [python.org](https://www.python.org).

2. **Configuración de entorno virtual** (opcional pero recomendado):
   ```bash
   pip install virtualenv
   virtualenv env
   .\env\Scripts\activate  # Windows
   source env/bin/activate  # macOS/Linux
   ```

3. **Instalación de Selenium**:
   ```bash
   pip install selenium
   ```

4. **Configuración del WebDriver**:
   - Descargar el WebDriver correspondiente al navegador deseado y asegurarse de que esté en el PATH del sistema.

## Estructura del Proyecto

- **Funciones/funciones.py**: Contiene funciones de utilidad y métodos generales de Selenium.
- **Excel/Funciones_ex.py**: Funciones específicas para interactuar con archivos Excel.
- **Functions/Page_login.py**: Implementación de Page Objects para las páginas de login.
- **LoginQA/ToolsLogin.py**: Archivo principal de pruebas utilizando unittest para ejecutar las pruebas.

## Automatización y Page Objects

Este proyecto utiliza la metodología Page Object para abstraer la lógica de la interfaz de usuario. Cada página de la aplicación web tiene su propia clase de Page Object, lo que facilita el mantenimiento y la reutilización del código.

## Uso de Data-Driven Testing

Se emplea Data-Driven Testing para ejecutar pruebas con diferentes conjuntos de datos, utilizando archivos Excel para almacenar los datos de prueba.

## Ejecución de Pruebas

Para ejecutar las pruebas, utiliza `unittest`:

```bash
python -m unittest LoginQA.ToolsLogin
```

## Contribución

Si deseas contribuir a este proyecto, sigue estos pasos:

1. Fork el repositorio y clónalo localmente.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Agrega nueva funcionalidad'`).
4. Push a la rama (`git push origin feature/nueva-funcionalidad`).
5. Crea un nuevo Pull Request.

## Problemas Conocidos

- Problemas comunes encontrados durante el desarrollo y ejecución de pruebas.
- Soluciones recomendadas para resolver problemas técnicos específicos.

## Licencia

Este proyecto se distribuye bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.
