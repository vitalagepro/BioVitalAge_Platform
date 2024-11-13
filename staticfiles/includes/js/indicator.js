const bars = document.querySelectorAll(".indicator-content-container");

bars.forEach(barraContainer => {
    let negativeRange = barraContainer.querySelector('.negativeTesto').textContent;
    let positiveRange = barraContainer.querySelector('.positiveTesto').textContent;
    let barra = barraContainer.querySelector('.barra-pointer');

    let valoreBarra = barra.getAttribute('data-value');
    let NegativeCheckedRange, PositiveCheckedRange, min;


    if (negativeRange.includes('-')) {
        let [rangeNegativeOne, rangeNegativeTwo] = negativeRange.split('-').map(part => part.trim());
        NegativeCheckedRange = Math.max(parseFloat(rangeNegativeOne), parseFloat(rangeNegativeTwo));
    } else {
        NegativeCheckedRange = parseFloat(negativeRange.split(" ")[0]);
    }


    if (positiveRange.includes('-')) {
        let [rangePositiveOne, rangePositiveTwo] = positiveRange.split('-').map(part => part.trim());
        PositiveCheckedRange = Math.min(parseFloat(rangePositiveOne), parseFloat(rangePositiveTwo));
        min = rangePositiveTwo;

    } else {
        PositiveCheckedRange = parseFloat(positiveRange.split(" ")[0]);
    }


    if (parseFloat(valoreBarra) >= NegativeCheckedRange) {
        barra.classList.add('negative');
        barra.style.width = "5%";
    } else {


        if(valoreBarra < PositiveCheckedRange){
            barra.classList.add('negative');
            barra.style.width = "100%";
        }
        else{
            const percentuale = ((NegativeCheckedRange - valoreBarra) / (NegativeCheckedRange - PositiveCheckedRange)) * 100;
            barra.classList.add('positive');
            barra.style.width = `${Math.round(percentuale)}%`;
        }
        
    }
});

