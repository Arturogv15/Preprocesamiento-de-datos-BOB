// Main JavaScript for Data Preprocessing Platform

// Global variables
let currentDataset = null;
let processingHistory = [];

// Initialize on page load
$(document).ready(function() {
    console.log('Data Preprocessing Platform loaded');
    
    // Initialize DataTables if present
    if ($.fn.DataTable) {
        $('.data-table').DataTable({
            pageLength: 25,
            responsive: true,
            language: {
                url: '//cdn.datatables.net/plug-ins/1.13.5/i18n/es-ES.json'
            }
        });
    }
    
    // Initialize tooltips
    if (typeof bootstrap !== 'undefined') {
        var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
        tooltipTriggerList.map(function (tooltipTriggerEl) {
            return new bootstrap.Tooltip(tooltipTriggerEl);
        });
    }
    
    // Auto-hide alerts after 5 seconds
    setTimeout(function() {
        $('.alert').fadeOut('slow');
    }, 5000);
});

// Utility Functions
function showLoading(message = 'Procesando...') {
    const spinner = `
        <div class="spinner-overlay" id="loadingSpinner">
            <div class="text-center">
                <div class="spinner-border text-light" role="status">
                    <span class="visually-hidden">Loading...</span>
                </div>
                <p class="text-light mt-3">${message}</p>
            </div>
        </div>
    `;
    $('body').append(spinner);
}

function hideLoading() {
    $('#loadingSpinner').remove();
}

function showAlert(message, type = 'info') {
    const alert = `
        <div class="alert alert-${type} alert-dismissible fade show" role="alert">
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        </div>
    `;
    $('.container').first().prepend(alert);
    
    // Auto-hide after 5 seconds
    setTimeout(function() {
        $('.alert').fadeOut('slow', function() {
            $(this).remove();
        });
    }, 5000);
}

// API Helper Functions
async function apiCall(endpoint, method = 'GET', data = null) {
    const options = {
        method: method,
        headers: {
            'Content-Type': 'application/json'
        }
    };
    
    if (data && method !== 'GET') {
        options.body = JSON.stringify(data);
    }
    
    try {
        const response = await fetch(endpoint, options);
        const result = await response.json();
        
        if (!result.success) {
            throw new Error(result.error || 'Unknown error occurred');
        }
        
        return result;
    } catch (error) {
        console.error('API Error:', error);
        showAlert(error.message, 'danger');
        throw error;
    }
}

// Dataset Functions
async function uploadDataset(file) {
    showLoading('Subiendo dataset...');
    
    const formData = new FormData();
    formData.append('file', file);
    
    try {
        const response = await fetch('/api/data/upload', {
            method: 'POST',
            body: formData
        });
        
        const result = await response.json();
        hideLoading();
        
        if (result.success) {
            showAlert('Dataset subido exitosamente', 'success');
            currentDataset = result.dataset_id;
            return result;
        } else {
            throw new Error(result.error);
        }
    } catch (error) {
        hideLoading();
        showAlert('Error al subir dataset: ' + error.message, 'danger');
        throw error;
    }
}

async function loadDatasetPreview(datasetId) {
    showLoading('Cargando preview...');
    
    try {
        const result = await apiCall(`/api/data/preview/${datasetId}`);
        hideLoading();
        return result;
    } catch (error) {
        hideLoading();
        throw error;
    }
}

// Data Processing Functions
async function applyDataCleaning(operation, params) {
    showLoading('Aplicando limpieza...');
    
    try {
        const result = await apiCall('/api/data/clean', 'POST', {
            dataset_id: currentDataset,
            operation: operation,
            params: params
        });
        
        hideLoading();
        showAlert('Limpieza aplicada exitosamente', 'success');
        
        // Add to history
        processingHistory.push({
            type: 'clean',
            operation: operation,
            params: params,
            timestamp: new Date()
        });
        
        return result;
    } catch (error) {
        hideLoading();
        throw error;
    }
}

async function applyDataTransformation(operation, params) {
    showLoading('Aplicando transformación...');
    
    try {
        const result = await apiCall('/api/data/transform', 'POST', {
            dataset_id: currentDataset,
            operation: operation,
            params: params
        });
        
        hideLoading();
        showAlert('Transformación aplicada exitosamente', 'success');
        
        // Add to history
        processingHistory.push({
            type: 'transform',
            operation: operation,
            params: params,
            timestamp: new Date()
        });
        
        return result;
    } catch (error) {
        hideLoading();
        throw error;
    }
}

// Visualization Functions
async function generateVisualization(vizType, params) {
    showLoading('Generando visualización...');
    
    try {
        const result = await apiCall('/api/viz/generate', 'POST', {
            dataset_id: currentDataset,
            type: vizType,
            params: params
        });
        
        hideLoading();
        return result;
    } catch (error) {
        hideLoading();
        throw error;
    }
}

function renderPlotly(plotData, containerId) {
    const plotDiv = document.getElementById(containerId);
    if (!plotDiv) {
        console.error('Plot container not found:', containerId);
        return;
    }
    
    try {
        const data = JSON.parse(plotData);
        Plotly.newPlot(containerId, data.data, data.layout, {responsive: true});
    } catch (error) {
        console.error('Error rendering plot:', error);
        showAlert('Error al renderizar visualización', 'danger');
    }
}

