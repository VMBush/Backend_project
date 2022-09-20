def app(environ, start_response):
    data = environ["QUERY_STRING"]
    data = data.replace("&", "\n")
    data = data.encode("UTF-8")

    start_response("200 OK", [
            ("Content-Type", "text/plain"),
            ("Content-Length", str(len(data)))
        ])
    return [data] 