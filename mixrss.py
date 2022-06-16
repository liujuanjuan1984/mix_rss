from flaskwebgui import FlaskUI

from mixrss.app import app


def run_app():
    # 静态资源修改不需要重启
    app.jinja_env.auto_reload = True
    app.run(debug=True)


def run_ui():
    # 静态资源修改不需要重启
    ui = FlaskUI(app, width=1024, height=680, host="0.0.0.0")
    ui.run()


def app_path():
    # 使用pyinstaller打包成单文件需要处理路径问题
    app_path = ""
    if hasattr(sys, "_MEIPASS"):  # 如果是单个EXE文件执行的时候sys中会存在这个_MEIPASS变量作为当前的工作根路径
        app_path = os.path.join(sys._MEIPASS)


if __name__ == "__main__":
    run_app()
