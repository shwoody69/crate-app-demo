from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout

Builder.load_string("""
<Calc>:
    a: _a
    b: _b
    c: _c
    result: _result
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        ScreenManager:
            size_hint: 1, .9
            id: _screen_manager
            Screen:
                name: 'screen1'
                GridLayout:
                    cols:1
                    TextInput:
                        multiline: False
                        id: _a
                        text: ''
                        font_size: 100
                        input_filter: "float"
                    TextInput:
                        multiline: False
                        id: _b
                        text: ''
                        font_size: 100
                        input_filter: "float"
                    TextInput:
                        multiline: False
                        id: _c
                        text: ''
                        font_size: 100
                        input_filter: "float" 
                    Button:
                        text: 'Slat Crate'
                        # You can do the opertion directly
                        on_release: root.slatcalc(args)
                    Button:
                        text: 'Double Ring Crate'
                        # Or you can call a method from the root class (instance of calc)
                        on_release: root.doublecalc(args)
            Screen:
                name: 'screen2'
                Label:
                    id: _result
                    font_size: 45
                    text_size: self.width, None
                    height: 500
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'bottom'
        BoxLayout:
            orientation: 'horizontal'
            size_hint: 1, .1
            Button:
                text: 'Calculator'
                on_press: _screen_manager.current = 'screen1'
            Button:
                text: 'Cut Sheet'
                on_press: _screen_manager.current = 'screen2'""")


class Calc(FloatLayout):
    def doublecalc(self, instance):
        length = self.a.text
        width = self.b.text
        height = self.c.text
        insides = str(int(length) + 2)
        outsides = str(float(width) + 3.5)
        slatnumber = str(int(length) // 12)
        heightnumber = str(((int(length)//12) * 2) + 6)
        if (int(width)//12) > 3:
            heightnumber = str(((int(length) // 12) * 2) + (int(slatnumber) * 2))
        if int(height) < 6:
            heightsize = str(int(7))
        else:
            heightsize = str(int(height) + 4)
        closernumber = str((int(length) // 12) * 2)
        outsideclosers = str(int(float(outsides) + 1.5))
        braces = str(float(length) + .5)
        self.result.text = "Cut 4 1x4's at " + insides + " inches.\nCut 4 1x4's at " + outsides + " inches.\nCut " + closernumber + " 1x4's at " + outsideclosers + " inches.\nCut " + heightnumber + " 1x4's at " + heightsize + " inches.\nCut 2 1x4's at " + braces + " inches."

    def slatcalc(self, instance):
        length = self.a.text
        width = self.b.text
        insides = str(int(length) + 2)
        outsides = str(float(width) + 3.5)
        slatnumber = str((int(length) // 12) + 2)
        closernumber = str(int(length) // 12)
        insideclosers = str(int(width) + 2)
        self.result.text = "Cut 2 1x4's at " + insides + " inches.\nCut " + slatnumber + " 1x4's at " + outsides + " inches.\nCut " + closernumber + " 1x4's at " + insideclosers + " inches."


class TestApp(App):
    def build(self):
        return Calc()


if __name__ == '__main__':
    TestApp().run()
