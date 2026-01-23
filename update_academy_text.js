const fs = require('fs');
const path = require('path');

const localesDir = path.join(__dirname, 'dawn/locales');
const translationKey = "strongside.header.academy";

const translations = {
	"fr": "ACADÉMIE",
	"en": "ACADEMY",
	"es": "ACADEMIA",
	"de": "AKADEMIE",
	"it": "ACCADEMIA",
	"pt-PT": "ACADEMIA",
	"pt-BR": "ACADEMIA",
	"nl": "ACADEMIE"
};

// Default fallback
const defaultText = "ACADEMY";

fs.readdir(localesDir, (err, files) => {
	if (err) {
		console.error("Could not list locales directory.", err);
		process.exit(1);
	}

	files.forEach(file => {
		if (!file.endsWith('.json')) return;

		const filePath = path.join(localesDir, file);
		const langCode = file.split('.')[0]; // e.g. 'fr' from 'fr.json'

		// Handle special case for en.default.json
		const effectiveLang = file.startsWith('en.default') ? 'en' : langCode;

		const textToInsert = translations[effectiveLang] || defaultText;

		try {
			const content = JSON.parse(fs.readFileSync(filePath, 'utf8'));

			// Ensure nested structure exists
			if (!content.strongside) content.strongside = {};
			if (!content.strongside.header) content.strongside.header = {};

			// Add keys
			content.strongside.header.academy = textToInsert;

			fs.writeFileSync(filePath, JSON.stringify(content, null, 2));
			console.log(`Updated ${file} with: "${textToInsert}"`);

		} catch (e) {
			console.error(`Error processing ${file}:`, e);
		}
	});
});
