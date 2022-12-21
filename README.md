
# OpenAI_Discord_BOT

## Prosta integracja OpenAI z Discordem napisana w języku PYTHON.

**Wystarczy jedna komenda!**

>     /chat [message]

## Pamiętaj o instalacji środowiska Python i odpowiednich bibliotek
**Instalacja Python w systemie Ubuntu,**

1.  Otwórz terminal w swoim systemie Ubuntu i wpisz następujące polecenie, aby zaktualizować listę pakietów:
**`sudo apt-get update`** 
2.  Następnie wpisz następujące polecenie, aby zainstalować Pythona:
**`sudo apt-get install python3`**
3.  Po zainstalowaniu Pythona możesz sprawdzić jego wersję, wpisując następujące polecenie:
**`python3 -V`**

**Instalacja biblioteki openai i discord w systemie Ubuntu**

- Otwórz terminal i upewnij się, że masz zainstalowane narzędzie **`pip`**, które jest menedżerem pakietów dla języka **Python**. Możesz to sprawdzić, wpisując polecenie **`pip --version`**. Jeśli nie masz zainstalowanego **pip**, możesz go zainstalować, wpisując polecenie **`sudo apt-get install python3-pip`**.
- Zainstaluj bibliotekę **openai** przy użyciu **pip**. **Wpisz polecenie `pip install openai`**.
- Zainstaluj bibliotekę **discord** przy użyciu **pip**. Wpisz polecenie **`pip install discord`**.

*Uwaga: Upewnij się, że masz zainstalowane odpowiednie wymagania systemowe dla obu bibliotek. W przypadku biblioteki **openai** mogą to być na przykład biblioteki **tensorflow** lub **tensorflow-cpu**. W przypadku biblioteki **discord** mogą to być biblioteki **aiohttp**, **websockets** lub inne, w zależności od tego, jakie funkcje będziesz chciał użyć.*



# Uruchomienie bota
## Krok 1: Utwórz bota Discord
1. Przejdź do https://discord.com/developers/applications utwórz aplikację
2. Zbuduj bota Discord pod aplikacją
3. Pobierz token z ustawienia bota
4. Podmień wartości dla*** discord_bot_token***

## Krok 2: Wygeneruj klucz API OpenAI
1. Przejdź do https://beta.openai.com/account/api-keys
2. Kliknij "Utwórz nowy tajny klucz"
3. Podmień wartości dla ***openAI_key***

## Krok 3: Uruchom bota
1. Otwórz terminal lub wiersz polecenia
2. Przejdź do katalogu, w którym zainstalowałeś bota ChatGPT Discord
3. Uruchom ***python3 bot.py***, aby uruchomić bota
