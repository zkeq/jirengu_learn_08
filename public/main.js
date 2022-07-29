getCSS.onclick = function() {
  const xhr = new XMLHttpRequest();
  xhr.open('GET', '/style.css');
  xhr.onreadystatechange = () =>{
    if(xhr.readyState === 4 && xhr.status === 200){
    const style = document.createElement('style');
    style.innerHTML = xhr.responseText;
    document.head.appendChild(style);
  }
}
  xhr.send();
}

getJS.onclick = function() {
  const xhr = new XMLHttpRequest();
  xhr.open('GET', '/2.js');
  xhr.onload = function() {
    // const script = document.createElement('script');
    // script.innerHTML = xhr.responseText;
    // document.head.appendChild(script);
    eval(xhr.responseText);
  }
  xhr.send();
}

let index = 1;
getHTML.onclick = function() {
  const xhr = new XMLHttpRequest();
  xhr.open('GET', `/3.htm`);
  xhr.onload = function() {
    const div = document.createElement('div');
    div.innerHTML = xhr.responseText;
    document.body.appendChild(div);
  }
  xhr.send();
}

getXML.onclick = function() {
  const xhr = new XMLHttpRequest();
  xhr.open('GET', '/4.xml');
  xhr.onreadystatechange = () =>{
    if (xhr.readyState === 4 && xhr.status === 200) {
      const xml = xhr.responseXML;
      const text = xml.getElementsByTagName('warning')[0].textContent;
      console.log(text.trim());
    }
  }
  xhr.send();
}

getJSON.onclick = function() {
  const xhr = new XMLHttpRequest();
  xhr.open('GET', '/5.json');
  xhr.onreadystatechange = () =>{
    if (xhr.readyState === 4 && xhr.status === 200) {
      const json = JSON.parse(xhr.responseText);
      console.log(json);
    }
  }
  xhr.send();
}

