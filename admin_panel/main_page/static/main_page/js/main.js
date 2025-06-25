const ctx = document.getElementById('salesChart').getContext('2d');
  const salesChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: ['5k', '10k', '15k', '20k', '25k', '30k', '35k', '40k', '45k', '50k', '55k', '60k'],
      datasets: [{
        label: 'Sales',
        data: [20, 45, 55, 85, 40, 50, 25, 45, 80, 65, 55, 60],
        fill: true,
        backgroundColor: 'rgba(47, 128, 237, 0.15)',
        borderColor: '#2f80ed',
        tension: 0.3,
        pointRadius: 5,
        pointHoverRadius: 7,
        pointBackgroundColor: '#2f80ed'
      }]
        },
        options: {
          responsive: true,
          plugins: {
            tooltip: {
              enabled: true,
              callbacks: {
                label: ctx => `Sales: ${ctx.parsed.y * 450}` // пример значения
              }
            },
            legend: {
              display: false
            }
          },
          scales: {
            y: {
              min: 0,
              max: 100,
              ticks: {
                stepSize: 20,
                callback: val => val + '%'
              },
              grid: {
                color: '#eee'
              }
            },
            x: {
              grid: {
                color: '#eee'
              }
            }
          }
        }
      });