def reverse(text):
    textlist = list(str(text))  # split text into list of letters
    word = "".join(textlist[::-1]) # join the list, in reverse
    return(word)