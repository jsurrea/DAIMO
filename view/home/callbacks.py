from logic import load_new_data, load_saved_data
from dash import Input, Output, State, callback, html


def register_home_callbacks():
    """
    Register callbacks of the home component
    """
    
    @callback(
        Output('output-data-upload', 'children'),
        Input('upload-data', 'contents'),
        State('upload-data', 'filename'),
    )
    def update_data_output(contents, filename):
        """
        Update the output of the data upload component
        """
        if filename is not None:
            try:
                load_new_data(contents, filename)
                return html.Div(
                    children = [
                        'El archivo se cargó correctamente.',
                    ],
                    className = "alert alert-success",
                    role = "alert",
                )
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


    @callback(
        Output("app-storage", "data"),
        Input("home-radioitems", "value"),
    )
    def update_data_source(selected_data):
        """
        Update the data source of the model
        """
        if selected_data is not None:
            load_saved_data(selected_data)
            return selected_data
