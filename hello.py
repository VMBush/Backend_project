def app(environ, start_response):
    data = environ["QUERY_STRING"]
    data = data.replace("&", "\n")
    print(data)
    data = data.encode("UTF-8")

    start_response("200 OK", [
            ("Content-Type", "text/plain"),
            ("Content-Length", str(len(data)))
        ])
    return [data] 