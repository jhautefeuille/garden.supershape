garden.supershape
=================

Generate super shape with Kivy framework

Example

	class ShapeTest(App):
        def build(self):
            shape = Shape(n1=7, color='3619ffff', bg_color='19526699', size_hint=(0.8, 1))
            return shape

Properties

	shape_size = BoundedNumericProperty(256, min=1, max=512, errorvalue=512)
    color = StringProperty('3619ffff')
    bg_color = StringProperty('19526699')
    a = BoundedNumericProperty(1, min=0.1, max=1, errorvalue=1)
    b = BoundedNumericProperty(1, min=0.1, max=1, errorvalue=1)
    m = BoundedNumericProperty(7, min=-100, max=100, errorvalue=16)
    n1 = BoundedNumericProperty(2, min=1, max=50, errorvalue=4)
    n2 = BoundedNumericProperty(8, min=1, max=50, errorvalue=4)
    n3 = BoundedNumericProperty(4, min=1, max=50, errorvalue=10)
    nbp = BoundedNumericProperty(100, min=2, max=1000, errorvalue=100)
    percent = BoundedNumericProperty(1, min=1, max=10, errorvalue=1)
    travel = BoundedNumericProperty(2, min=2, max=100, errorvalue=2)
    line = BooleanProperty(False)
    wdth = BoundedNumericProperty(1, min=1, max=10, errorvalue=1)
    path = ListProperty()
