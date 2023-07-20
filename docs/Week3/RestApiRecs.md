# [REST API - FASTAPI](https://www.linkedin.com/posts/jesumyip_custom-response-html-stream-file-others-activity-7083432591449604097-CSl1/)

- Use ORJSONResponse as opposed to JSONResponse
    - [ORJSON](https://lnkd.in/gMqRCCMc)
    ```py
    from fastapi import FastAPI
    from fastapi.responses import ORJSONResponse

    app = FastAPI()


    @app.get("/items/", response_class=ORJSONResponse)
    async def read_items():
    return ORJSONResponse([{"item_id": "Foo"}])
    ```

- Suggested to be using try-catch blocks for Pydantic for composing return data
    - Unnecessary to use jsonable_encoder as it cause FastAPI to perform another round of Pydantic validation based on API response model

- OpenTelemetry
    - Incorporating OT into code -> wrapping each function in otel trace allows for performance tracking of every fxn in code
    - Otel data is exported to NewRelic allowing for analysis of function speed and optimization
    - "OTEL_PYTHON_LOG_FORMAT" environment variable (for the OpenTelemetry Python SDK) to a value of "%(pathname)s:%(funcName)s:%(lineno)d:%(levelname)s:%(message)s" -> use the logging Pypi module
        * Causes OT to log full path to .py file, function name, and line number
