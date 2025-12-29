/*
1 meter = 3.281 feet
1 liter = 0.264 gallon
1 kilogram = 2.204 pound
*/

let convbutton = document.getElementById("convbutton")

convbutton.addEventListener("click", () => {
      
    let inputnumber = document.getElementById("inputnumber").value;
    let meter = document.getElementById("meter");
    let meterconversion = inputnumber * 3.281
    let feetconversion = inputnumber / 3.281

    meter.textContent = `${inputnumber} meters = ${meterconversion.toFixed(1)} feet | ${inputnumber} feet = ${feetconversion.toFixed(1)} meters`
    /* ---------------------------------------------------------- */
    
    let liters = document.getElementById("liters");
    let litersconversion = inputnumber * 0.264
    let gallonsconversion = inputnumber / 0.264

    liters.textContent = `${inputnumber} liters = ${litersconversion.toFixed(1)} gallons | ${inputnumber} gallons = ${gallonsconversion.toFixed(1)} liters`
    
     /* ---------------------------------------------------------- */
     
    let kilo = document.getElementById("kilo");
    let kiloconversion = inputnumber * 2.204
    let poundsconversion = inputnumber / 2.204

    kilo.textContent = `${inputnumber} kilos = ${kiloconversion.toFixed(1)} pounds | ${inputnumber} pounds = ${poundsconversion.toFixed(1)} kilos`
})



  
    



