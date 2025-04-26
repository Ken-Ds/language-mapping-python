
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

  function showSection(sectionId) {
    const sectionIds = ['statistics', 'language', 'delicacy', 'tourist'];

    sectionIds.forEach(id => {
      const section = document.getElementById(id);
      if (section) {
        section.style.display = (id === sectionId) ? 'block' : 'none';
      }
    });

    const buttons = document.querySelectorAll('.province-tabs button');
    buttons.forEach(btn => btn.classList.remove('active'));

    const clickedButton = Array.from(buttons).find(btn =>
      btn.getAttribute('onclick') === `showSection('${sectionId}')`
    );
    if (clickedButton) {
      clickedButton.classList.add('active');
    }

    // Fetch data ONLY when 'language' tab is clicked
    if (sectionId === 'language') {
      fetchIlocosNorteLanguage();
    }
  }


