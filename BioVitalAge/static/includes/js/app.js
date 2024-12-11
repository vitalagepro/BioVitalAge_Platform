const userImg = document.getElementById("userImg");
const userModal = document.getElementById("userModal");
const userModalBtn = document.getElementById("nav-bar-user-modal-btn");

function showModal() {
  userModal.style.display = "block";
}

userImg.addEventListener("mouseover", showModal);

userModal.addEventListener("mouseout", () => {
  userModal.style.display = "none";
});

userModalBtn.addEventListener("mouseover", showModal);

// Access to :root style css
const rootStyles = getComputedStyle(document.documentElement);

// Access to color in the :root
const bgColorDark = rootStyles.getPropertyValue("--bg-color-dark").trim();
const bgColorLight = rootStyles.getPropertyValue("--bg-color-light").trim();
const titleColorDarkLighter = rootStyles
  .getPropertyValue("--title-color-dark-lighter")
  .trim();
const titleColorDark = rootStyles.getPropertyValue("--title-color-dark").trim();
const titleColorLight = rootStyles
  .getPropertyValue("--title-color-light")
  .trim();

const darkColor = rootStyles.getPropertyValue("--dark-color").trim();
const lighterTwoColor = rootStyles
  .getPropertyValue("--lighter-two-color")
  .trim();
const lighterOneColor = rootStyles
  .getPropertyValue("--lighter-one-color")
  .trim();
const lightColor = rootStyles.getPropertyValue("--light-color").trim();
const mindColor = rootStyles.getPropertyValue("--mind-color").trim();

/* Fill the clock based in % function */
// function updateKidneyClock(){
//     const kidneyClock = document.getElementById('kidneyClock');
//     const kidneyPercentage = document.getElementById('kidneyPercentage');

//     const percentage = 57;
//     const angle = (percentage / 100) * 360;

//     // kidneyClock.style.background = `conic-gradient(${darkColor} ${angle}deg, #e0e0e0 ${angle}deg)`;

//     kidneyPercentage.textContent = `${percentage}%`;
//     kidneyPercentage.style.color = darkColor;
// }
// function updateLipidClock(){
//     const lipidClock = document.getElementById('lipidClock');
//     const lipidPercentage = document.getElementById('lipidPercentage');

//     const percentage = 33;
//     const angle = (percentage / 100) * 360;

//     // lipidClock.style.background = `conic-gradient(${bgColorDark} ${angle}deg, #e0e0e0 ${angle}deg)`;

//     lipidPercentage.textContent = `${percentage}%`;
//     lipidPercentage.style.color = bgColorDark;
// }
// function updateLiverClock(){
//     const liverClock = document.getElementById('liverClock');
//     const liverPercentage = document.getElementById('liverPercentage');

//     const percentage = 73;
//     const angle = (percentage / 100) * 360;

//     liverClock.style.background = `conic-gradient(${lighterTwoColor} ${angle}deg, #e0e0e0 ${angle}deg)`;

//     liverPercentage.textContent = `${percentage}%`;
//     liverPercentage.style.color = lighterTwoColor;
// }
// function updateGlucoseClock(){
//     const glucoseClock = document.getElementById('glucoseClock');
//     const glucosePercentage = document.getElementById('glucosePercentage');

//     const percentage = 15;
//     const angle = (percentage / 100) * 360;

//     glucoseClock.style.background = `conic-gradient(${lightColor} ${angle}deg, #e0e0e0 ${angle}deg)`;

//     glucosePercentage.textContent = `${percentage}%`;
//     glucosePercentage.style.color = lightColor;
// }

// // updateKidneyClock()
// updateLipidClock()
// updateLiverClock()
// updateGlucoseClock()

/*  -----------------------------------------------------------------------------------------------
    Funzioni
--------------------------------------------------------------------------------------------------- */
function goToPatientsPage() {
  alert("Vai alla pagina di tutti i pazienti");
}

function goToRefertiPage() {
  alert("Vai alla pagina dei referti dei pazienti");
}

// Grafici
const weeklyCtx = document.getElementById("weeklyPatientsChart");
new Chart(weeklyCtx, {
  type: "line",
  data: {
    labels: ["Lun", "Mar", "Mer", "Gio", "Ven", "Sab", "Dom"],
    datasets: [
      {
        label: "Pazienti Visitati",
        data: [5, 10, 8, 12, 15, 20, 5],
        borderColor: "#fff",
        backgroundColor: "rgba(255,255,255,0.3)",
        fill: true,
        tension: 0.3,
      },
    ],
  },
  options: {
    responsive: true,
    scales: {
      x: {
        ticks: { color: "#fff" },
        grid: { color: "rgba(255,255,255,0.2)" },
      },
      y: {
        ticks: { color: "#fff" },
        grid: { color: "rgba(255,255,255,0.2)" },
      },
    },
    plugins: {
      legend: { display: false },
    },
  },
});

const patientsCtx = document.getElementById("patientsChart");
new Chart(patientsCtx, {
  type: "bar",
  data: {
    labels: ["Gen", "Feb", "Mar", "Apr", "Mag", "Giu"],
    datasets: [
      {
        label: "Pazienti Inseriti",
        data: [30, 45, 60, 50, 70, 90],
        backgroundColor: "#3a255d",
        categoryPercentage: 0.8, // Riduce lo spazio tra le categorie
        barPercentage: 0.9, // Riduce lo spazio interno tra le barre
      },
    ],
  },
  options: {
    responsive: true,
    plugins: {
      legend: { display: false },
    },
    scales: {
      x: {
        ticks: {
          autoSkip: false, // Mostra tutte le etichette
        },
      },
      y: { 
        beginAtZero: true 
      },
    },
  },
});

const monthlyCtx = document.getElementById("monthlyPatientsChart");
const monthlyData = {
  labels: [
    "Gen",
    "Feb",
    "Mar",
    "Apr",
    "Mag",
    "Giu",
    "Lug",
    "Ago",
    "Set",
    "Ott",
    "Nov",
    "Dic",
  ],
  datasets: [
    {
      label: "Pazienti Mensili",
      data: [40, 60, 55, 70, 80, 90, 100, 85, 75, 95, 110, 120],
      backgroundColor: "#3a255d",
      borderColor: "#6a2dcc",
      borderWidth: 2,
      fill: true,
    },
  ],
};

let monthlyPatientsChart = new Chart(monthlyCtx, {
  type: "line",
  data: monthlyData,
  options: {
    responsive: true,
    interaction: {
      mode: "index",
      intersect: false,
    },
    plugins: {
      legend: { display: false },
    },
    scales: {
      y: { beginAtZero: true },
    },
    onHover: (event, chartElement) => {
      const tooltip = document.getElementById("monthlyTooltip");
      if (chartElement.length > 0) {
        const index = chartElement[0].index;
        const monthLabel = monthlyData.labels[index];
        const patientCount = monthlyData.datasets[0].data[index];
        const calcCount = Math.floor(patientCount * 0.6);

        tooltip.innerHTML = `
                    <strong>${monthLabel}</strong><br>
                    Pazienti: ${patientCount}<br>
                    Con calcolo età bio: ${calcCount}
                `;
        const canvasPos = monthlyCtx.getBoundingClientRect();
        tooltip.style.opacity = 1;
        tooltip.style.left = event.clientX - canvasPos.left + "px";
        tooltip.style.top = event.clientY - canvasPos.top + "px";
      } else {
        const tooltip = document.getElementById("monthlyTooltip");
        tooltip.style.opacity = 0;
      }
    },
  },
});