// Progress Tracking
async function updateProgress(moduleName, moduleType, completed = false, timeSpent = 0) {
    try {
        await apiCall('/api/progress/update', 'POST', {
            module_name: moduleName,
            module_type: moduleType,
            completed: completed,
            time_spent: timeSpent
        });
    } catch (error) {
        console.error('Error updating progress:', error);
    }
}

// Quiz Functions
let quizStartTime = null;
let quizAnswers = {};

function startQuiz(quizId) {
    quizStartTime = new Date();
    quizAnswers = {};
    console.log('Quiz started:', quizId);
}

function selectAnswer(questionId, answer) {
    quizAnswers[questionId] = answer;
    
    // Visual feedback
    $(`.quiz-option[data-question="${questionId}"]`).removeClass('selected');
    $(`.quiz-option[data-question="${questionId}"][data-answer="${answer}"]`).addClass('selected');
}

async function submitQuiz(quizId) {
    if (Object.keys(quizAnswers).length === 0) {
        showAlert('Por favor responde al menos una pregunta', 'warning');
        return;
    }
    
    const timeTaken = Math.floor((new Date() - quizStartTime) / 1000);
    
    showLoading('Enviando respuestas...');
    
    try {
        const result = await apiCall('/api/quiz/submit', 'POST', {
            quiz_id: quizId,
            answers: quizAnswers,
            time_taken: timeTaken
        });
        
        hideLoading();
        
        // Show results
        showQuizResults(result);
        
    } catch (error) {
        hideLoading();
    }
}

function showQuizResults(result) {
    const percentage = result.percentage.toFixed(1);
    const passed = percentage >= 70;
    
    const resultHtml = `
        <div class="alert alert-${passed ? 'success' : 'warning'} text-center">
            <h4>${passed ? '¡Felicidades!' : 'Sigue practicando'}</h4>
            <p class="mb-0">Obtuviste ${result.score} de ${result.total} respuestas correctas (${percentage}%)</p>
        </div>
    `;
    
    $('#quizResults').html(resultHtml);
}

// Pipeline Functions
async function savePipeline(name, description, datasetName) {
    if (processingHistory.length === 0) {
        showAlert('No hay pasos para guardar', 'warning');
        return;
    }
    
    showLoading('Guardando pipeline...');
    
    try {
        const result = await apiCall('/api/pipeline/save', 'POST', {
            name: name,
            description: description,
            dataset_name: datasetName,
            steps: processingHistory
        });
        
        hideLoading();
        showAlert('Pipeline guardado exitosamente', 'success');
        return result;
        
    } catch (error) {
        hideLoading();
    }
}

function clearProcessingHistory() {
    processingHistory = [];
    showAlert('Historial limpiado', 'info');
}

// Table Rendering
function renderDataTable(data, containerId) {
    const container = document.getElementById(containerId);
    if (!container) return;
    
    if (data.length === 0) {
        container.innerHTML = '<p class="text-muted">No hay datos para mostrar</p>';
        return;
    }
    
    // Get column names
    const columns = Object.keys(data[0]);
    
    // Create table HTML
    let html = '<div class="table-responsive"><table class="table table-striped table-hover">';
    
    // Header
    html += '<thead><tr>';
    columns.forEach(col => {
        html += `<th>${col}</th>`;
    });
    html += '</tr></thead>';
    
    // Body
    html += '<tbody>';
    data.forEach(row => {
        html += '<tr>';
        columns.forEach(col => {
            html += `<td>${row[col] !== null ? row[col] : '<span class="text-muted">null</span>'}</td>`;
        });
        html += '</tr>';
    });
    html += '</tbody></table></div>';
    
    container.innerHTML = html;
}

// Statistics Display
function displayStatistics(stats, containerId) {
    const container = document.getElementById(containerId);
    if (!container) return;
    
    let html = '<div class="row">';
    
    // Basic info
    html += `
        <div class="col-md-3 mb-3">
            <div class="card">
                <div class="card-body text-center">
                    <h6 class="text-muted">Filas</h6>
                    <h3>${stats.shape[0]}</h3>
                </div>
            </div>
        </div>
        <div class="col-md-3 mb-3">
            <div class="card">
                <div class="card-body text-center">
                    <h6 class="text-muted">Columnas</h6>
                    <h3>${stats.shape[1]}</h3>
                </div>
            </div>
        </div>
        <div class="col-md-3 mb-3">
            <div class="card">
                <div class="card-body text-center">
                    <h6 class="text-muted">Duplicados</h6>
                    <h3>${stats.duplicates}</h3>
                </div>
            </div>
        </div>
        <div class="col-md-3 mb-3">
            <div class="card">
                <div class="card-body text-center">
                    <h6 class="text-muted">Memoria</h6>
                    <h3>${stats.memory_usage}</h3>
                </div>
            </div>
        </div>
    `;
    
    html += '</div>';
    container.innerHTML = html;
}

// Export functions to global scope
window.DataPreprocessing = {
    uploadDataset,
    loadDatasetPreview,
    applyDataCleaning,
    applyDataTransformation,
    generateVisualization,
    renderPlotly,
    updateProgress,
    startQuiz,
    selectAnswer,
    submitQuiz,
    savePipeline,
    clearProcessingHistory,
    renderDataTable,
    displayStatistics,
    showAlert,
    showLoading,
    hideLoading
};

// Made with Bob
