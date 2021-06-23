import click
import robin_stocks as rs

@click.group()
def main():
    print('hello')

@main.command(help='gets a stock quote for one or more symbols')
@click.argument('symbols')
def quote(symbols):
    pass

@main.command(help='gets a stock quote for all stocks in watchlist')
def watchlist():
    print('x')

if __name__ == '__main__':
    main()