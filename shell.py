import main



def getText(var):
    inputText=var

    result, error = main.run('<stdin>', inputText)

    if error:
        return (error.as_string())
    elif result:
        return (result)
