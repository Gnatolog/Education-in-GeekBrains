# Проект Notion Application by Python
###  *Информация о проекте*
Необходимо написать проект, содержащий функционал работы с заметками.
Программа должна уметь создавать заметку, сохранять её, читать список
заметок, редактировать заметку, удалять заметку.

***
### *Задание*
**Реализовать**: консольное приложение заметки, с сохранением, чтением,
добавлением, редактированием и удалением заметок. Заметка должна
содержать идентификатор, заголовок, тело заметки и дату/время создания или
последнего изменения заметки. Сохранение заметок необходимо сделать в
формате json или csv формат (разделение полей рекомендуется делать через
точку с запятой).

**Реализацию** пользовательского интерфейса студент может
делать как ему удобнее, можно делать как параметры запуска программы
(команда, данные), можно делать как запрос команды с консоли и
последующим вводом данных, как-то ещё, на усмотрение студента.

**Например**:
***
1 python notes.py

2 add --title "новая заметка"

3 –msg "тело новой заметки"
***
**Или так**:
***
1 python note.py

2 Введите команду: add

3 Введите заголовок заметки: новая заметка

4 Введите тело заметки: тело новой заметки

5 Заметка успешно сохранена

6 Введите команду:
***
### При чтении списка заметок реализовать фильтрацию по дате