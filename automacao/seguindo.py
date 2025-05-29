from selenium.webdriver.common.by import By
import time, random
from utils.arquivos import salvar_csv

def deixar_de_seguir(driver, shop_id, atualizar_status, quantidade=20):
    url = f"https://shopee.com.br/shop/{shop_id}/following?__classic__=1"
    driver.get(url)
    atualizar_status("🔄 Carregando perfis seguidos...")

    for _ in range(20):
        driver.execute_script("window.scrollBy(0, 600);")
        time.sleep(random.uniform(1.0, 2.0))

    botoes = driver.find_elements(By.XPATH, '//button[normalize-space(text())="Seguindo"]')
    resultados = []

    for i, btn in enumerate(botoes[:quantidade]):
        try:
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
            time.sleep(random.uniform(0.3, 0.6))
            btn.click()
            time.sleep(0.4)

            confirmar = driver.find_element(By.XPATH, '//button[normalize-space(text())="Deixar de seguir"]')
            confirmar.click()

            resultados.append((i+1, f"Perfil {i+1}", "Deixado de seguir"))
            atualizar_status(f"🚫 {i+1} perfis deixados de seguir...")

            # pausa a cada 10 perfis
            if (i + 1) % 10 == 0:
                time.sleep(random.uniform(3.0, 5.0))
            else:
                time.sleep(random.uniform(0.5, 1.0))

        except:
            resultados.append((i+1, "Erro ao deixar de seguir", "Falha"))


    salvar_csv("deixados_de_seguir.csv", resultados)
    atualizar_status("✅ Perfis removidos com sucesso.")
