from selenium.webdriver.common.by import By
import time, random
from utils.arquivos import salvar_csv

def deixar_de_seguir(driver, shop_id, atualizar_status):
    url = f"https://shopee.com.br/shop/{shop_id}/following?__classic__=1"
    driver.get(url)
    atualizar_status("🔄 Carregando perfis seguidos...")

    for _ in range(20):
        driver.execute_script("window.scrollBy(0, 600);")
        time.sleep(random.uniform(1.0, 2.0))

    botoes = driver.find_elements(By.XPATH, '//button[normalize-space(text())="Seguindo"]')
    resultados = []

    for i, btn in enumerate(botoes[:20]):
        try:
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
            time.sleep(random.uniform(1.0, 1.5))
            btn.click()
            time.sleep(1.0)

            confirmar = driver.find_element(By.XPATH, '//button[normalize-space(text())="Deixar de seguir"]')
            confirmar.click()

            resultados.append((i+1, f"Perfil {i+1}", "Deixado de seguir"))
            atualizar_status(f"🚫 {i+1} perfis deixados de seguir...")
            time.sleep(random.uniform(2.0, 3.0))
        except:
            resultados.append((i+1, "Erro ao deixar de seguir", "Falha"))

    salvar_csv("deixados_de_seguir.csv", resultados)
    atualizar_status("✅ Perfis removidos com sucesso.")
