
  
    var oReq = new XMLHttpRequest();
    oReq.onload = reqListener;
    oReq.open("get", ".json", true);
    oReq.responseType = 'json';
    oReq.send();