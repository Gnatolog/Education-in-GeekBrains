# **Инструкция для работы с Git и удалёнными репозиториями**

## **Что такое Git?**
<image src="/home/robert/Desktop/Git/Gitart.jpeg" alt="logo git">

___
Git - это одна из реализаций распределённых систем контроля версий, имеющая как и локальные, так и удалённые репозитории. Является самой популярной реализацией систем контроля версий в мире.

## **Подготовка репозитория**
<image src="/home/robert/Desktop/Git/repository.png" alt="logo git">
___
Для создание репозитория необходимо выполнить команду git init в папке с репозиторием и у Вас создаться репозиторий (появится скрытая папка .git)

## **Создание коммитов**
<image src="/home/robert/Desktop/Git/commit.jpeg" alt="logo git">
___
### **Git add**

Для добавления измений в коммит используется команда git add. Чтобы использовать команду git add напишите git add <имя файла>

### **Просмотр состояния репозитория**

Для того, чтобы посмотреть состояние репозитория используется команда git status. Для этого необходимо в папке с репозиторием написать git status, и Вы увидите были ли измения в файлах, или их не было.

### **Создание коммитов**

Для того, чтобы создать коммит(сохранение) необходимо выполнить команду git commit. Выполняется она так: git commit -m "<сообщение к коммиту>. Все файлы для коммита должны быть ДОБАВЛЕНЫ и сообщение к коммиту писать ОБЯЗАТЕЛЬНО.

## **Перемещение между сохранениями**
<image src="/home/robert/Desktop/Git/save changes.gif" alt="logo git">
___
ля того, чтобы перемещаться между коммитами, используется команда git checkout. Используется она в папке с пепозиторием следующим образом: git checkout <номер коммита>

## **Журнал изменений**
<image src="/home/robert/Desktop/Git/jurnal.jpg" alt="logo git">
___
Для того, чтобы посмтреть все сделанные изменения в репозитории, используется команда git log. Для этого достаточно выполнить команду git log в папке с репозиторием

## **Ветки в Git**
<image src="/home/robert/Desktop/Git/branchesgit.jpg" alt="logo git">
___
### Создание ветки
Для того, чтобы создать ветку, используется команда git branch. Делается это следующим образом в папке с репозиторием: git branch <название новой ветки>

## **Слияние веток**
___
Для того чтобы дабавить ветку в текущую ветку используется команда git merge 

## **Удаление веток**
___
Для удаления ветки ввести команду "git branch -d 'name branch'"

## *__Работа с удалённым репозиторием__*
1. Для работы с удалённым репозиторием необходимо зарегестрироваться на удаленном сервере. К примеру GitHub.
2. Необходимо создать удалённый репозиторий на самом сервере
3. После чего необоходимо создать локальный репозиторий при помощи команды git init или же использовать уже имеющийся.
4. Следущий важный шаг связать локальный репозиторий и удаленный репозиторий для это го после того как будет создан репозитория на GitHub нужно следовать инструкйии. В частности прописать 3 команды в своём терминале:
            
            * git remote add origin
            * git branch -M main
            * git push -u origin main

5. Как только будту завершены данные действия Вы сможете использовать такие команды как:

            * git push - для отправки изменений на удаленный репозиторий
            * git pull - для закачивания и слияния изменений которые внесены на удалёном репозитории
## **Как сделать pull request** 
1. Делаем **Fork** репозитория
2. Делаем **git clone Своей версии** репозитория
3. **Создаём новую ветку** и в нёё вносим свои изменения
4. Фиксируем изменения **(делаем git commit)**
5. Отправляем свою весию в **свой GitHub**
6. На Git Hub нажимаем кнопку **pull request**