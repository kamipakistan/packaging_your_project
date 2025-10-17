import urllib.request

import click
from bs4 import BeautifulSoup
from transformers import pipeline

def extract_from_url(url):
    """
    Fetches the given URL and extracts all visible paragraph (<p>) text.
    Returns a combined string of all paragraphs.
    """
    text = ''
    try:
        # Pretend to be a browser to avoid blocking
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        req = urllib.request.Request(url, headers=headers)

        with urllib.request.urlopen(req, timeout=10) as response:
            html = response.read().decode('utf-8', errors='ignore')

        # Parse HTML
        parser = BeautifulSoup(html, 'html.parser')

        # Extract all <p> text
        paragraphs = [p.get_text(strip=True) for p in parser.find_all('p')]
        text = "\n".join(paragraphs)

        return text

    except Exception as e:
        print(f"Error fetching or parsing {url}: {e}")
        return ""


def process(text):
    """
    Summarizes the input text using a Hugging Face model.
    Compatible with TensorFlow backend.
    """
    click.echo("Initializing summarizer model...")

    # Load the summarization model
    summarizer = pipeline("summarization", model="t5-small", framework="tf")

    # Hugging Face models have input token limits (e.g., 512-1024)
    max_chunk_length = 1000
    if len(text) > max_chunk_length:
        text = text[:max_chunk_length]
        click.echo("Input truncated to fit model token limit.")

    click.echo("Generating summary...")
    result = summarizer(
        text,
        max_length=180,
        min_length=30,
        do_sample=False
    )

    click.echo("Summarization process complete!")
    click.echo("=" * 80)

    return result[0]["summary_text"]
