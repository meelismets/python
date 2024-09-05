const soovid=[
  "Too kuusk tuppa",
  "Kaunista jõulupuud",
  "Otsi kuurist kelk väja",
  "Mine kelgutama",
  "Tee lumememme",
  "Laula jõululaule",
  "Küpseta piparkooke",
  "Kaunista piparkooke",
  "Lisa kuusele ehteid",
  "Joonista jõulukaarte",
  "Otsi uisud kapist välja",
  "Mine uisutama",
  "Saada jõulukaarte",
  "Koo üks paar jõulusokke",
  "Riputa lindudele pekki",
  "",
  "",
  "",
  "",
  "",
  "",
  "",
  "",
  "Oota jõuluvana",
  "Ava kingitusi, kui veel on midagi avada"
];

let kalender = document.getElementById('kalender');

let paev = 0;
for (let i=0; i<5; i++) {
  let rida = document.createElement('tr');
  for (let j=0; j<5; j++) {
    let lahter = document.createElement('td');
    lahter.onclick = function() {
      lahter.classList.add('avatud');
    }
    lahter.innerHTML = soovid[paev];
    rida.appendChild(lahter);
    paev++;
  }
  kalender.appendChild(rida);
}