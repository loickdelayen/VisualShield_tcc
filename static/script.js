document.addEventListener('DOMContentLoaded', function () {
    // Função para atualizar o histórico de alertas
    function updateAlerts() {
        fetch('/get_alerts')
            .then(response => response.json())
            .then(data => {
                const alertList = document.getElementById('alert_list');
                alertList.innerHTML = ''; // Limpa a lista de alertas
                data.forEach(log => {
                    const listItem = document.createElement('li');
                    listItem.textContent = `${log.data_hora} - Erro: ${log.erro} - EPI Faltando: ${log.epi_faltando}`;
                    alertList.appendChild(listItem);
                });
            })
            .catch(error => console.error('Erro ao buscar alertas:', error));
    }

    // Função para atualizar o gráfico de alertas
    function updateChart(periodo) {
        fetch('/get_logs')
            .then(response => response.json())
            .then(data => {
                const labels = data.map(item => periodo === 'Mensal' ? `Mês ${item[1]}` : `Semana ${item[1]}`);
                const values = data.map(item => item[0]);

                const ctx = document.getElementById('alertChart').getContext('2d');
                new Chart(ctx, {
                    type: 'line',
                    data: {
                        labels: labels,
                        datasets: [{
                            label: 'Número de Alertas',
                            data: values,
                            borderColor: 'rgb(75, 192, 192)',
                            fill: false
                        }]
                    },
                    options: {
                        responsive: true,
                        scales: {
                            x: {
                                title: {
                                    display: true,
                                    text: periodo
                                }
                            },
                            y: {
                                title: {
                                    display: true,
                                    text: 'Número de Erros'
                                }
                            }
                        }
                    }
                });
            })
            .catch(error => console.error('Erro ao gerar gráfico:', error));
    }

    // Evento de mudança no select para alterar o período do gráfico
    document.getElementById('periodo').addEventListener('change', function () {
        const selectedPeriod = this.value;
        updateChart(selectedPeriod);
    });

    // Inicialização do dashboard
    updateAlerts();
    updateChart('Mensal');
});
