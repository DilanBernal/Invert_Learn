# Invert Learn

Comandos para ejecutar el proyecto:
* Gateway
```
python -m uvicorn gateway.main:app --reload
```
* Web
```
npm run dev
```
* Escritorio 
```
npm run electron
 (si es en windows agregarle una w al final de electron)
npm run electronw
```
> [!NOTE]
> Notas importantes
Antes de ejecutar los proyectos, hay que instalar los paquetes:
### Web y escritorio
- Pararse en la carpeta con ```cd frontend/web o escritorio```
- ejecutar el comando ```npm install``` o ```npm i```
### Backend 
- crear entorno virtual
- Con ```pip install``` instalar las siguientes libreriaas
- ```fastapi```
- ```pymysql```
- ```uvicorn```
- ```mysql.connector```
- ```psycopg2```
- ```urllib```
- ```typing```
- ```pydantic```
