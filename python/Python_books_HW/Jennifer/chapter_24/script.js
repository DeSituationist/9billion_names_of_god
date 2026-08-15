/*
let $new_p = document.createElement( 'p' );
document.appendChild( $new_p );
document.insertBefore( $new_p, document.body.firstChild );

let $second_h1 = document.querySelector('h1:nth-child(2)');
$second_h1.parentNode.removeChild( $second_h1 );
*/
let $body = document.body;
let $p = document.createElement( 'p' );
$p.innerText = 'I  made this with JS';
$body.appendChild( $p );

let $ul = document.createElement( 'ul' );
let $li = document.createElement( 'li' );
$li.innerText = 'I made this with JS too.';
$ul.appendChild( $li );
$body.insertBefore( $ul, $p );

let new_text = document.createTextNode( 'Hi there!' );
new_text.nodeValue += ' ';
$p.insertBefore(new_text, $p.firstChild);

let $toggle = document.createElement( 'button' );
$toggle.innerText = 'Theme Toggle';
document.body.appendChild( $toggle );

$body.classList.add('test');
$body.classList.contains('test');
$body.classList.remove('test');
$body.classList.toggle('test'); // It adds the class name if it isn’t already applied to the element, or removes it if it is already applied

let $button = document.createElement('button');
$button.innerText = 'Click Me';
document.body.appendChild($button);
$button.onclick = function(){
    console.log( 'Ouch!' );
}
function hi(){
    console.log( 'Hi' );
}
function bye(){
    console.log( 'Bye' );
}
$button.onfocus = hi;
$button.onblur = bye;
$button.addEventListener('click', function(){
    console.log( 'Yey' );
});

let $h2 = document.querySelector('h2');
$h2.classList.add('light-theme');

$toggle = document.createElement('button');
$toggle.type = 'button';
$toggle.innerText = 'Light';
$toggle.classList.add('toggle');
$toggle.classList.add('toggle-light')
$toggle.onclick = toggleTheme;
document.body.appendChild($toggle);

function toggleTheme() {
    const isLight = $h2.classList.contains('light-theme');
    const newTheme = isLight ? 'dark-theme' : 'light-theme';

    const themeName = newTheme.split('-')[0]; 
    $h2.classList.remove('light-theme', 'dark-theme');
    $h2.classList.add(newTheme);

    $toggle.classList.remove('toggle-light', 'toggle-dark');
    $toggle.classList.add('toggle-' + themeName);

    $toggle.innerText = themeName.charAt(0).toUpperCase() + themeName.slice(1);
}
