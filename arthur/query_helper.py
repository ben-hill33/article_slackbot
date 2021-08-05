

class QueryHelper(object):
    
    def __init__(self, name, query=None, category=None, country=None, sources=None, language=None, slack_channel=None):
        """Constructs the query helper object.

        Args:
            name: string, The name for this query used in Slack.
            query: string, The query to use. Advanced search is available:
                Surround phrases with quotes (") for exact match.
                Prepend words or phrases that must appear with a + symbol. Eg: +bitcoin
                Prepend words that must not appear with a - symbol. Eg: -bitcoin
                Alternatively you can use the AND / OR / NOT keywords,
                    optionally group these with paranthesis.
                    Eg: crypto AND (ethereum OR litecoin) NOT bitcoin.
            category: string, One of business, entertainment, general, health, science, sports, technology.
                Cannot be set if sources is set.
            country: string, The 2-letter ISO 3166-1 code (lowercase) for the country.
                Cannot be set if sources is set
            sources: list, String sources valid for the api. Obtainable from https://github.com/Medium/medium-api-docs
            language: [description]. Defaults to None.
            slack_channel: [description]. Defaults to None.
        """
        pass

