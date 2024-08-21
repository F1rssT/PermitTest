import gspread
from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.core.window import Window

#up



WINDOW_COLOR = (0.9, 0.9, 0.9, 1)
HEADER_COLOR = (0.2, 0.6, 0.8, 1)
ROW_COLOR_1 = (0.95, 0.95, 0.95, 1)
ROW_COLOR_2 = (1, 1, 1, 1)
BUTTON_COLOR = (0.2, 0.6, 0.8, 1)
BUTTON_TEXT_COLOR = (1, 1, 1, 1)
BUTTON_SIZE_HINT = (0.3, None)
BUTTON_HEIGHT = 50

credentials = {
  "type": "service_account",
  "project_id": "mytestsheets-433007",
  "private_key_id": "6d0ab6ee7f339e28e7928496dc9e104d15215fa6",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQC+qw80XL9oXPE4\ngOrujZ5XTewzJ5NzdRufIeD+yS808Z9XorjQhVmlVzyP8TtUh7S5KN8tJEW9O4xi\ntVMmGNTCknjnt62BO6U6cZzSz2g3JCXgYyBJBET2OJ4nDvVxXUBaI54MovtcN+vs\nKZOJWS5nWF1P+ivKCPsuil4pZkc3BC0m4NF+vMGMGuD2XS6lErzVxpX1K1wNQPCm\nHBo0lNnEPlg6wVkycClKbMfciX0rY6nHolvQNo1fxG4/vbIA6EQwhFoNbjh8/S2f\nQRY7UnnlJfkx6/SToGR2zpB2nqChTyniKPnC4+NKL9hXL9RO7XcFcTKEBjleDIpn\n6f7tEsInAgMBAAECggEAXvaRxxGen5sS5YKIADJ2t6Luznean/mmvTZBeoS3R1ZE\nd4BrLigMgyYU2thaJXrFjycFKNWVCm/bNtp6xFG/vfz3zOkVuHT9kUM+yVxV2ojd\neInGbbd7pWqDko6HvmOkhoCQ2lheewq7LU9z1Qee7gf7ybafEqwwdnih91qig4pq\noQ3VilCGCEXAQG743QoheZx3q45pK3Z5NOYuEoq0AwUUcXtU2ZvBg3qTjfU8MTAv\n+OB1t3X4/k4QS9Vpyiw1QZ2PDEBWFBppquQyC1/XAtuQp9ckpG7xttYuo0lWccLo\ntLxZpzdECeYkqgbGg9m4+SfP9PGdcqttl0CRG4HbqQKBgQD12rm3zynUk8jR+JD0\nwz5sKr6pu6TPxmokmMTWGlitnmguMndy2XYePXqvwAASd8p+x7/Hi/SviMUgyncv\nKoqvT9qQU/BEVqlbo5mka70PWAPR/PpB9aARSoR0OtwwkZuAnQaEpJOdwmcI6b4R\nYNT1yyxd7SKuNu/JI8V2tGbgpQKBgQDGiVTf6fS5T3j2iywMXKQt4QedWznSsvbK\ndQNa52oytOXsvlr+pTR2xVriA8tJwhDDVugOg7Vxmw22jcFhgB4C8jmVEaCh5dba\nc3KTe9qSZUVzM4izebMiSjoFUhakJS5D+1kil0x5QMX9gNIbcKmThKkR0iEthaTL\nuShRQf0x2wKBgQC5lLdn1krfGgcW6CiTeeXexI1Tlj8cT8vDgEXkz9JsjAxcAuBD\no38T6Jh5ndbwGdiSxrkvKagz8GvNCsfYpKY3G3ICTDore7cvY1kQ0frOYEPR+MH3\nlC+VnchJ7DxVtTPKa72F1q1PAnXANqCwgYV/XDRLWjs5gmKSVBw0NI0LuQKBgQCC\nez+M6fYs1E5ruov4k+pTPNIEWTBnibco2D6cP/tL2BhEv9aOBYW1iX9xi4zPrPvX\nZgadg3J8d6tLj17I9arDxO6TSkKIJMZQTA/BXmUIUgaS8Aun6RQSNTZsyMaYmtcN\nVuP+F/Hqvudg9Ikh/6lzinyTecbUZEEqo0YcIYKGgQKBgQCq4+aspu2Zm1RHz6aJ\n1w8PgUR2c6+cH1eDfhDM7ZXyOI8D1xMdMWcSlUGpeJqiFJ2j7Xb6hJuP6emLuG+M\nv7wSIZU++S480EkMFn6F6SIbJn2OVdRVxEPeZF2CU1RO8znGMDNJE1R96ic0str5\nnrqyWw5ee9Sg+ZXCqe4KKmNU3A==\n-----END PRIVATE KEY-----\n",
  "client_email": "sheets-test-api@mytestsheets-433007.iam.gserviceaccount.com",
  "client_id": "111944113809933343092",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/sheets-test-api%40mytestsheets-433007.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}

gc = gspread.service_account_from_dict(credentials)
sh = gc.open("Permits_test")


class ColoredLabel(Label):
    def __init__(self, background_color, **kwargs):
        super(ColoredLabel, self).__init__(**kwargs)
        with self.canvas.before:
            Color(*background_color)
            self.rect = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect, pos=self._update_rect)
        self.bind(texture_size=self._update_rect)
    
    def _update_rect(self, instance, value):
        self.rect.pos = self.pos
        self.rect.size = self.size


