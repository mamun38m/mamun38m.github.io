import json
from pathlib import Path


# ============================================================
# 1. File paths
# ============================================================

data_file = Path("data.json")
html_file = Path("index.html")


# ============================================================
# 2. Read data.json
# ============================================================

data = json.loads(
    data_file.read_text(encoding="utf-8")
)


# ============================================================
# 3. Generate Research Interests
# ============================================================

research_html = ""

for item in data.get("research_interests", []):
    research_html += f"""
        <li>{item}</li>
    """


# ============================================================
# 4. Generate Education
# ============================================================

education_html = ""

for item in data.get("education", []):
    education_html += f"""
        <div class="education-item">
            <h3>{item.get("degree", "")}</h3>
            <p>{item.get("institution", "")}</p>
            <p>{item.get("year", "")}</p>
        </div>
    """


# ============================================================
# 5. Generate Publications
# ============================================================

publication_html = ""

for item in data.get("publications", []):
    publication_html += f"""
        <div class="publication-item">
            <h3>{item.get("title", "")}</h3>
            <p>
                {item.get("journal", "")}
                ·
                {item.get("year", "")}
            </p>
            <a href="{item.get("doi", "#")}" target="_blank">
                DOI
            </a>
        </div>
    """


# ============================================================
# 6. Generate complete HTML
# ============================================================

html_content = f"""<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport"
          content="width=device-width, initial-scale=1.0">

    <title>{data.get("name", "My Website")}</title>

    <link rel="stylesheet" href="style.css">

</head>


<body>

    <header>

        <h1>{data.get("name", "")}</h1>

        <p>{data.get("title", "")}</p>

        <nav>

            <a href="#about">About</a>

            <a href="#research">Research</a>

            <a href="#education">Education</a>

            <a href="#publications">Publications</a>

        </nav>

    </header>


    <main>

        <!-- About -->

        <section id="about">

            <h2>About Me</h2>

            <p>
                {data.get("about", "")}
            </p>

        </section>


        <!-- Research -->

        <section id="research">

            <h2>Research Interests</h2>

            <ul>

                {research_html}

            </ul>

        </section>


        <!-- Education -->

        <section id="education">

            <h2>Education</h2>

            {education_html}

        </section>


        <!-- Publications -->

        <section id="publications">

            <h2>Publications</h2>

            {publication_html}

        </section>

    </main>


    <script src="script.js"></script>

</body>

</html>
"""


# ============================================================
# 7. Write index.html
# ============================================================

html_file.write_text(
    html_content,
    encoding="utf-8"
)


# ============================================================
# 8. Success message
# ============================================================

print("Website updated successfully.")

print("Name:", data.get("name", ""))

print(
    "Research interests:",
    len(data.get("research_interests", []))
)

print(
    "Education:",
    len(data.get("education", []))
)

print(
    "Publications:",
    len(data.get("publications", []))
)