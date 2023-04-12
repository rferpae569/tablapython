import "https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js";

function dibuja(data) {
    let a="";
    Object.values(data).forEach(value => {
         a+=`<li>${value.name}  ${value.age}  ${value.isEmployed}</li>`;
    });
    document.querySelector("#respuesta2").innerHTML=`<ul>${a}</ul>`;
    document.querySelector("div#respuesta").innerHTML=`<p>${JSON.stringify(data)}</p>`;
    
}
    document.querySelector('#ver').addEventListener('click',
    evt => {  
        evt.preventDefault();
        fetch('/datos')
            .then(response => {
                // network failure, request prevented
                if (response.status >= 200 && response.status < 300) {
                    return Promise.resolve(response);
                }
        
        
                return Promise.reject(new Error(response.statusText));
            })
            .then(response => response.json())
            .then(result => {
                dibuja(result);
            })
            .catch(error => {
                // common error
                console.error(error);
                return null;
            });
    });