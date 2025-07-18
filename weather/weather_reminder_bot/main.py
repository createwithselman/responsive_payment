# main.py
from weather import get_weather
from tasks import add_task, show_tasks
import logging
import log_config

def main():
    print("🌤️  Hava Durumu + Hatırlatıcı Bot")
    sehir = input("Şehrini gir: ")
    print(get_weather(sehir))

    show_tasks()

    secim = input("\nYeni görev eklemek ister misin? (e/h): ")
    if secim.lower() == "e":
        gorev = input("Görevi yaz: ")
        add_task(gorev)
        print("✅ Görev eklendi.")
    else:
        print("Tamamdır, görev eklenmedi.")

    logging.info("Bot çalışması tamamlandı.")

if __name__ == "__main__":
    main()
    