class AddPopup(Popup):
    def __init__(self, **kwargs):
        super(AddPopup, self).__init__(**kwargs)
        self.title = "Додати перепустку"
        self.size_hint = (None, None)
        self.size = (400, 300)

        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.name_input = TextInput(hint_text="ПІБ")
        self.permit_number_input = TextInput(hint_text="Номер перепустки")
        self.supervisor_input = TextInput(hint_text="Супервізор")
        self.description_input = TextInput(hint_text="Опис")
        

        layout.add_widget(self.name_input)
        layout.add_widget(self.permit_number_input)
        layout.add_widget(self.supervisor_input)
        layout.add_widget(self.description_input)

        add_button = Button(text="Додати", background_color=BUTTON_COLOR, color=BUTTON_TEXT_COLOR)
        add_button.bind(on_press=self.add_permit)
        layout.add_widget(add_button)

        self.content = layout

    def add_permit(self, instance):
        val = sh.sheet1.get_all_values()
        size = len(val)
        name = self.name_input.text
        permit_number = self.permit_number_input.text
        supervisor = self.supervisor_input.text
        description = self.description_input.text
        if name and permit_number and supervisor:
            sh.sheet1.update([[size,name, int(permit_number), supervisor, "Видано", "Працює", description]], 'A'+str(size+1))

        else:
            popup = Popup(title="Помилка", content=Label(text="Усі поля мають бути заповнені"), size_hint=(None, None), size=(400, 200))
            popup.open()


class PermitList(Popup):
    def __init__(self, **kwargs):
        super(PermitList, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.title = ""
        self.size_hint = (None, None)
        self.size = (600, 600)


        grid = GridLayout(cols=6, size_hint_y=None, spacing=1, padding=1)
        grid.bind(minimum_height=grid.setter('height'))

        column_widths = [20, 180, 100, 150, 100, 100]
        headers = ["ID", "ПІБ", "Номер перепустки", "Супервізор", "Статуп перепустки", "Статус працівника"]
        permits = sh.sheet1.get_all_records()
        for header, width in zip(headers, column_widths):
            label = ColoredLabel(text=header, background_color=HEADER_COLOR, color=(1, 1, 1, 1), bold=True, size_hint_y=None, height=40)
            label.text_size = (width, None)
            label.halign = 'center'
            label.valign = 'middle'
            grid.add_widget(label)


        for i, permit in enumerate(permits, 1):
            id = permit['ID']
            name = permit['ПІБ']
            permit_number = permit['Номер перепустки']
            supervisor = permit['Супервізор']
            permit_status = permit['Статус Перепустки']
            worker_status = permit['Статус Працівника']
            # description = permit['Опис'] 
  
            row_color = ROW_COLOR_1 if i % 2 == 0 else ROW_COLOR_2
            grid.add_widget(self.create_label(str(id), row_color, column_widths[0]))
            grid.add_widget(self.create_label(name, row_color, column_widths[1]))
            grid.add_widget(self.create_label(str(permit_number), row_color, column_widths[2]))
            grid.add_widget(self.create_label(supervisor, row_color, column_widths[3]))
            grid.add_widget(self.create_label(permit_status, row_color, column_widths[4]))
            grid.add_widget(self.create_label(worker_status, row_color, column_widths[5]))
            # grid.add_widget(self.create_label(description, row_color, column_widths[6]))


        scroll = ScrollView(size_hint=(1, 1))
        scroll.add_widget(grid)
        self.add_widget(scroll)

    def create_label(self, text, background_color, width):
        label = ColoredLabel(text=text, background_color=background_color, color=(0, 0, 0, 1), size_hint_y=None, height=40)
        label.text_size = (width, None)
        label.halign = 'center'
        label.valign = 'middle'
        label.padding = [10, 5]  # Add padding for better text visibility
        return label
    


class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [20, 10, 20, 10]
        self.spacing = 10

        button_layout = BoxLayout(size_hint_y=None, height=BUTTON_HEIGHT, spacing=10)
        self.add_widget(button_layout)
    
        add_button = Button(text="Додати", background_color=BUTTON_COLOR, color=BUTTON_TEXT_COLOR, size_hint=BUTTON_SIZE_HINT)
        add_button.bind(on_press=self.open_add_popup)
        button_layout.add_widget(add_button)

        scan_button = Button(text="Сканувати", background_color=BUTTON_COLOR, color=BUTTON_TEXT_COLOR, size_hint=BUTTON_SIZE_HINT)
        scan_button.bind(on_press=self.scan_entry)
        button_layout.add_widget(scan_button)

        list_button = Button(text="Список", background_color=BUTTON_COLOR, color=BUTTON_TEXT_COLOR, size_hint=BUTTON_SIZE_HINT)
        list_button.bind(on_press=self.show_list)
        button_layout.add_widget(list_button)


        exit_button = Button(text="Вийти", background_color=BUTTON_COLOR, color=BUTTON_TEXT_COLOR, size_hint=BUTTON_SIZE_HINT)
        exit_button.bind(on_press=self.exit_app)
        button_layout.add_widget(exit_button)
    
    def open_add_popup(self, instance):
        popup = AddPopup()
        popup.open()

    def scan_entry(self, instance):
        popup = Popup(title="Сканувати", content=Label(text="Ця функція ще не реалізована"), size_hint=(None, None), size=(400, 200))
        popup.open()

    def show_list(self, instance):
        popup = PermitList()
        popup.open()


    def exit_app(self, instance):
        App.get_running_app().stop()

class MyApp(App):
    def build(self):
        Window.clearcolor = WINDOW_COLOR
        return MainScreen()
    





MyApp().run()