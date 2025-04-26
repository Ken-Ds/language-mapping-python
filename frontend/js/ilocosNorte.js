async function fetchIlocosNorteLanguage() {
  const provinceId = 'P001';
  const response = await fetch(`http://127.0.0.1:8000/phrases/comparison/${provinceId}`);
  const data = await response.json();

  const table = document.getElementById('phraseTable');
  const thead = table.querySelector('thead');
  const tbody = table.querySelector('tbody');

  thead.innerHTML = '';
  tbody.innerHTML = '';

  // Step 1: Collect all unique languages
  const languagesSet = new Set();
  data.forEach(row => {
    Object.keys(row.translations).forEach(lang => languagesSet.add(lang));
  });

  const languages = Array.from(languagesSet).sort();

  // Step 2: Create header row
  const headerRow = document.createElement('tr');
  const englishHeader = document.createElement('th');
  englishHeader.textContent = 'English';
  headerRow.appendChild(englishHeader);

  languages.forEach(lang => {
    const th = document.createElement('th');
    th.textContent = lang;
    headerRow.appendChild(th);
  });

  thead.appendChild(headerRow);

  // Step 3: Group data by English phrase
  const groupedData = {};
  data.forEach(row => {
    const englishPhrase = row.english_translation || '';
    if (!groupedData[englishPhrase]) {
      groupedData[englishPhrase] = {};
    }
    Object.keys(row.translations).forEach(lang => {
      groupedData[englishPhrase][lang] = row.translations[lang];
    });
  });

  // Step 4: Create data rows
  Object.keys(groupedData).forEach(englishPhrase => {
    const tr = document.createElement('tr');

    // Add English phrase
    const englishCell = document.createElement('td');
    englishCell.textContent = englishPhrase;
    tr.appendChild(englishCell);

    // Add translations for each language
    languages.forEach(lang => {
      const td = document.createElement('td');
      td.textContent = groupedData[englishPhrase][lang] || ''; // Leave empty if no translation
      tr.appendChild(td);
    });

    tbody.appendChild(tr);
  });
}