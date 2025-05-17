import time

# Ключевые слова и очки
keywords = {
    "секретная операция": 15,
    "цель": 10,
    "агент": 10,
    "зашифрованное сообщение": 10,
    "записи": 10,
    "перенаправление": 5,
    "отчёт": 10,
    "протокол": 5,
    "доступ": 10,
    "проникновение": 15,
    "срочно": 10,
    "важно": 10,
    "конфиденциально": 10
}

# Логи KGB
kgb_log = [
    "[09:00] Агент007: Утренний брифинг начался. У тебя есть детали секретной операции?",
    "[09:02] АгентX: Два человека направлены в целевую зону. Связь держим открытой.",
    "[09:05] АгентMira: Ответа на вчерашний отчёт ещё нет. Будьте осторожны.",
    "[09:10] Агент007: Зашифрованные сообщения передаются только участникам красного протокола.",
    "[09:13] АгентX: Поступили новые записи. Жду перенаправления.",
    "[09:16] АгентMira: Проникновение будет без прерывания связи. Внимание."
]

# Ответы агентов
cevap_sartlari = {
    "отчёт": "[АгентX]: Это меня заинтересовало. Отправляю файл с отчётом.",
    "зашифрованное сообщение": "[АгентMira]: Не выноси зашифрованные сообщения за пределы канала!",
    "цель": "[Агент007]: Кто именно цель? Уточни.",
    "секретная операция": "[АгентX]: Детали операции в файле. Продолжай."
}

# Подсчёт очков
def puan_hesapla(metin):
    puan = 0
    metin = metin.lower()
    for kelime, deger in keywords.items():
        if kelime in metin:
            puan += deger
    return puan

# Проверка на ответы агентов
def yanit_var_mi(metin):
    metin = metin.lower()
    cevaplar = []
    for kelime, yanit in cevap_sartlari.items():
        if kelime in metin:
            cevaplar.append(yanit)
    return cevaplar

def main():
    print("=== Внутренний терминал связи KGB ===\n")
    print("Перехвачены сообщения агентов...\n")

    for satir in kgb_log:
        print(satir)
        time.sleep(2)

    print("\n>> Теперь напиши фишинговое письмо на основе этих сообщений.")
    print("(Оставь строку пустой, чтобы завершить письмо)\n")

    eposta = ""
    while True:
        satir = input()
        if satir.strip() == "":
            break
        eposta += satir + " "

    toplam_puan = puan_hesapla(eposta)
    print(f"\n📩 Очки за письмо: {toplam_puan}")

    if toplam_puan >= 30:
        print("✅ Письмо оказалось убедительным. Ответы от агентов...\n")
        time.sleep(1)
        cevaplar = yanit_var_mi(eposta)
        yanit_puan = 0
        for cevap in cevaplar:
            print(cevap)
            yanit_puan += 10
            time.sleep(1)

        toplam_puan += yanit_puan
        print(f"\n📡 Очки за ответы: {yanit_puan}")
        print(f"🎯 Общие очки: {toplam_puan}")

        if toplam_puan >= 50:
            print("\n🎉 Поздравляем! Получен файл: [отчёт.pdf] (возможно содержит эксплойт) güel şidmi ctf.py e gel ve /bağlan yaz")
        else:
            print("\n🔒 Ответы получены, но защита всё ещё активна. aman kendimi kaptırdım dur jsjsjsjsj")
    else:
        print("❌ Письмо не убедительно. Ответов нет.")

if __name__ == "__main__":
    main()
