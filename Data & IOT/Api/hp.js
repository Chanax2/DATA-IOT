let cards = document.querySelectorAll(".cards")
console.log(cards);

function fetchCharacters(){
    return fetch('https://hp-api.lainocs.fr/characters/')
    .then((response) => response.json())
}


async function displayCharacters() {
    const data = await fetchCharacters();
    
    for (let i = 0; i < cards.length ; i++){
        console.log("ligne 13" , data , cards[i]);
        cards[i].innerHTML += `
        <a href="single-hp.html?slug=${data[i].slug}">
        <div class="character">
        <h2>${data[i].name}</h2>
        </div></a>
        `
        console.log(`url(${data[i].image})`);
        cards[i].style.backgroundImage =`url(${data[i].image})`
    };
    console.log(data);

}



displayCharacters() 

