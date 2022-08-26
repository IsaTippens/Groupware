class Service():
    """
        Services abstract the interaction being data storage/retrieval from a frontend
        Data is parsed to the relevant views as well as additional processing
        It does not care where or how the data is stored and retrieved, thats the job of the repositories
        As long as the repository provides the expected data type, services can do their job

        Frontends could be a gui/rest api/ or a terminal interface like the one we're doing.
    """
    def __init__(self):
        pass
    
    def get_all(self):
        pass

    def get(self,name: str):
        pass

    def add(self,value):
        pass

    def update(self,value):
        pass

    def delete(self,value):
        pass