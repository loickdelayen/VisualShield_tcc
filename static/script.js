document.addEventListener('DOMContentLoaded', function () {
    // Função para atualizar o histórico de alertas
    function updateAlerts() {
        fetch('/get_alerts')
            .then(response => response.json())
            .then(data => {
                const alertList = document.getElementById('alert_list');
                const fragment = document.createDocumentFragment(); // Evita reflow na DOM
    
                data.forEach(log => {
                    const listItem = document.createElement('li');
                    listItem.textContent = `${log.data_hora} - Erro: ${log.erro} - EPI Faltando: ${log.epi_faltando}`;
                    fragment.appendChild(listItem);
                });
    
                alertList.innerHTML = ''; // Limpa de uma vez só
                alertList.appendChild(fragment);
            })
            .catch(error => console.error('Erro ao buscar alertas:', error));
    }
    

    // Função para atualizar o gráfico de alertas
    let alertChart = null; // Variável global para armazenar o gráfico

function updateChart(periodo) {
    fetch('/get_logs')
        .then(response => response.json())
        .then(data => {
            const labels = data.map(item => periodo === 'Mensal' ? `Mês ${item[1]}` : `Semana ${item[1]}`);
            const values = data.map(item => item[0]);

            const ctx = document.getElementById('alertChart').getContext('2d');

            // Se já existir um gráfico, destrói antes de criar outro
            if (alertChart) {
                alertChart.destroy();
            }

            alertChart = new Chart(ctx, {
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

    // Função para verificar se a câmera está funcionando
    function checkCameraStatus() {
        const cameraFeed = document.getElementById('camera_feed');
        const cameraMessage = document.getElementById('camera-message');

        // Tenta acessar a câmera, se não conseguir, exibe a mensagem de erro
        if (!cameraFeed.complete || cameraFeed.naturalWidth === 0) {
            cameraMessage.style.display = 'block';  // Exibe a mensagem de erro
        } else {
            cameraMessage.style.display = 'none';   // Esconde a mensagem de erro
        }
    }

    // Inicializa a página
    updateAlerts();
    updateChart('Mensal');
    checkCameraStatus(); // Verifica o status da câmera

    // Se a câmera estiver funcionando, ele tentará novamente a cada 2 segundos
    setInterval(checkCameraStatus, 2000);
});


