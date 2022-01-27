class ReplaceString:
    def replace(self, name):
        if (len(name) <3):
            print("please enter valid name")
        else:
            print(f"hello {name} how are you?")

template = ReplaceString()
name = input("ENTER NAME:")
template.replace(name)