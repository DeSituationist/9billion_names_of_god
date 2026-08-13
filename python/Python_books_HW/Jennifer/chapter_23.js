/*
function doSomething(parameter){

}

const doSomething = function(){

}
*/
function countWords( the_text ){
    return the_text.split(' ').length;
}

function wordsToMinutes( words ){
    return words / 250;
}

let $p = document.querySelector('p#main');

function insertReadingTime( $p ){
    if (!$p.innerText){
        return 'no text found';
    }
    let words = countWords( $p.innerText);
    let duration = wordsToMinutes( words );
    $p.innerText += " (Reading time: " + duration + " minutes)";
}

insertReadingTime( $p );

/*
if ( test criteria && || ! ){

} else {

}
*/
let mailing_list = [
    "email@domain-1.tld", "email@domain-2.tld",
    "email@domain-3.tld", "email@domain-4.tld",
    "email@domain-5.tld", "email@domain-6.tld",
];
for ( let i = 0; i < mailing_list.length; i++){
    sendEmail( mailing_list[ i ] );
}

let $paragraphs = document.querySelectorAll("p");

let count = $paragraphs.length;

for (let i = 0; i < count; i++){
    insertReadingTime($paragraphs[i]);
}

let $divs = document.querySelectorAll("div");

function compare_divs_and_ps($divs, $ps){
    let $div_count = $divs.length;
    let $ps_count = $ps.length;
    if ($ps_count > $div_count) {
        return 'Page has more paragraphs';
    } else {
        return 'Page has more divs';
    }
}