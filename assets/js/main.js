
const slides=[...document.querySelectorAll('.slide')],dots=[...document.querySelectorAll('.dot')];let i=0;
function show(n){slides.forEach((s,k)=>s.classList.toggle('active',k===n));dots.forEach((d,k)=>d.classList.toggle('active',k===n));i=n}
if(slides.length){setInterval(()=>show((i+1)%slides.length),4600);dots.forEach((d,k)=>d.onclick=()=>show(k));}
