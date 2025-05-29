from selenium.webdriver.common.by import By
import time, random
from utils.arquivos import salvar_csv

def seguir_usuarios(driver, shop_id, atualizar_status, quantidade=20):
    url = f"https://shopee.com.br/shop/{shop_id}/followers?__classic__=1"
    driver.get(url)
    atualizar_status("🔄 Carregando seguidores...")

    for _ in range(20):
        driver.execute_script("window.scrollBy(0, 600);")
        time.sleep(random.uniform(1.0, 2.0))

    botoes = driver.find_elements(By.XPATH, '//button[normalize-space(text())="+Seguir"]')
    resultados = []

    for i, btn in enumerate(botoes[:quantidade]):
        try:
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
            time.sleep(random.uniform(0.3, 0.6))  # 🔽 delay reduzido
            btn.click()
            time.sleep(0.4)

            try:
                nome = btn.find_element(By.XPATH, './preceding::div[contains(@class, "q96n7h")][1]').text.strip()
            except:
                nome = f"usuario {i+1}"

            resultados.append((i+1, nome, "Seguido"))
            atualizar_status(f"✅ Seguindo {i+1} usuários...")

            # 🔁 pausa a cada 10 seguidores
            if (i + 1) % 10 == 0:
                time.sleep(random.uniform(3.0, 5.0))
            else:
                time.sleep(random.uniform(0.5, 1.0))  # 🔽 entre ações

        except:
            resultados.append((i+1, "Erro ao clicar", "Falha"))


    salvar_csv("seguidos.csv", resultados)
    atualizar_status("✅ Seguidores seguidos e salvos.")

