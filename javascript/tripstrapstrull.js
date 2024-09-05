let xkord = true;

let m2ngulaud = document.getElementById('tabel');

for (let i=0; i<3; i++) {
  let rida = document.createElement('tr');
  for (let j=0; j<3; j++) {
    let lahter = document.createElement('td');
    lahter.innerHTML = ' ';
    lahter.onclick = function() {
      if(xkord) {
        lahter.classList.add('xtegi');
        lahter.innerHTML = 'X';
      } else {
        lahter.classList.add('otegi');
        lahter.innerHTML = 'O';
      }
      xkord = !xkord;
    }

    rida.appendChild(lahter);
  }
  m2ngulaud.appendChild(rida);
}