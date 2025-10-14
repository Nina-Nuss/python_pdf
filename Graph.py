from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie

#----------------------------------------------------------------------
def create_pie_chart():
    d = Drawing()
    pie = Pie()
    pie.x = 200
    pie.y = 65
    pie_data = [10, 20, 30, 40]
    pie.labels = [letter for letter in 'abcd']
    pie.slices.strokeWidth = 0.5
    pie.slices[3].popout = 20
    d.add(pie)
    d.save(formats=['pdf'], outDir='.', fnRoot='test-pie')


if __name__ == '__main__':
    create_pie_chart()