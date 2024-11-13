const indicatorContainers = document.querySelector('.indicator-content-container')
const containerRangePositive = indicatorContainers.querySelector('.positiveTesto')
const rangePositiveIndicator = containerRangePositive.querySelectorAll('p')

const indicator = indicatorContainers.querySelector('.indicatore')

let valoreEsame = indicator.getAttribute('data-value')
let minPositive = rangePositiveIndicator[0].textContent
let maxPositive = rangePositiveIndicator[1].textContent


if(parseFloat(valoreEsame) <= parseFloat(minPositive) && parseFloat(valoreEsame) >= parseFloat(maxPositive)){
    
    if(parseFloat(valoreEsame) == parseFloat(minPositive)){
        indicator.style.left = "28%";
    }
    else if(parseFloat(valoreEsame) == parseFloat(maxPositive)){
        indicator.style.left = "58%";
    }
    else{
        const percentuale = ((minPositive - valoreEsame) / (minPositive - maxPositive)) * 40;
        let fixedPercentuale = percentuale + 26;
        indicator.style.left = `${Math.round(fixedPercentuale)}%`;
    }
}else{
    console.log("FinireDomani")
}
