
class ReadListController:
    vect = []

    def __init__(self, route):
        file = open(route, 'r')
        for line in file:
            self.vect.append(line.rstrip('\n'))
        file.close()

    def get_list(self):
        return self.vect

    def get_formatted_list(self, is_string=False):
        chain = ''
        separator = ''
        if is_string:
            separator = "'"

        for obj in self.vect:
            new_obj = separator + obj + separator
            if chain == '':
                chain = new_obj
            else:
                chain = chain + ', ' + new_obj

        return chain
