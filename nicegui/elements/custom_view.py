import justpy as jp
import os.path

class CustomView(jp.JustpyBaseComponent):

    vue_dependencies = []

    def __init__(self, vue_type, filename, dependencies=[], **options):

        self.vue_type = vue_type
        self.vue_filepath = os.path.realpath(filename).replace('.py', '.js')
        self.vue_dependencies = dependencies

        self.pages = {}
        self.classes = ''
        self.options = jp.Dict(**options)

        super().__init__()

        self.initialize(temp=False)

    def add_page(self, wp: jp.WebPage):

        marker = '<!--' + self.__module__ + '-->\n'
        if marker not in wp.head_html:
            wp.head_html += marker
            for dependency in self.vue_dependencies:
                wp.head_html += f'<script src="{dependency}"></script>\n'

        if self.vue_filepath not in jp.component_file_list:
            jp.component_file_list += ['file?path=' + self.vue_filepath]

        super().add_page(wp)

    def react(self, _):

        pass

    def convert_object_to_dict(self):

        return {
            'vue_type': self.vue_type,
            'id': self.id,
            'show': True,
            'options': self.options,
        }
