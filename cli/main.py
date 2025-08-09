import click

@click.group()
def cli():
    """CleanDrop CLI - Dropbox → Scrubber → S3"""
    pass

@cli.command()
def auth():
    """Authenticate with Dropbox (OAuth2)."""
    click.echo("Auth placeholder - Milestone 01.")

@cli.command()
def ingest():
    """Ingest files from Dropbox."""
    click.echo("Ingest placeholder - Milestone 02.")

@cli.command()
def scrub():
    """Scrub files via external API."""
    click.echo("Scrub placeholder - Milestone 04.")

@cli.command()
def upload():
    """Upload scrubbed files to S3."""
    click.echo("Upload placeholder - Milestone 05.")

if __name__ == "__main__":
    cli()
