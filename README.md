# 🏦 Bank Account Application (Python)

Prosta aplikacja konsolowa symulująca konto bankowe z obsługą PIN-u, wpłat, wypłat oraz limitem debetu.

Projekt został napisany w Pythonie w celu nauki programowania obiektowego oraz obsługi wyjątków.

---

## 📌 Funkcjonalności

- 🔐 Logowanie przy użyciu kodu PIN (maksymalnie 3 próby)
- 💰 Wpłata środków na konto
- 💸 Wypłata środków z kontrolą limitu debetu
- ⚠️ Obsługa błędów (niepoprawne kwoty, przekroczenie limitu)
- 🧾 Aktualne saldo wyświetlane po każdej operacji

---

## 🛠 Technologie

- Python 3
- Programowanie obiektowe (OOP)
- Obsługa wyjątków (`ValueError`)
- Pętla `while`
- Instrukcje warunkowe

---

## 🧠 Logika działania

### Klasa `Bank`

Aplikacja opiera się na klasie `Bank`, która przechowuje:

- `amount` – aktualne saldo konta
- `overdraft_limit` – maksymalny dozwolony debet (1000 zł)

### Metody:

- `add_money(money)`  
  Dodaje środki do konta (kwota musi być większa od 0)

- `withdraw_money(money)`  
  Wypłaca środki z konta:
  - kwota musi być większa od 0
  - nie może przekroczyć limitu debetu

---

## 🔐 Autoryzacja

Użytkownik musi podać poprawny PIN (3 próby).

Po 3 nieudanych próbach konto zostaje zablokowane.

---

## ▶️ Jak uruchomić projekt

1. Sklonuj repozytorium:
   ```bash
   git clone https://github.com/Marcin45-45/aplikacja_bank.git
