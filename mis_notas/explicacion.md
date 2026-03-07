# Notas sobre Git y .gitignore

## ¿Qué es .gitignore?

".gitignore" es un archivo que le indica a Git qué archivos o carpetas no debe rastrear ni subir al repositorio.

Esto se usa para evitar subir:

- notas personales
- archivos temporales
- configuraciones locales
- archivos generados automáticamente por programas

Git simplemente ignorará todo lo que coincida con las reglas del archivo.

---

Cómo crear un .gitignore

Crear el archivo en la raíz del proyecto:

nano .gitignore

Luego agregar los archivos o carpetas que no queremos subir.

Ejemplo:

mis_notas/
notas_privadas.txt
*.log
*.tmp

---

Ignorar carpetas completas

Si se agrega una barra "/", Git ignorará toda la carpeta.

Ejemplo:

mis_notas/

Todo lo que esté dentro de esa carpeta será ignorado.

---

Ignorar tipos de archivos

Se pueden usar comodines.

Ejemplo:

*.log
*.tmp
*.pyc

Esto evita subir archivos temporales o compilados.

---

Problema común

Si un archivo ya fue agregado al repositorio antes de ponerlo en ".gitignore", Git seguirá rastreándolo.

Para solucionarlo:

git rm --cached nombre_archivo

Ejemplo:

git rm --cached notas_privadas.txt

Después hacer commit normalmente.

---

Archivos que normalmente se ignoran en Python

__pycache__/
*.pyc
*.pyo
*.log

Python genera estos archivos automáticamente y no es necesario subirlos.

---

Comandos básicos de Git

Ver estado del repositorio:

git status

Ver cambios antes de hacer commit:

git diff

Agregar archivos:

git add archivo.py

Agregar todos los archivos modificados:

git add .

Crear un commit:

git commit -m "mensaje del commit"

Subir cambios al repositorio:

git push

---

Flujo básico de trabajo en Git

1. Editar archivos
2. Ver cambios

git status
git diff

3. Agregar cambios

git add .

4. Crear commit

git commit -m "Descripción del cambio"

5. Subir al repositorio

git push

---

Buenas prácticas

- Nunca subir contraseñas o tokens.
- Usar ".gitignore" para archivos privados.
- Escribir mensajes de commit claros.
- Revisar cambios con "git diff" antes de hacer commit.
- Hacer commits pequeños y frecuentes.

---

Notas personales

Guardar documentación personal en carpetas ignoradas por Git puede ser útil para:

- guardar comandos
- escribir ideas
- documentar errores
- guardar aprendizaje

Esto permite tener notas dentro del proyecto sin publicarlas.
