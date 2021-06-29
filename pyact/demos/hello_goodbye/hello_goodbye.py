import pyact as pa

def greeter ():
    (text, color), setMessage = pa.useState (('Press Hello or Goodbye', 'black'))

    def sayHello ():
        setMessage (('Hello to you as well', 'green'))

    def sayGoodbye ():
        setMessage (('Goodbye to you as well', 'red'))

    return [
        pa.createElement ('button', {'onClick': sayHello}, 'Hello'),
        pa.createElement ('button', {'onClick': sayGoodbye}, 'Goodbye'),
        pa.createElement ('div', {'style': {'color': color}}, text)
    ]

pa.render (greeter, None, 'root')
