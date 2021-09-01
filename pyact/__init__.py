React = require ('react')
ReactDOM = require ('react-dom')

createElement = React.createElement
useState = React.useState
createContext = React.createContext
useContext = React.useContext
createRef = React.createRef
useEffect = React.useEffect

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
