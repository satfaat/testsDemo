## Email
### Attributes
- type: string
- required: yes
- format: Recipient_name@Domain_name.Top-level_domain
- Recipient_name length: maximum of 64 characters
### Description: 
Если строка не соответствует формату,
- то выводится предупреждение.
- Submit button not active.

### Positive
#### english [a-zA-Z]:
- maiL@mail.com
#### digit [0-9]:
- 1mail@mail2.ru
- 15@mail.gov

#### symbols in the middle: ! # $ % & ' * + - / = ? ^ _ ` { | 
- dot+ma@mail.ru
- 100%@m.com
- 2^@m.ro
- 50$@la.lo
- be/not_be@ko.sh
#### dash, hyphen:
- my-mail@mail.ln
#### dot, period:
- sf.mail@m.net
- sg.@mail.ca.be
#### underscore:
- top_mai@sky.com.au

### Negative
#### russian
- адр@mail.ru

#### symbols as first char in Recipient name: ! # $ % & ' * + - / = ? ^ _ ` { | 
- !mail@m.ru
- #call@m.rr
- _mail@club.dot
- `to`@mn.nm
- *@m.tt
- ~dog@dog.com
- =mail@..ru

#### Alternative special characters such as  " ( ) , : ; < > @ [ \ ] 
- (if)@ru.ru
- cool@@m.ru
- tom,go@m.fr
- Tom:json@m.fr
- go;run@m.tt
- tag<>@jk.lo
- key[value]@bit.ch
- my\key@ul.go

#### no format:
- mailmail.ru
- @nm.ru
- goo@.ru
- go@
- today break@jo.ru
- empty field
- 12345678
- cosmoscom

## Password
### Attributes
- type: ?
- required: yes

char_length: >=4
Если пароль не совпадает со значением в поле Confirm password или меньше 4 символов,
то выводится сообщение об ошибке.

#### [4-бесконечность] positive
- 4 to44, 10 fivee54698, 100 need string generator
#### [0-3] negative
- empty filed
- 1 f, 3 tri

## Submit button
Send data to server