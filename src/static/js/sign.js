function changeSign() {
    var sup = document.getElementById('sign-up');
    var sin = document.getElementById('sign-in');
    if (sup.classList.contains('hidden')) {
        sup.classList.remove('hidden');
        sup.classList.add('shown');
        sin.classList.remove('shown');
        sin.classList.add('hidden');
    } else {
        sup.classList.remove('shown');
        sup.classList.add('hidden');
        sin.classList.remove('hidden');
        sin.classList.add('shown');
    }
}