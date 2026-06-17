
const slides=[...document.querySelectorAll('.slide')],dots=[...document.querySelectorAll('.dot')];let i=0;
function show(n){slides.forEach((s,k)=>s.classList.toggle('active',k===n));dots.forEach((d,k)=>d.classList.toggle('active',k===n));i=n}
if(slides.length){setInterval(()=>show((i+1)%slides.length),4600);dots.forEach((d,k)=>d.onclick=()=>show(k));}

document.querySelectorAll('.lang-switcher').forEach((switcher) => {
  const button = switcher.querySelector('button');
  const dropdown = switcher.querySelector('.lang-dropdown');
  if (!button || !dropdown) return;

  button.setAttribute('type', 'button');
  button.setAttribute('aria-haspopup', 'true');
  button.setAttribute('aria-expanded', 'false');

  button.addEventListener('click', (event) => {
    event.preventDefault();
    event.stopPropagation();
    const open = dropdown.style.display === 'block';
    dropdown.style.display = open ? 'none' : 'block';
    button.setAttribute('aria-expanded', String(!open));
  });

  dropdown.addEventListener('click', (event) => {
    event.stopPropagation();
  });
});

document.addEventListener('click', () => {
  document.querySelectorAll('.lang-switcher .lang-dropdown').forEach((dropdown) => {
    dropdown.style.display = 'none';
    const button = dropdown.closest('.lang-switcher')?.querySelector('button');
    button?.setAttribute('aria-expanded', 'false');
  });
});

