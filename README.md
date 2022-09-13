# GSHEET INTEGRATION
- URL DEPLOY = https://still-shore-34711.herokuapp.com/
- username = franciscobarros
- password = pruebatecnica123
## Cómo correr el repositorio
- Debes tener instalado python 3.9 o superior.
- Debes tener instalado Django 4.1.
- Posicionate en el directorio raíz, y correr el comando ```pip install -r requirements.txt``` (o ```pip3```)
- Corre el comando ```python3 manage.py runserver```
- Corre las migraciones usando ```python3 manage.py migrate```
- Listo!
## Cómo funciona
- Es una aplicación básica de Django, que usa la librería de autenticación de Django.
- La aplicación tiene solo tres rutas: ruta raíz ```/```, ruta login ```/login```, y ruta con la GoogleSheet ```/googlesheet```.
- La ruta /googlesheet despliega un HTML básico con un ```ifram``` embebido. Este ```ifram``` apunta a una hoja de cálculo de Google, son acceso público que puedes encontrar en este link: https://docs.google.com/spreadsheets/d/1pOVy_FuQGYI-yaeGIAsPss9MdmiXOeHbLOBggfhXa7E/edit?usp=sharing.
- La hoja de cálculo implementa un Script usando Apps Scripts de Google para envíar la HTTP POST REQUEST. Este Script es el siguiente (se puede encontrar en la pestaña Extensiones -> Apps Script del GoogleSheet):
```
function validateEmail(email) {
  var re = /\S+@\S+\.\S+/;
  if (!re.test(email)) {
    throw new Error("Invalid email");
  }
  return true;
};

function validateHeader(header) {
  if (header !== "Tasa") {
    throw new Error("You have edited an invalid column");
  }
  return true;
}

function validateRate(_rate) {
  try {
    var rate = parseFloat(_rate);
    return rate;
  } catch {
    throw new Error("Invalid rate on sheet");
  }
}

function validateId(_id) {
  try {
    var id = parseInt(_id);
    return id;
  } catch {
    throw new Error("Invalid ID on sheet");
  }
}

function onEditCell(e) {
  var url = 'https://hooks.zapier.com/hooks/catch/6872019/oahrt5g/'
  var col = e.range.getColumn();
  var row = e.range.getRow();
  var header = SpreadsheetApp.getActiveSheet().getRange(1, col).getValue();
  Logger.log(header);
  var email = SpreadsheetApp.getActiveSheet().getRange(row, col + 1).getValue();

  // validations
  var rate = validateRate(e.value);
  var id = validateId(SpreadsheetApp.getActiveSheet().getRange(row, col - 1).getValue())
  validateEmail(email);
  validateHeader(header);

  // build request
  var data = {
    "idOp" : id,
    "tasa" : rate,
    "email" : email,
  };
  var payload = JSON.stringify(data);
  var options = {
    "method" : "POST",
    "contentType" : "application/json",
    "payload" : payload
  };

  //request
  var response = UrlFetchApp.fetch(url, options);
  Logger.log(email);
  Logger.log(id);
  Logger.log(rate);
  Logger.log(response);
};
```
