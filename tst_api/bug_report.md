## Requirements
- AR - actual result
- DR - desired result

## Check-list

|Request|Description|Status|Bug ID|
---| --- | --- | ---
| - Request = /users |1. ввести |Passed| |
| - Method = POST
|||||
| - Request = /users||Passed||
| - Method = PUT
|||||

## Баг 1
**Description:**
Запрос без id возвращает код 404

**Enviroment:**
[server](http://bzteltestapi.pythonanywhere.com/)

**Steps to reproduce:**
		Через api отправить запрос {{server}}users

- **DR**: код ответа = 400 Bad Request
- **AR**: Ответ
```json
{
    "code": 404,
    "message": "Not Found."
}
```
