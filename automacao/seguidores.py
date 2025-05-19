from selenium.webdriver.common.by import By
import time, random
from utils.arquivos import salvar_csv

def seguir_usuarios(driver, shop_id, atualizar_status):
    url = f"https://shopee.com.br/shop/{shop_id}/followers?__classic__=1"
    driver.get(url)
    atualizar_status("🔄 Carregando seguidores...")

    for _ in range(20):
        driver.execute_script("window.scrollBy(0, 600);")
        time.sleep(random.uniform(1.0, 2.0))

    botoes = driver.find_elements(By.XPATH, '//button[normalize-space(text())="+Seguir"]')
    resultados = []

    for i, btn in enumerate(botoes[:20]):
        try:
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
            time.sleep(random.uniform(1.0, 1.5))
            btn.click()
            time.sleep(1.0)

            try:
                nome = btn.find_element(By.XPATH, './preceding::div[contains(@class, "q96n7h")][1]').text.strip()
            except:
                nome = f"usuario {i+1}"

            resultados.append((i+1, nome, "Seguido"))
            atualizar_status(f"✅ Seguindo {i+1} usuários...")
            time.sleep(random.uniform(2.0, 3.0))
        except:
            resultados.append((i+1, "Erro ao clicar", "Falha"))

    salvar_csv("seguidos.csv", resultados)
    atualizar_status("✅ Seguidores seguidos e salvos.")
