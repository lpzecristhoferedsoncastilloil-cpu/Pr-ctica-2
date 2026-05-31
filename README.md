# Instrucciones - Testing Automatizado

Requisitos:
- Python 3.8+
- Google Chrome instalado
- Entorno virtual (recomendado)

1) Activar entorno virtual (PowerShell)

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
& .venv\Scripts\Activate.ps1
```

(Opcional - CMD)

```cmd
.venv\Scripts\activate.bat
```

2) Instalar dependencias

```powershell
pip install -r requirements.txt
```

3) Ejecutar un script

```powershell
python ejercicio1.py
python ejercicio2.py
python ejercicio6.py
```

Notas:
- `webdriver-manager` descargará automáticamente la versión compatible de ChromeDriver.
- Si ves errores de permiso en PowerShell, ejecuta la línea `Set-ExecutionPolicy` indicada arriba.
- No modifiqué tus scripts; si quieres que los ejecute o verifique sintaxis, dímelo y lo hago.
