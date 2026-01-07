// static/script.js

// 1. Define real image URLs for each flower type
const flowerImages = {
    'Setosa': 'https://upload.wikimedia.org/wikipedia/commons/5/56/Kosaciec_szczecinkowaty_Iris_setosa.jpg',
    'Versicolor': 'https://upload.wikimedia.org/wikipedia/commons/4/41/Iris_versicolor_3.jpg',
    'Virginica': 'https://upload.wikimedia.org/wikipedia/commons/9/9f/Iris_virginica.jpg'
};

document.getElementById('predictionForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const btn = document.getElementById('submitBtn');
    const btnText = document.getElementById('btnText');
    const loader = document.getElementById('btnLoader');
    const resultCard = document.getElementById('result-card');
    const flowerImg = document.getElementById('flower-img');
    const predText = document.getElementById('prediction-text');
    
    // UI Loading State
    btn.disabled = true;
    btnText.style.display = 'none';
    loader.style.display = 'block';
    
    // Hide result while loading
    resultCard.classList.remove('show-result');
    resultCard.style.display = 'none';

    const formData = new FormData(this);
    
    try {
        // Artificial delay for effect
        await new Promise(r => setTimeout(r, 600));

        // Send to Flask
        const response = await fetch('/predict', {
            method: 'POST',
            body: formData
        });
        
        const data = await response.json();
        
        if(data.error) {
            throw new Error(data.error);
        }

        // --- UPDATE THE UI ---
        
        // 1. Set the text
        predText.textContent = data.class;
        
        // 2. Set the Real Image
        flowerImg.src = flowerImages[data.class];
        
        // 3. Reset classes and Show Result
        resultCard.className = ''; 
        resultCard.classList.add(data.class); 
        resultCard.classList.add('show-result'); 
        resultCard.style.display = 'block';

    } catch (error) {
        console.error('Error:', error);
        alert('Error: ' + error.message);
    } finally {
        // Reset Button
        btn.disabled = false;
        btnText.style.display = 'block';
        loader.style.display = 'none';
    }
});