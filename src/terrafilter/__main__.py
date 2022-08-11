"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Terrafilter."""


if __name__ == "__main__":
    main(prog_name="terrafilter")  # pragma: no cover
