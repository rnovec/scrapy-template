# -*- coding: utf-8 -*-

# Selenium settings for sii project
#
# For simplicity, this file contains settings considered important to 
# run selenium webdriver in background:
#
# Este archivo se encarga de la configuración por defecto para Selenium WebDriver
# `chrome_options` y sus argumentos se asegura que selenium se ejecute en 
# segundo plano sin abrir el navegador.
#
# in any file: from sii.selenium import browser

from selenium import webdriver
import os
import json

# rutas de ejecutables
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHROMEDRIVER_PATH = os.path.join(BASE_DIR, 'chromedriver')

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN") # configuración para heroku
settings = {"recentDestinations": [{"id": "Save as PDF", "origin": "local",
                                    "account": ""}], "selectedDestinationId": "Save as PDF", "version": 2}
profile = {
    # 'printing.print_preview_sticky_settings.appState': json.dumps(settings),
    "download.default_directory": BASE_DIR, #Change default directory for downloads
    "download.prompt_for_download": False, #To auto download the file
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True
}

# comente estas lineas si desea mostrar el navegador
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--disable-dev-shm-usage")
# chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--no-sandbox")
chrome_options.add_experimental_option("prefs", profile)
chrome_options.add_argument('--kiosk-printing')

# singleton de selenium
browser = webdriver.Chrome(os.environ.get(
    "CHROMEDRIVER_PATH", CHROMEDRIVER_PATH), chrome_options=chrome_options)


