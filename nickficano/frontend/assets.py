from flask.ext.assets import Environment, Bundle


#: application css bundle
css_all = Bundle("less/__init__.less", depends=["**/*.less"],
                 filters="less", output="css/style.css", debug=False)


def init_app(app):
    webassets = Environment(app)
    webassets.register('css_all', css_all)
    webassets.cache = not app.debug
    webassets.debug = app.debug
