import uvicorn


if __name__ == "__main__":
    # Loading config for server and starting it
    config = uvicorn.Config("ServerApplication:app", port=8080, log_level="info", log_config="logconfig.ini")
    server = uvicorn.Server(config)
    server.run()