Dziennik Nauki
Aplikacja webowa napisana w Django, której celem jest umożliwienie użytkownikowi zarządzania tematami nauki oraz śledzenia postępów
projekt został wykonany w architekturze MVC (Model-View-Controller), zgodnie z wymaganiami zaliczeniowymi.

Opis projektu
Dziennik Nauki pozwala użytkownikowi dodawać tematy związane z nauką, określać poziom zaawansowania, opisywać osiągnięcia oraz dodawać notatki do poszczególnych tematów
użytkownik musi się zalogować, aby korzystać z funkcjonalności aplikacji.
Projekt wykorzystuje dwie powiązane ze sobą tabele: Temat oraz Notatka. Każdy temat jest powiązany z konkretnym użytkownikiem, a każda notatka przypisana jest do jednego tematu

Funkcjonalności
System logowania i wylogowywania
Dodawanie, edytowanie i usuwanie tematów nauki
Dodawanie notatek do tematów
Filtrowanie tematów po nazwie (wyszukiwanie)
Walidacja danych po stronie serwera
Stylizacja interfejsu użytkownika z użyciem Bootstrap
Bezpieczny dostęp do danych tylko dla zalogowanego użytkownika

Instalacja
Aby uruchomić aplikację lokalnie:
Sklonuj repozytorium lub pobierz kod źródłowy.
Utwórz środowisko wirtualne
Wykonaj migracje: python manage.py migrate.
Utwórz konto superużytkownika: python manage.py createsuperuser.
Uruchom serwer: python manage.py runserver.
Przejdź do przeglądarki: http://127.0.0.1:8000/

Technologie
Django wersja 5.1.6
Python 3.13.3
SQLite jako domyślna baza danych
HTML, CSS
Bootstrap (CDN)

Podsumowanie
Projekt spełnia podstawowe wymagania zaliczeniowe. Dodatkowo zawiera rozszerzenia:
dodano drugi model (Notatka) i relację z modelem głównym (Temat),
zastosowano stylizację interfejsu (Bootstrap),
wprowadzono funkcję filtrowania (wyszukiwania tematów),
zaimplementowano logikę sesji użytkownika,
dodano walidację danych