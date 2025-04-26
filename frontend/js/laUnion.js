async function fetchLaUnionLanguage() {
  const provinceId = 'P003';
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


async function fetchLaUnionStatistics() {
  try {
    const provinceId = 'P003'; // La Union
    const response = await fetch(`http://127.0.0.1:8000/statistics/${provinceId}`);

    if (!response.ok) {
      throw new Error('Network response was not ok');
    }

    const data = await response.json();

    const municipalityStatsSection = document.querySelector('#municipalityStats');
    const overallStatsSection = document.querySelector('#overallStats');

    municipalityStatsSection.innerHTML = ''; // Clear existing stats
    overallStatsSection.innerHTML = ''; // Clear existing stats

    if (data.length === 0) {
      const noDataItem = document.createElement('p');
      noDataItem.textContent = 'No language data available.';
      municipalityStatsSection.appendChild(noDataItem);
      overallStatsSection.appendChild(noDataItem);
      return;
    }

    // Step 1: Display Top 3 Languages for Each Municipality
    data.forEach(municipality => {
      const statItem = document.createElement('div');
      statItem.classList.add('stat-item');

      const title = document.createElement('h4');
      title.textContent = municipality.name; // Municipality Name
      statItem.appendChild(title);

      const languageList = document.createElement('ul');

      municipality.languages.slice(0, 3).forEach(language => { // Only take top 3 languages
        const listItem = document.createElement('li');
        listItem.textContent = language;
        languageList.appendChild(listItem);
      });

      statItem.appendChild(languageList);
      municipalityStatsSection.appendChild(statItem);
    });

    // Step 2: Display Overall Top 10 Languages
    const languageCounts = {};

    data.forEach(municipality => {
      municipality.languages.forEach(language => {
        if (!languageCounts[language]) {
          languageCounts[language] = 0;
        }
        languageCounts[language]++;
      });
    });

    const topLanguages = Object.entries(languageCounts)
      .sort((a, b) => b[1] - a[1])
      .slice(0, 10)
      .map(([language]) => language);

    const overallStatItem = document.createElement('div');
    overallStatItem.classList.add('stat-item');

    const overallTitle = document.createElement('h4');
    overallTitle.textContent = 'Overall Top 10 Languages';
    overallStatItem.appendChild(overallTitle);

    const overallLanguageList = document.createElement('ul');

    topLanguages.forEach(language => {
      const listItem = document.createElement('li');
      listItem.textContent = language;
      overallLanguageList.appendChild(listItem);
    });

    overallStatItem.appendChild(overallLanguageList);
    overallStatsSection.appendChild(overallStatItem);

  } catch (error) {
    console.error('Error fetching La Union statistics:', error);
  }
}



async function fetchLaUnionDelicacies() {
  try {
    const provinceId = 'P003'; // La Union
    const response = await fetch(`http://127.0.0.1:8000/popular/foods/${provinceId}`);

    if (!response.ok) {
      throw new Error('Network response was not ok');
    }

    const data = await response.json();

    const delicacySection = document.querySelector('#delicacy');
    const delicacyList = delicacySection.querySelector('.delicacy-list');

    delicacyList.innerHTML = ''; // Clear existing list

    if (data.length === 0) {
      const noDataItem = document.createElement('li');
      noDataItem.textContent = 'No delicacies available.';
      delicacyList.appendChild(noDataItem);
      return;
    }

    // Create list items for each delicacy
    data.forEach(item => {
      const listItem = document.createElement('li');
      listItem.textContent = item.NAME;
      delicacyList.appendChild(listItem);
    });

  } catch (error) {
    console.error('Error fetching La Union delicacy data:', error);
  }
}

async function fetchLaUnionTouristSpots() {
  try {
    const provinceId = 'P003'; // La Union
    const response = await fetch(`http://127.0.0.1:8000/popular/tourist-spots/${provinceId}`);

    if (!response.ok) {
      throw new Error('Network response was not ok');
    }

    const data = await response.json();

    const touristSection = document.querySelector('#tourist');
    const touristList = touristSection.querySelector('.tourist-list');

    touristList.innerHTML = ''; // Clear existing list

    if (data.length === 0) {
      const noDataItem = document.createElement('li');
      noDataItem.textContent = 'No tourist spots available.';
      touristList.appendChild(noDataItem);
      return;
    }

    // Create list items for each tourist spot
    data.forEach(item => {
      const listItem = document.createElement('li');
      listItem.innerHTML = `
        <div class="tourist-item">
          <div class="tourist-name">${item.NAME}</div>
          <div class="tourist-location">${item.LOCATION}</div>
        </div>
      `;
      touristList.appendChild(listItem);
    });

  } catch (error) {
    console.error('Error fetching La Union tourist spot data:', error);
  }
}

