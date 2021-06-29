React = require ('react')
ReactDOM = require ('react-dom')

el = createElement = React.createElement
us = useState = React.useState
cc = createContext = React.createContext
uc = useContext = React.useContext

def render (component, properties, parentId):
    def main ():
        ReactDOM.render (
            React.createElement (component, properties),
            document.getElementById (parentId)
        )

    document.addEventListener ('DOMContentLoaded', main)

alert = window.alert

def val (event):
    return event ['target']['value']
