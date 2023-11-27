from model import load_new_data

def update_data_output(filename):
    """
    Update the output of the data upload component
    """
    if filename is not None:
        try:
            load_new_data(filename)
        except Exception as e:
            print(e)
            return html.Div(
                children = [
                    'Ocurrió un error al procesar el archivo.',
                ],
                className = "alert alert-danger",
                role = "alert",
            )

    # If no file is uploaded, return an empty component
    return ""
