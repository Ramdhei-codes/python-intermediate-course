from bokeh.plotting import figure, output_file, show
import read_csv

def run():
    output_file('cumpleaños.html', 'Cumpleaños de la familia')
    fig = figure()

    data = read_csv.read_csv('./cumpleaños.csv')


    fig.line(list(range(1,13)), list(data.values()), line_width=5)
    show(fig)

if __name__ == '__main__':
    run()
