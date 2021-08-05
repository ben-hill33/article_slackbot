# Requirements

- Must accept queries or categories for areas I'm interested in
- Must accept sources if I want to limit to specific publications
- Should integrate with a publication api to retrieve article headlines for each category/query.
- Should provide functionality to post separate categories to separate channel
- Each post should include the article, description and a link to the article

# Design

- Article helper interface
  - Connect to the API
  - Query the top headlines based on config
- Slack API interface / Facade
  - Connect to the API
  - Structure data in desired message format
  - Send msg to a specified channel
- Query object
  - Encapsulate all query logic and perform data checks if needed
  - Map a query to a channel
  - Map query to the name of our result set
- Config
  - House all constants / settings
  - Contain an iterable of query objects
- Runner
  - Use the objects to implement the behavior we want and execute the program

# Happy Path

1. Use config file to get a set of queries we want to use for our article search.
2. Iterate overy query objects and call medium api for each to get top headlines.
3. Format slack messages according to preferred style/layout.
4. Send slack messages to the specified channel.
5. Exit.
