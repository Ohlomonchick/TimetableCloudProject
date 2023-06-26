# TimetableCloudProject

** Запуск производится в K8s **

Все необходимые конфиги в k8s/apps. Первым шагом необходимо создать postgres PV и PVC. Далее запуск подов и Сервисов в любом порядке.

Бэкенд и конфиги для Kubernetes микросервисного проекта расписания занятий для учебных заведений и расписания мероприятий для организаций.

![interface](https://github.com/Ohlomonchick/TimetableCloudProject/blob/main/gitimages/interface.png?raw=true)

Основан на Django REST Framework. 

- Kubernetes задействует Ingress.
- Несколько реплик каждого из сервисов
- Бесшовное обновление
- Отличная расширяемость 


**Поддержка любых сторонних интерфейсов. **

Например, реализованы админ-панель и уведомления об ивентах в telegram:

![telegram](https://github.com/Ohlomonchick/TimetableCloudProject/blob/main/gitimages/admintelegram.png?raw=true)



