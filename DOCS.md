# Slack setup

1. If you don't have a Slack account, [create one here](https://slack.com/).
2. Go to [slack api website](https://api.slack.com/) and click `Create an app`.
3. Choose configuration as `From scratch`.
4. Name your project and select your workspace.
5. Scroll down to `Scopes` and `Add an OAuth Scope`.
   - Choose (at least): `chat:write`,
   - `chat:write.customize`
6. Scroll back up and click `Install to workspace`.
7. Select `Allow`.
8. Copy `Bot User OAuth Token`
9. Open Slack Desktop app.
10. Add a new channel.
11. Add another channel for a different category if you wish.
12. Select one of the channels you just created.
13. Hit the `i` icon (upper right)
14. Select `More`
15. Select your bot.

# API Setup

- Go to [Medium](https://github.com/Medium/medium-api-docs)
  - Read through their API documentation.
- Get an integration token for **your use only**.
  - Copy and paste token into `.env`

# Development environment setup

- Create project directory and cd into it.
- I used [python poetry](https://python-poetry.org/) for my virtual environment.
- Once you have changed directories into your project folder:
  - `$ poetry init -n`
  - Poetry add the following dependencies:
    - `$ slack-sdk`
    - `$ pytz`
    - `$ python-dateutil`
    - `$ pytest`
    - `$ pytest-mock`
