class DisplayBox:

    def __init__(self, text: str = None, width: int = 66):
        self.text: list[str] = []
        self.width: int = width
        if text is not None:
            self.add_text(text)

    def __str__(self):
        output = self.separator()
        for line in self.text:
            output += line
        output += self.separator()
        return output

    def separator(self) -> str:
        return f"+{"-" * (self.width - 2)}+\n"
    
    def add_separator(self) -> "DisplayBox":
        self.text.append(self.separator())
        return self


    def add_text(self, *lines) -> "DisplayBox":
        for line in lines:
            spaces = (self.width - (len(line) + 2)) // 2
            if self.width % 2 != len(line) % 2:
                self.text.append(f"|{" " * (spaces + 1)}{line}{" " * spaces}|\n")
            else:
                self.text.append(f"|{" " * spaces}{line}{" " * spaces}|\n")
        return self
