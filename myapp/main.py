import click
import myapp.subcommands.run.cli as run

@click.group()
@click.help_option('-h', '--help')
@click.version_option('0.1', '-v', '--version', message='%(prog)s v%(version)s')
@click.option('-d', '--debug', default=False, envvar='DEBUG', is_flag=True)
def entry_point(debug):
    click.echo("entry_point")

entry_point.add_command(run.run)
