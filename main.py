import cv2
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
class MainApp(App):

    def build(self):
        layout = BoxLayout(orientation='vertical',padding = 40)
        self.image = Image()
        layout.add_widget(self.image)

        self.capture = cv2.VideoCapture(0)
        Clock.schedule_interval(self.load_video, 1.0 / 30.0)

        return layout

    def load_video(self, *args):
        ret, frame = self.capture.read()
        #frame initialize
        self.image_frame = frame
        buffer = cv2.flip(frame, 0).tobytes()
        texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt = 'bgr')
        texture.blit_buffer(buffer, colorfmt='bgr', bufferfmt='ubyte')
        self.image.texture = texture


if __name__ == '__main__':
    MainApp().run()