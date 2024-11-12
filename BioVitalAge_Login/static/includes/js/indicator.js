const bars = document.querySelectorAll(".indicator-content-container");

negativeRange = bars[0].querySelector('.negativeTesto').textContent
positiveRange = bars[0].querySelector('.positiveTesto').textContent
barra = bars[0].querySelector('.barra-pointer')

valoreBarra = barra.getAttribute('data-value');
var NegativeCheckedRange;
var PositiveCheckedRange;

if (negativeRange.includes('-')) {

    var [rangeNegativeOne, rangeNegativeTwo] = negativeRange.split('-').map(part => part.trim());
    if (parseFloat(rangeNegativeOne) > parseFloat(rangeNegativeTwo)){
        NegativeCheckedRange = rangeNegativeOne
    }else{
        NegativeCheckedRange = rangeNegativeTwo;
    }
}
else{
    NegativeCheckedRange = negativeRange.split(" ")[0];
}

if (positiveRange.includes('-')) { 
    var [rangePositiveOne, rangePositiveTwo] = positiveRange.split('-').map(part => part.trim());
    if (parseFloat(rangePositiveOne) < parseFloat(rangePositiveTwo)){
        PositiveCheckedRange = rangePositiveOne
    }else{
        PositiveCheckedRange = rangePositiveTwo
    }
}
else{
    PositiveCheckedRange =  positiveRange.split(" ")[0];;
}


const percentuale = ((valoreBarra - negativeRange) / (positiveRange - negativeRange)) * 100;

console.log(percentuale); 







barraIndicator = bars[0].querySelector('.barra-pointer').textContent


