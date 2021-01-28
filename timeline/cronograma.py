import schedule
import os
import time



print("Cronograma iniciado")
schedule.every(2).minutes.do(lambda: os.system('scrapy crawl globo_news'))
print(f"Próximo trabalho está configurado para rodar as {str(schedule.next_run())}")


while True:
    schedule.run_pending()
    time.sleep(1)
