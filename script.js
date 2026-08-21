fetch("data.json")
    .then(response => response.json())
    .then(data => {

        document.getElementById("name").textContent =
            data.name;

        document.getElementById("title").textContent =
            data.title;

        document.getElementById("about-text").textContent =
            data.about;


        // Research interests

        const researchList =
            document.getElementById("research-list");

        data.research_interests.forEach(item => {

            const div = document.createElement("div");

            div.textContent = item;

            researchList.appendChild(div);

        });


        // Education

        const educationList =
            document.getElementById("education-list");

        data.education.forEach(item => {

            const div = document.createElement("div");

            div.innerHTML = `
                <h3>${item.degree}</h3>
                <p>${item.institution}</p>
                <p>${item.year}</p>
            `;

            educationList.appendChild(div);

        });


        // Publications

        const publicationList =
            document.getElementById("publication-list");

        data.publications.forEach(item => {

            const div = document.createElement("div");

            div.innerHTML = `
                <h3>${item.title}</h3>
                <p>${item.journal} · ${item.year}</p>
                <a href="${item.doi}" target="_blank">
                    DOI
                </a>
            `;

            publicationList.appendChild(div);

        });

    });