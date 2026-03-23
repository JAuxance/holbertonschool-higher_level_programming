const character = document.querySelector('#character');
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
fetch(url)
  .then(Response => Response.json())
  .then(data => {
    character.textContent = data.name;
  });
