# Features

* Run unlimited accounts simultaneously to add members.
* Auto-distribute CSV files based on account count.
* Scrape active members from any public group.
* Add members by username or user ID.
* Minimal account ban risk.
* Auto-join public groups for faster member addition.
* Filter and remove banned accounts easily.
* Cross-platform, best on Windows.
* TG stores unlimited accounts for adding.
* Scripts launch automatically based on account count.


# How to use

* Install Requirements

```bash
  pip install -r requirements.txt
```

* If run error try something it out of date
```bash
  pip install --upgrade telethon
```



### MANAGER.py

1. Create Telegram accounts using virtual numbers.
2. Go to `my.telegram.org` for user authentication.
3. Access API Development Tools, fill out the form, and select 'Other' with a reason (e.g., 'App testing tool Telegram').
4. Obtain your API ID and API hash for `manager.py`.
5. Launch `manager.py` in CMD: `python manager.pyc`.
6. Choose the first option for new accounts or the second to add to existing ones.
7. Enter values and type 'y' for multiple accounts.

> [!CAUTION]
> Accounts are stored in `Vars.txt.` Do not delete it.

8. To remove banned accounts, select the banfilter option. It will update `Vars.txt.`.

---

### SCRAPER.PY

1. Launch the scraper to gather users from a public group.
2. In CMD, run: `python scraper.py`.
3. Enter the group username `(omit @, e.g., for @this_group, enter 'this_group')`.

> [!TIP]
> First use may require a login code. Scraped accounts save to `members.csv`.

---

### TSADDER.PY

1. Launch to add users: `python tsadder.py`.
2. Create sessions for all accounts and enter the login code (if prompted).
3. Filter out banned accounts. Enter the public group username.
4. It will redistribute members.csv into segments `(e.g., members0.csv, members1.csv)`.
5. Specify the number of accounts to use `(recommended: 10+)`.
6. Choose to add by username or by ID.

> [!NOTE]
> Adding by ID uses user IDs; adding by username requires users to have usernames.



## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://windymaster009.github.io/kevin.github.io/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/kevin-nhim-678574218/)



## License

[MIT](https://choosealicense.com/licenses/mit/) License

Copyright (c) [2025] [Windy]



![Logo](https://media3.giphy.com/media/HLB0nLA36GCCo6JuB5/200.gif)

