class Extract:

    def find(data, lookup):
        new_data = data
        for search in lookup:
            new_data = new_data[search]
        return new_data


