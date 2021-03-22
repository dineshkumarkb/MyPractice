import click


@click.group()
def main():
    pass


@main.command()
@click.option("--a", prompt=" Enter the first number", type=int)
@click.option("--b", prompt=" Enter the second number", type=int)
def add(a, b):
    value = a + b
    click.echo(" The added value {}".format(value))


@main.command()
@click.option("--a", prompt=" Enter the first number", type=int)
@click.option("--b", prompt=" Enter the second number", type=int)
def sub(a, b):
    value = a - b
    click.echo(" The difference is {}".format(value))


@main.command()
@click.option("--a", prompt=" Enter the first number", type=int)
@click.option("--b", prompt=" Enter the second number", type=int)
def mul(a, b):
    value = a * b
    click.echo(" The multiplied value {}".format(value))


@main.command()
@click.option("--a", prompt=" Enter the first number", type=int)
@click.option("--b", prompt=" Enter the second number", type=int)
def div(a, b):
    value = a / b
    click.echo(" The  value {}".format(value))


if __name__ == "__main__":
    main()

    