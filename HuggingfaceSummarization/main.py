import click
import os
from .utils import extract_from_url, process

# Mute TensorFlow logs
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


@click.command()
@click.option('--url', type=str, help='Provide a URL to extract and summarize text from.')
@click.option('--file', type=click.Path(exists=True), help='Provide a file path to summarize its content.')
def main(url, file):
    """
    Summarizes text either from a given URL or from a local file.
    Example usage:
      python main.py --url https://example.com
      python main.py --file article.txt
    """
    if not url and not file:
        click.echo("Please provide either --url or --file option.")
        return

    # Extract text
    if url:
        text = extract_from_url(url)
    elif file:
        with open(file, 'r', encoding='utf-8') as f:
            text = f.read()

    if not text.strip():
        click.echo("No text found to summarize.")
        return
    click.echo('\n')
    click.echo('\n')
    click.echo('\n')
    click.echo(f"Summarizing text from → {url or file}")
    click.echo("=" * 80)

    # Run summarization
    click.echo("Summary..")
    summary = process(text)

    click.echo(summary)
    click.echo("=" * 80)
    click.echo("Done!")



if __name__ == '__main__':
    main()
