from app import init_app

if __name__ == '__main__':

    application = init_app()
    application.run(host='0.0.0.0', port=8000)
