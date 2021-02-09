from gui import UI, generate_app

if __name__ == '__main__':
    app = generate_app()
    ui = UI()
    ui.resize(600, 400)
    ui.show()
    exit(app.exec_())
