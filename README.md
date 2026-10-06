# Isikhungo Sezobuchwepheshe Boluntu

A Streamlit website for a community-focused technology organization. The site includes home, about, services, impact, and contact sections.

## Requirements

- Python 3.9 or later
- The Python packages listed in `requirements.txt`
- `hero-image.png` in the same directory as `siz_9.py`

## Setup

From the directory containing `siz_9.py`, `requirements.txt`, and `hero-image.png`, install the dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run

The attached script has a syntax error in the About page branch. In `siz_9.py`, change:

```python
elif page == "Okumayelana nathi
```

to:

```python
elif page == "Okumayelana nathi":
```

Then start the website with:

```bash
streamlit run siz_9.py
```

Streamlit will print the local URL in the terminal and open the app in a browser.

## Asset

The home page loads `hero-image.png` from the same folder as the script. Add that image before running the site; otherwise the home page cannot display its hero image.
