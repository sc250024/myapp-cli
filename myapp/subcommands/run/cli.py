import click
import myapp.resources.functions as functions

@click.command()
@click.help_option('-h', '--help')
def run():
    click.echo("run")
    click.echo("The current OS is: {}".format(functions.get_current_os()))
