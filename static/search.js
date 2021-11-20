$(document).ready(function(){
    let searchButton = document.getElementById('search_text');

    searchButton.addEventListener('keyup', search);

    function search(){
        const allElements = document.querySelectorAll('.search_item');
        allElements.forEach(function(elem) {
            elem.classList.add('hide');
        });
        const searchTerm = this.value.toUpperCase();
        console.log(searchTerm);
        let searchSelector = 'div[class*="' + searchTerm +'"]';
        if ((searchTerm=='') || (searchTerm==' ')){
            searchSelector = 'div[class*="search_item"]';
        }
       
        const matchedElements = document.querySelectorAll(searchSelector);
        matchedElements.forEach(function(elem) {
            elem.classList.remove('hide');
        });
    }

  });