// Cargar ejemplo seleccionado
document.getElementById('exampleSelector').addEventListener('change', function(e) {
    const exampleName = e.target.value;
    if (exampleName) {
        loadExample(exampleName);
    }
});

// Cargar ejemplo desde el servidor
async function loadExample(exampleName) {
    try {
        const response = await fetch(`/api/examples/${exampleName}`);
        const data = await response.json();
        
        if (data.success) {
            document.getElementById('codeEditor').value = data.code;
        } else {
            alert('Error cargando ejemplo: ' + data.error);
        }
    } catch (error) {
        alert('Error cargando ejemplo: ' + error.message);
    }
}

// Analizar código
async function analyzeCode() {
    const code = document.getElementById('codeEditor').value;
    
    if (!code.trim()) {
        alert('Por favor, ingresa algún código para analizar.');
        return;
    }
    
    try {
        const response = await fetch('/api/analyze', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ code: code })
        });
        
        const result = await response.json();
        displayResults(result);
        
    } catch (error) {
        alert('Error analizando código: ' + error.message);
    }
}

// Mostrar resultados
function displayResults(result) {
    const container = document.getElementById('resultsContainer');
    
    // Resultado general
    if (result.overall_success) {
        container.innerHTML = `<div class="success">✅ Análisis completado exitosamente</div>`;
    } else {
        container.innerHTML = `<div class="error">❌ Se encontraron errores en el análisis</div>`;
    }
    
    // Mostrar tokens
    displayTokens(result.lexical_analysis.tokens);
    
    // Mostrar tabla de símbolos
    displaySymbolTable(result.symbol_table);
    
    // Mostrar errores
    displayErrors(result);
    
    // Abrir pestaña de tokens por defecto
    openTab(event, 'Tokens');
}

// Mostrar tokens
function displayTokens(tokens) {
    const tokensList = document.getElementById('tokensList');
    tokensList.innerHTML = '';
    
    tokens.forEach(token => {
        const tokenElement = document.createElement('div');
        tokenElement.className = 'token-item';
        tokenElement.innerHTML = `
            <strong>Token:</strong> ${token.token} 
            <strong>Valor:</strong> ${token.value} 
            <strong>Tipo:</strong> ${token.type}
        `;
        tokensList.appendChild(tokenElement);
    });
}

// Mostrar tabla de símbolos
function displaySymbolTable(symbolTable) {
    const tbody = document.querySelector('#symbolTable tbody');
    tbody.innerHTML = '';
    
    symbolTable.forEach(symbol => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${symbol.lexeme}</td>
            <td>${symbol.token}</td>
            <td>${symbol.type}</td>
            <td>${symbol.value}</td>
            <td>${symbol.state}</td>
        `;
        tbody.appendChild(row);
    });
}

// Mostrar errores
function displayErrors(result) {
    const errorsList = document.getElementById('errorsList');
    errorsList.innerHTML = '';
    
    // Errores léxicos
    if (result.lexical_analysis.errors && result.lexical_analysis.errors.length > 0) {
        result.lexical_analysis.errors.forEach(error => {
            const errorElement = document.createElement('div');
            errorElement.className = 'error-item';
            errorElement.textContent = `Léxico: ${error}`;
            errorsList.appendChild(errorElement);
        });
    }
    
    // Errores sintácticos
    if (result.syntax_analysis.errors && result.syntax_analysis.errors.length > 0) {
        result.syntax_analysis.errors.forEach(error => {
            const errorElement = document.createElement('div');
            errorElement.className = 'error-item';
            errorElement.textContent = `Sintáctico: ${error}`;
            errorsList.appendChild(errorElement);
        });
    }
    
    if (errorsList.children.length === 0) {
        errorsList.innerHTML = '<div class="success">No se encontraron errores</div>';
    }
}

// Limpiar editor
function clearEditor() {
    document.getElementById('codeEditor').value = '';
    document.getElementById('resultsContainer').innerHTML = '';
    document.getElementById('tokensList').innerHTML = '';
    document.querySelector('#symbolTable tbody').innerHTML = '';
    document.getElementById('errorsList').innerHTML = '';
}

// Sistema de pestañas
function openTab(evt, tabName) {
    const tabcontent = document.getElementsByClassName("tabcontent");
    for (let i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    
    const tablinks = document.getElementsByClassName("tablinks");
    for (let i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";
}

// Abrir la pestaña de Tokens por defecto
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('Tokens').style.display = 'block';
    if (document.querySelector('.tablinks')) {
        document.querySelector('.tablinks').className += ' active';
    }
});