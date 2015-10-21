class Assistant(object):

    """Docstring for Assistant. """

    def __init__(self):
        """TODO: to be defined1. """

    def list_ideas(self,topic,count):
        """TODO: Docstring for list_ideas.

        :topic: TODO
        :count: TODO
        :returns: a list of related ideas

        """
        knowledge_base = KnowledgeClient(host,port)
        knowledges = knowledge_base.find(topic,count)
        return knowledges


    def search(self, topic, count):
        """TODO: Docstring for search.
        :returns: TODO

        """
