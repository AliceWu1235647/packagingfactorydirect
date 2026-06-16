
let i=0;const slides=[...document.querySelectorAll('.slide')],dots=[...document.querySelectorAll('.dot')];function show(n){slides.forEach((s,k)=>s.classList.toggle('active',k===n));dots.forEach((d,k)=>d.classList.toggle('active',k===n));i=n}if(slides.length){setInterval(()=>show((i+1)%slides.length),4200);dots.forEach((d,k)=>d.onclick=()=>show(k));}
