# OneSpan Sign Connector — Connector Discovery

**Official Documentation:** https://onespan.com  
**Base URL:** https://sandbox.esignlive.com/api  
**Auth Model:** API Key (Authorization: Basic <key>)  

## Основные сущности вендора
- пакеты документов (/packages), получатели, поля для подписей, аудитный журнал (evidence summary)

## Лимиты и особенности API
- Соблюдение Rate Limits вендора, обработка HTTP 429 с экспоненциальным backoff.
- Валидация входных данных по Pydantic-схемам вендора до отправки запроса.
- Тестовая точка проверки подключения: `GET /api/user`.
