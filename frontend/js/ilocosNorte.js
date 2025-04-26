async function fetchIlocosNorteLanguage() {
    const provinceId = 'P001';
    const response = await fetch(`http://127.0.0.1:8000/phrases/comparison/${provinceId}`);
    const data = await response.json();
  
    const tableBody = document.querySelector('#phraseTable tbody');
    tableBody.innerHTML = '';
  
    data.forEach(row => {
      const tr = document.createElement('tr');
  
      const phraseCell = document.createElement('td');
      phraseCell.textContent = row.phrase_id;
      tr.appendChild(phraseCell);
  
      const translationsCell = document.createElement('td');
      translationsCell.textContent = Object.entries(row.translations)
        .map(([lang, translation]) => `${lang}: ${translation}`)
        .join(', ');
      tr.appendChild(translationsCell);
  
      tableBody.appendChild(tr);
    });
  }
  
  window.onload = fetchIlocosNorteLanguage;
  